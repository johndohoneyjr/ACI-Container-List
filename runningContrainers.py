import os
import base64
import json
from azure.identity import ClientSecretCredential
from azure.mgmt.containerinstance import ContainerInstanceManagementClient
import requests


# Set your Azure Resource Group name
RESOURCE_GROUP = "dohoney-conf-compute"

# Get the subscription ID
SUBSCRIPTION_ID = os.getenv('AZURE_SUBSCRIPTION_ID')

# Set your Azure Management API version
API_VERSION = '2021-03-01'

# Get a credential for authentication
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
tenant_id = os.environ.get('TENANT_ID')
credential = ClientSecretCredential(tenant_id, client_id, client_secret)

# Get the subscription ID
ACCESS_TOKEN = credential.get_token('https://management.azure.com/.default').token

# Set the base URL for the Azure Management API
BASE_URL = f'https://management.azure.com/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP}'

# Set the headers for the API requests
HEADERS = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

# List all container groups in the resource group
response = requests.get(f'{BASE_URL}/providers/Microsoft.ContainerInstance/containerGroups?api-version={API_VERSION}', headers=HEADERS)
container_groups = response.json()

for container_group in container_groups['value']:
    # Get the container group details
    container_group_details_url = container_group['id']
    response = requests.get(f'https://management.azure.com{container_group_details_url}?api-version={API_VERSION}', headers=HEADERS)
    container_group_details = response.json()

    # Extract the required details
    resource_id = container_group_details['id']
    location = container_group_details['location']
    containers = container_group_details['properties']['containers']
    image = containers[0]['properties']['image']  # Assuming there's at least one container
    region = container_group_details['location']

    # Print the details
    print(f"Resource ID: {resource_id}")
    print(f"Subscription: {SUBSCRIPTION_ID}")
    print(f"Docker/ACR Image: {image}")
    print(f"Azure Region: {region}")
    print("Container Events:")
    print(json.dumps(container_group_details['properties']['containers'][0]['properties']['instanceView']['events'], indent=4))
    print("-------------------------")
    # base 64 decode the confidential compute data
    # print(base64.b64decode(conf_data).decode())
    print("-------------------------")