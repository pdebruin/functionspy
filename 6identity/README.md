# functionspy

## 6 Identity
This sample follows [2 Function storage](../2functionstorage/) and extends it with an input binding from a storage account queue. 


region=northeurope
resourcegroup=functionspy6
storageaccount=functionspy6sa
pythonversion=3.11
functionapp=functionspy6fa
az group create --name $resourcegroup --location $region
<!-- az storage account create --name $storageaccount --location $region --resource-group $resourcegroup 
az functionapp create --resource-group $resourcegroup --consumption-plan-location westeurope --runtime python --runtime-version $pythonversion --functions-version 4 --name $functionapp --os-type linux --storage-account $storageaccount
func azure functionapp publish $functionapp -->

server=functionspy6sv
database=functionspy6db

az sql server create --name $server --resource-group $resourcegroup --location $region --enable-ad-only-auth --external-admin-principal-type User --external-admin-name pidebrui --external-admin-sid 0a5c2d73-9bb3-47a8-8a81-f580b1a570d0

az sql db create -g $resourcegroup -s $server -n $database --compute-model Serverless -e GeneralPurpose -f Gen5 -c 2
--min-capacity 0.5  
--auto-pause-delay 720