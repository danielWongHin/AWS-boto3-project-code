import boto3
from pprint import pprint

# This demonstrates is about some resources' operation example by using boto3
# All examples are using resources interface, a high-level abstraction compared to clients
# Document:  https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

# Create the manage Console (aka login), then, you can access the resource

manageConsole = boto3.session.Session(profile_name="root")
ec2 = manageConsole.resource(service_name="ec2", region_name="ap-east-1")
iam = manageConsole.resource(service_name="iam", region_name="ap-east-1")
s3 = manageConsole.resource(service_name="s3", region_name="ap-east-1")

# For STS there is only Client interface

sts = manageConsole.client(service_name="sts", region_name="ap-east-1")


# How to check the account ID
def sts_get_account_id():
    response = sts.get_caller_identity()
    pprint(response["Account"])


# How to list all the iam user

def list_iam_user():
    for user in iam.users.all():
        print(user.user_name)


# How to list all the S3 Bucket

def list_s3_bucket():
    for s3_bucket in s3.buckets.limit(5):
        print(s3_bucket.name)


# How to create instance
def create_instances():
    ec2.create_instances(
        ImageId="ami-0c1d5a98de68acf64",
        MinCount=1,
        MaxCount=1,
        InstanceType="t3.micro",
        KeyName="Daniel_AWS_Key_apeast1"
    )


# How to get the info of image, instance and volume
def get_image_and_instance_id():
    response = ec2.instances.all()

    for item in response:
        print("-----------------------")
        print(f"The instance id is {item.instance_id}\nThe image id is {item.image_id}")


def get_volume_info():
    for item_volumes in ec2.volumes.all():
        print("-----------------------")
        print(f"The volume id is {item_volumes.volume_id}")
        print(f"The Availability Zone is {item_volumes.availability_zone}")
        print(f"The Volume type is {item_volumes.volume_type}")


# How to operate the instances
def stop_instance():
    instance_id = input("Enter your instance id: ")
    instance = ec2.Instance(instance_id)
    instance.stop()


def terminate_instance():
    instance_id = input("Enter your instance id: ")
    instance = ec2.Instance(instance_id)
    instance.terminate()


def start_instance():
    instance_id = input("Enter your instance id: ")
    instance = ec2.Instance(instance_id)
    instance.start



