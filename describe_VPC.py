# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = input("Please enter the AWS_REGION")

# this is the configration for the logger

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_client = boto3.client("ec2", region_name=AWS_REGION)


def describe_vpcs(tag, tag_values, max_items):

    try:
        paginator = vpc_client.get_paginator('describe_vpcs')

        response_iterator = paginator.paginate(
            Filters=[{
                'Name': f'tag:{tag}',
                'Values': tag_values
            }],
            PaginationConfig={'MaxItems': max_items})

        full_result = response_iterator.build_full_result()

        vpc_list = []

        for page in full_result['Vpcs']:
            vpc_list.append(page)

    except ClientError:
        logger.exception('This Could not describe VPCs.')
        raise
    else:
        return vpc_list


if __name__ == '__main__':
    TAG = 'Techhub_VPC'
    TAG_VALUES = ['Custom_VPC']
    MAX_ITEMS = 10
    vpcs = describe_vpcs(TAG, TAG_VALUES, MAX_ITEMS)
    logger.info('Here is your VPC Details: ')
    for vpc in vpcs:
        logger.info(json.dumps(vpc, indent=4) + '\n')