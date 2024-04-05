import os
import base64
import json
from azure.identity import ClientSecretCredential
from azure.mgmt.containerinstance import ContainerInstanceManagementClient
from azure.identity import DefaultAzureCredential


# Set your Azure Resource Group name
RESOURCE_GROUP = "dohoney-conf-compute"
print(os.environ)

# Get a credential for authentication
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
tenant_id = os.environ.get('TENANT_ID')
credential = ClientSecretCredential(tenant_id, client_id, client_secret)

# Get the subscription ID
myJWT = credential.get_token('https://management.azure.com/.default').token

# Create a client for container instance management
client = ContainerInstanceManagementClient(credential, myJWT)

def list_container_groups():
    """
    Lists all container groups in the specified Azure Resource Group.

    Returns:
        None
    """
    # List all container groups in the resource group
    container_groups = client.container_groups.list_by_resource_group(RESOURCE_GROUP)

    for container_group in container_groups:
        # Get the container group details
        container_group_details = client.container_groups.get(RESOURCE_GROUP, container_group.name)

        # Extract the required details
        resource_id = container_group_details.id
        location = container_group_details.location
        containers = container_group_details.containers
        image = containers[0].image if containers else None
        region = location
        conf_data = container_group_details.tags.get('confidentialComputeProperties.ccePolicy', None)

        # Print the details
        print(f"Resource ID: {resource_id}")
        print(f"Subscription: {SUBSCRIPTION_ID}")
        print(f"Docker/ACR Image: {image}")
        print(f"Azure Region: {region}")
        print("Container Events:")
        for container in containers:
            print(container.instance_view.events)

        # Base 64 decode the confidential compute data
        if conf_data:
            print(base64.b64decode(conf_data).decode())
        print("-------------------------")


if __name__ == "__main__":
    list_container_groups()
