# Define the local image name
$LOCAL_IMAGE = "container-metadata"

# Build the Docker image
docker build -t $LOCAL_IMAGE .

# Run the Docker container with environment variables
docker run -d --name metatest -p 5000:5000 `
  -e AZURE_SUBSCRIPTION_ID=$env:AZURE_SUBSCRIPTION_ID `
  -e CLIENT_ID=$env:CLIENT_ID `
  -e CLIENT_SECRET=$env:CLIENT_SECRET `
  -e TENANT_ID=$env:TENANT_ID `
  $LOCAL_IMAGE