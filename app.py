from flask import Flask, request, jsonify
import os
from azure.identity import ClientSecretCredential
from azure.mgmt.containerinstance import ContainerInstanceManagementClient
import requests

app = Flask(__name__)
## REference https://learn.microsoft.com/en-us/rest/api/container-instances/container-groups/get?view=rest-container-instances-2023-05-01&tabs=HTTP
@app.route('/container_groups', methods=['GET'])
def get_container_groups():
    # Get the resource group from the query parameters
    resource_group = request.args.get('resourceGroupName')
    container_group = request.args.get('containerGroupName')

    # Get the subscription ID
    subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')

    # Set your Azure Management API version
    api_version = '2023-05-01'

    # Get a credential for authentication
    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')
    tenant_id = os.environ.get('TENANT_ID')
    credential = ClientSecretCredential(tenant_id, client_id, client_secret)

    # Get the subscription ID
    access_token = credential.get_token('https://management.azure.com/.default').token

    # Set the base URL for the Azure Management API
    base_url = f'https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}'

    # Set the headers for the API requests
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # List all container groups in the resource group
    response = requests.get(f'{base_url}/providers/Microsoft.ContainerInstance/containerGroups/{container_group}?api-version={api_version}', headers=headers)
    container_groups = response.json()

    return jsonify(container_groups)

if __name__ == '__main__':
    app.run(debug=True)