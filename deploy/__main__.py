import pulumi
import pulumi_aws as aws
import json
from pathlib import Path

# Create an S3 bucket
cf_templates_bucket = aws.s3.Bucket(
    "cf-templates-bucket",
    bucket="lbr-cfn-templates",  # Replace with your desired bucket name
    force_destroy=True,
    versioning={"enabled": True},
    website={"index_document": "index.html"},
    tags={
        "Name": "Public CloudFormation Templates Bucket",
        "Environment": "Production",
    },
)

aws.s3.BucketOwnershipControls(
    "cf-templates-bucket",
    bucket=cf_templates_bucket.bucket,
    rule=aws.s3.BucketOwnershipControlsRuleArgs(
        object_ownership="BucketOwnerPreferred",
    ),
    opts=pulumi.ResourceOptions(parent=cf_templates_bucket),
)

# Create a bucket policy to allow public read access
bucket_policy = aws.s3.BucketPolicy(
    "bucket-policy",
    bucket=cf_templates_bucket.id,
    policy=cf_templates_bucket.id.apply(
        lambda id: json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "PublicReadGetObject",
                        "Effect": "Allow",
                        "Principal": "*",
                        "Action": ["s3:GetObject"],
                        "Resource": [f"arn:aws:s3:::{id}/*"],
                    }
                ],
            }
        )
    ),
    opts=pulumi.ResourceOptions(parent=cf_templates_bucket),
)

# Block public access settings
block_public_access = aws.s3.BucketPublicAccessBlock(
    "public-access-block",
    bucket=cf_templates_bucket.id,
    block_public_acls=False,
    block_public_policy=False,
    ignore_public_acls=False,
    restrict_public_buckets=False,
    opts=pulumi.ResourceOptions(parent=cf_templates_bucket),
)

parent_dir = Path('..').resolve()
uploaded_files = []

for dir_path in parent_dir.iterdir():
    if dir_path.is_dir():
        template_path = dir_path / 'template.yaml'
        if template_path.exists():
            file_name = template_path.name
            dir_name = template_path.parent.name
            key = f"{dir_name}/{file_name}"
            
            bucket_object = aws.s3.BucketObject(
                f"template-{dir_name}",
                bucket=cf_templates_bucket.id,
                key=key,
                source=pulumi.FileAsset(str(template_path)),
                content_type="application/yaml",
                acl="public-read",
                opts=pulumi.ResourceOptions(parent=cf_templates_bucket),
            )
            uploaded_files.append(bucket_object)

# Export the bucket name and website endpoint
pulumi.export("bucket_name", cf_templates_bucket.id)
pulumi.export("website_endpoint", cf_templates_bucket.website_endpoint)
