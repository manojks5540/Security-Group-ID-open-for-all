#!/us/bin/python

import boto3

def unique(list1):

    unique_list = []

    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    print(unique_list)



def security_group_check ():

    regions = ['us-east-1', 'ap-southeast-1']
    
    for region in regions:

        sg_id_list= []    

        client = boto3.client('ec2', region_name=region)

        response = client.describe_security_groups()

        print("Sg id open for public in region  " + region)

        for sg in response['SecurityGroups']:
             sgid=sg['GroupId'] 
             for rules in sg['IpPermissions']:
                 for i in rules['IpRanges']: 
                      if i['CidrIp'] == '0.0.0.0/0':
                            sg_id_list.append(sgid)


        unique(sg_id_list)

security_group_check()    
