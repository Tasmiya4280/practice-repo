import Boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket = 'abc',
)


def create_ec2_instance():
    ec2 = boto3.client('ec2', region_name='us-east-1')  

    response = ec2.run_instances(
        ImageId='ami-0c2b8ca1dad447f8a', 
        InstanceType='t2.micro',  
        KeyName='xyz', 
    )

    instance_id = response['Instances'][0]['InstanceId']
    print(f"Instance created with ID: {instance_id}")
    
create_ec2_instance()
