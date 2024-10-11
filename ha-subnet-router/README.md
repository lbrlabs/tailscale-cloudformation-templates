# Tailscale Subnet Router CloudFormation Template

This CloudFormation template deploys a Tailscale subnet router in AWS, allowing you to connect your AWS VPC to your Tailscale network. The template creates an Auto Scaling Group with EC2 instances running as Tailscale subnet routers.

## Quick Deploy

Click the button below to deploy this template to your AWS account:

[![Deploy to AWS CloudFormation](https://img.shields.io/badge/Deploy%20to-AWS%20CloudFormation-orange.svg?style=flat)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=TailscaleSubnetRouter&templateURL=https://lbr-cfn-templates.s3.us-west-2.amazonaws.com/ha-subnet-router/template.yaml)

## Features

- Supports selecting an existing VPC
- Configurable Auto Scaling Group for high availability
- Customizable Tailscale settings
- Automatic IP forwarding configuration
- IMDSv2 support for enhanced security
- Custom hostname option for Tailscale nodes
- Optional open inbound security group for Tailscale UDP port

## Parameters

The template includes the following parameters:

- `VpcId`: Select a VPC for the Tailscale subnet router
- `SubnetIds`: List of Subnet IDs for the Auto Scaling Group
- `TailscaleAuthKey`: Tailscale authentication key
- `AmiId`: AMI ID for the EC2 instances
- `InstanceType`: EC2 instance type (default: t3.micro)
- `MinSize`, `MaxSize`, `DesiredCapacity`: Auto Scaling Group size configuration
- `AdvertiseTags`: ACL tags to request (comma-separated list)
- `EnableSSH`: Enable SSH access via Tailscale
- `Track`: Version of the Tailscale client to install (stable or unstable)
- `MaxRetries`: Maximum number of retries to connect to the control server
- `RetryDelay`: Delay in seconds between retries to connect to the control server
- `Hostname`: Custom hostname for the Tailscale node (optional)
- `OpenInboundSecurityGroup`: Option to open UDP port 41641 on the security group

## Usage

1. Click the "Deploy to AWS" button above.
2. Log in to your AWS account if prompted.
3. Review the stack details and parameters.
4. Provide values for the required parameters, including your Tailscale authentication key.
5. Click "Create stack" to deploy the Tailscale subnet router.

## Customization

You can fork this repository and modify the template to suit your specific needs. Some areas you might want to customize:

- Instance type and AMI ID
- VPC and subnet selection
- Tailscale configuration options
- Security group rules

## Outputs

The template provides the following outputs:

- `AutoScalingGroupName`: Name of the created Auto Scaling Group
- `SecurityGroupId`: ID of the Security Group attached to the instances
- `SelectedVpcId`: ID of the VPC used for deployment
- `VpcCidrBlock`: CIDR block of the selected VPC

## Security Considerations

- IMDSv2 is enabled by default for enhanced instance metadata security.
- Ensure that your Tailscale authentication key is kept secret and not shared.
- Review and adjust the security group settings as needed for your environment.
- Consider using AWS Secrets Manager to store sensitive information like the Tailscale auth key.
- The template includes an option to open the Tailscale UDP port (41641) on the security group. Use this feature cautiously and only when necessary.

## Notable Changes

- Added support for IMDSv2 to enhance instance security.
- Introduced a custom hostname option for Tailscale nodes.
- Simplified VPC selection to use an existing VPC.
- Added an option to open the inbound Tailscale UDP port on the security group.
- Implemented a retry mechanism for Tailscale setup to improve reliability.
- Included a Lambda function to retrieve VPC CIDR information dynamically.

## Contributing

Contributions to improve the template are welcome. Please submit pull requests or open issues to suggest changes or report problems.

## License

This project is licensed under the MIT License - see the LICENSE file for details.