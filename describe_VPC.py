# By MuZakkir Saifi
# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

REGION = input("Please enter the REGION")

# this is the configration for the logger_for

logger_for = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

response = boto3.client("ec2", region_name=REGION)


def describe(tag, tag_values, max_items):

    try:
        pag = response.get_paginator('describe_vpcs')

        response_iterator = pag.paginate(
            Filters=[{
                'Name': f'tag:{tag}',
                'Values': tag_values
            }],
            PaginationConfig={'MaxItems': max_items})

        result = response_iterator.build_full_result()

        list = []

        for page in result['Vpcs']:
            list.append(page)

    except ClientError:
        logger_for.exception('OOPs can not  describe your VPCs.')
        raise
    else:
        return list


if __name__ == '__main__':
    TAG = input("Enter the TAG NAME")
#  empty list
    VALUES = []
    
    # user will enter the number of elements
    number = int(input("Enter number of elements : "))
    for i in range(0, n):
        elements = input("enter you value")
    
        VALUES.append(elements)
    MAXIMUM_ITEMS = int(input("Enter the Value for MAX ITEMS"))
    vpcs = describe(TAG, VALUES, MAXIMUM_ITEMS)
    logger_for.info('Here is your VPC Details: ')
    for vpc in vpcs:
        logger_for.info(json.dumps(vpc, indent=4) + '\n')