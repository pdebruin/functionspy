# functionspy

## 8 Timer
This sample shows an Azure Function in Python with timer trigger.

```
func init --python
func new 
```
* Timer Trigger
* timer_trigger
* [0 */5 * * * *]

### Run locally
```
func start
```
Log:
Found Python version 3.11.5 (python3).

Azure Functions Core Tools
Core Tools Version:       4.0.5530 Commit hash: N/A +c8883e7f3c06e2b424fbac033806c19d8d91418c (64-bit)
Function Runtime Version: 4.28.5.21962

[2024-06-13T11:38:56.186Z] Customer packages not in sys path.
[2024-06-13T11:38:57.133Z] Worker process started and initialized.

Functions:

        timer_trigger: timerTrigger

For detailed output, run func with --verbose flag.
[2024-06-13T11:39:02.036Z] Host lock lease acquired by instance ID '000000000000000000000000C7C8539E'.
[2024-06-13T11:40:00.072Z] Executing 'Functions.timer_trigger' (Reason='Timer fired at 2024-06-13T13:40:00.0307363+02:00', Id=7dc1b3a8-de25-4092-aa34-f72915d0dcb8)
[2024-06-13T11:40:00.141Z] Python timer trigger function executed.
[2024-06-13T11:40:00.164Z] Executed 'Functions.timer_trigger' (Succeeded, Id=7dc1b3a8-de25-4092-aa34-f72915d0dcb8, Duration=119ms)

### Run in Azure

```
region=northeurope
resourcegroup=functionspy8
storageaccount=functionspy8sa
pythonversion=3.11
functionapp=functionspy8fa
az group create --name $resourcegroup --location $region
az storage account create --name $storageaccount --location $region --resource-group $resourcegroup 
az functionapp create --resource-group $resourcegroup --consumption-plan-location westeurope --runtime python --runtime-version $pythonversion --functions-version 4 --name $functionapp --os-type linux --storage-account $storageaccount
func azure functionapp publish $functionapp
```
Log:
13/06/2024, 11:50:00,002
Information
Executing 'Functions.timer_trigger' (Reason='Timer fired at 2024-06-13T11:50:00.0012937+00:00', Id=c94f7941-81a1-45c5-8dbd-8525da27126c)
13/06/2024, 11:50:00,028
Information
Python timer trigger function executed.
13/06/2024, 11:50:00,037
Information
Executed 'Functions.timer_trigger' (Succeeded, Id=c94f7941-81a1-45c5-8dbd-8525da27126c, Duration=36ms)

[Source](https://learn.microsoft.com/azure/azure-functions/create-first-function-cli-python)

[Home](../README.md)