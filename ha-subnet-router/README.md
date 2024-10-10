# Tailscale Subnet Router CloudFormation Template

This CloudFormation template deploys a Tailscale subnet router in AWS, allowing you to connect your AWS VPC to your Tailscale network. The template creates an Auto Scaling Group with EC2 instances running as Tailscale subnet routers.

## Quick Deploy

Click the button below to deploy this template to your AWS account:

[![Deploy to AWS](https://raw.githubusercontent.com/aws-samples/aws-cloudformation-button/main/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=TailscaleSubnetRouter&templateURL=https://raw.githubusercontent.com/yourusername/your-repo-name/main/tailscale-subnet-router-template.yml)

## Features

- Supports selecting an existing VPC or manually inputting a VPC ID
- Configurable Auto Scaling Group for high availability
- Customizable Tailscale settings
- Automatic IP forwarding and UDP offload configuration

## Parameters

The template includes the following parameters:

- `VpcSelectionMethod`: Choose to select an existing VPC or input a VPC ID manually
- `ExistingVpcId`: Select an existing VPC (if using the 'existing' selection method)
- `ManualVpcId`: Manually input a VPC ID (if using the 'manual' selection method)
- `SubnetIds`: List of Subnet IDs for the Auto Scaling Group
- `TailscaleAuthKey`: Tailscale authentication key
- `InstanceType`: EC2 instance type (default: t3.micro)
- `AmiId`: AMI ID for the EC2 instances
- `MinSize`, `MaxSize`, `DesiredCapacity`: Auto Scaling Group size configuration
- Various Tailscale configuration options (e.g., `EnableSSH`, `AcceptDNS`, `AdvertiseRoutes`, etc.)

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

- Ensure that your Tailscale authentication key is kept secret and not shared.
- Review and adjust the security group settings as needed for your environment.
- Consider using AWS Secrets Manager to store sensitive information like the Tailscale auth key.

## Contributing

Contributions to improve the template are welcome. Please submit pull requests or open issues to suggest changes or report problems.