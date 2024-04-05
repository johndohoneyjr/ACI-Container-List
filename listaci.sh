#!/bin/env bash

# This script lists the details of container groups in an Azure resource group.
# It retrieves the subscription ID, lists all container groups in the specified resource group,
# and extracts details such as resource ID, location, image, and container events for each container group.
az login

# Set your Azure Resource Group name
RESOURCE_GROUP="dohoney-conf-compute"

# Get the subscription ID
SUBSCRIPTION_ID=$(az account show --query id --output tsv)

# List all container groups in the resource group
CONTAINER_GROUPS=$(az container list --resource-group $RESOURCE_GROUP --query [].name --output tsv)

for CONTAINER_GROUP in $CONTAINER_GROUPS
do
    # Get the container group details
    CONTAINER_GROUP_DETAILS=$(az container show --name $CONTAINER_GROUP --resource-group $RESOURCE_GROUP)

    # Extract the required details
    RESOURCE_ID=$(echo $CONTAINER_GROUP_DETAILS | jq -r '.id')
    LOCATION=$(echo $CONTAINER_GROUP_DETAILS | jq -r '.location')
    # This could be a Docker Swarm or Side Car container(s)
    CONTAINERS=$(echo $CONTAINER_GROUP_DETAILS | jq -r '.containers[]')
    IMAGE=$(echo $CONTAINERS | jq -r '.image')
    REGION=$(echo $CONTAINER_GROUP_DETAILS | jq -r '.location')
    ConfData=$(echo $CONTAINER_GROUP_DETAILS | jq -r '.confidentialComputeProperties.ccePolicy')

    # Print the details
    echo "Resource ID: $RESOURCE_ID"
    echo "Subscription: $SUBSCRIPTION_ID"
    echo "Docker/ACR Image: $IMAGE"
    echo "Azure Region: $REGION"
    echo "Container Events:"
    echo $CONTAINER_GROUP_DETAILS | jq -r '.containers[].instanceView.events'
    #echo "-------------------------"
    # base 64 decode the confidential compute data
    #echo $(echo $ConfData | base64 --decode) 
    echo "-------------------------"
done