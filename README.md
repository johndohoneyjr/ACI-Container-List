## ACI Container Information

In order to use these programs or shell scripts, you will need to set up a Service Principal in Entra, and set the CLIENT_ID, CLIENT_SECRET, AZURE_SUBSCRIPTION_ID and TENANT_ID into your Windows Environment

Sanity check in Powershell:
```bash
$ gce env:*
```
Next you will need to add the value of your AZURE_SUBSCRIPTION_ID into your environment
Sanity check in Powershell:
```bash
$ gce env:AZURE_SUBSCRIPTION_ID
```

The necessary Python modules can then be installed:

```bash
pip install -r requirements.txt
```
## Build and Test

```pwsh
  PS testContainer.ps1
  docker ps
  curl 
  uri: http://localhost:5000/container_groups?resourceGroupName=aci-test-me&containerGroupName=testme
```

```
Sample JSON respons payload from test Hello World ACI Image
{
    "id": "/subscriptions/9bb9f5c1-2e1a-4f65-a451-3e60c0a3f1cc/resourceGroups/aci-test-me/providers/Microsoft.ContainerInstance/containerGroups/testme",
    "location": "eastus",
    "name": "testme",
    "properties": {
        "containers": [
            {
                "name": "testme",
                "properties": {
                    "configMap": {
                        "keyValuePairs": {}
                    },
                    "environmentVariables": [],
                    "image": "mcr.microsoft.com/azuredocs/aci-helloworld:latest",
                    "instanceView": {
                        "currentState": {
                            "detailStatus": "",
                            "startTime": "2024-04-10T21:17:12.571Z",
                            "state": "Running"
                        },
                        "events": [
                            {
                                "count": 1,
                                "firstTimestamp": "2024-04-10T21:17:03Z",
                                "lastTimestamp": "2024-04-10T21:17:03Z",
                                "message": "Successfully pulled image \"mcr.microsoft.com/azuredocs/aci-helloworld@sha256:565dba8ce20ca1a311c2d9485089d7ddc935dd50140510050345a1b0ea4ffa6e\"",
                                "name": "Pulled",
                                "type": "Normal"
                            },
                            {
                                "count": 1,
                                "firstTimestamp": "2024-04-10T21:17:03Z",
                                "lastTimestamp": "2024-04-10T21:17:03Z",
                                "message": "pulling image \"mcr.microsoft.com/azuredocs/aci-helloworld@sha256:565dba8ce20ca1a311c2d9485089d7ddc935dd50140510050345a1b0ea4ffa6e\"",
                                "name": "Pulling",
                                "type": "Normal"
                            },
                            {
                                "count": 1,
                                "firstTimestamp": "2024-04-10T21:17:12Z",
                                "lastTimestamp": "2024-04-10T21:17:12Z",
                                "message": "Started container",
                                "name": "Started",
                                "type": "Normal"
                            }
                        ],
                        "restartCount": 0
                    },
                    "ports": [
                        {
                            "port": 80,
                            "protocol": "TCP"
                        }
                    ],
                    "resources": {
                        "requests": {
                            "cpu": 1,
                            "memoryInGB": 1.5
                        }
                    }
                }
            }
        ],
        "initContainers": [],
        "instanceView": {
            "events": [],
            "state": "Running"
        },
        "ipAddress": {
            "ip": "20.124.165.182",
            "ports": [
                {
                    "port": 80,
                    "protocol": "TCP"
                }
            ],
            "type": "Public"
        },
        "isCreatedFromStandbyPool": false,
        "isCustomProvisioningTimeout": false,
        "osType": "Linux",
        "provisioningState": "Succeeded",
        "provisioningTimeoutInSeconds": 1800,
        "restartPolicy": "OnFailure",
        "sku": "Standard"
    },
    "tags": {},
    "type": "Microsoft.ContainerInstance/containerGroups"
}
```
ACI does allow for Docker Swarms or Sidecars, so the return Containers array can be iterated over to access all containers in the container group.  This is a simple example, and probably what 80% of our customers use -- a single container.
