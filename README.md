## How to describe the AWS VPC  using boto3.

#### Amazon Virtual Private Cloud (Amazon VPC) enables you to launch AWS resources into a virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS. You can follow this [link](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) to know more.

-------------

**Files:** 
```
    describe_VPC.py
```

## Apply the script

1. First configure the aws credentials using aws-cli.

        aws configure

2. Now, from the current directory run the following command to create the AWS VPC.

        python3 describe_VPC.py
