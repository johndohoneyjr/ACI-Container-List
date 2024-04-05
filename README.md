## ACI Container Information

In order to use these programs or shell scripts, you will need to set up a Service Principal in Entra, and set the CLIENT_ID, CLIENT_SECRET, and TENANT_ID into your Windows Environment

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

ACI does allow for Docker Swarms or Sidecars, so the return Containers array can be iterated over to access all containers in the container group.  This is a simple example, and probably what 80% of our customers use -- a single container.
