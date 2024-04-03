# functionspy

## 1 Function
This sample shows a simple Azure Function in Python to start with. 

```
func init --python
func new --name HttpExample --template "HTTP trigger" --authlevel "anonymous"
```

Use the following command to start the function in your environment.

```
func start
```

Ready to deploy to Azure?

```
region=westeurope
resourcegroup=functionspy
storageaccount=myuniquename
pythonversion=$pythonversion
functionapp=$functionapp
az group create --name $resourcegroup --location $region
az storage account create --name $storageaccount --location $region --resource-group $resourcegroup 
az functionapp create --resource-group AzureFunctionsQuickstart-rg --consumption-plan-location westeurope --runtime python --runtime-version $pythonversion --functions-version 4 --name $functionapp --os-type linux --storage-account $storageaccount
func azure functionapp publish $functionapp
```

[Source](https://learn.microsoft.com/azure/azure-functions/create-first-function-cli-python)

[Home](../README.md)