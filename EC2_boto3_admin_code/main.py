import boto3
from pprint import pprint

# This demonstrates is about some ec2 operation example by using boto3
manageConsole = boto3.session.Session(profile_name="root")
ec2 = manageConsole.resource(service_name="ec2", region_name="ap-east-1")


def create_instances():
    ec2.create_instances(
        ImageId="ami-0c1d5a98de68acf64",
        MinCount=1,
        MaxCount=1,
        InstanceType="t3.micro",
        KeyName="Daniel_AWS_Key_apeast1"
    )


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
