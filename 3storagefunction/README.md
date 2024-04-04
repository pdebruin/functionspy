# functionspy

## 3 Storage function
This sample follows [2 Function storage](../2functionstorage/) and extends it with an input binding from a storage account queue. 

```
python -m venv .venv
source .venv/bin/activate
sudo apt-get install python3-venv

func init --python
func new --name QueueExample --template "Queue trigger"
    queuename outqueue 
    queueconnectionstring AzureWebJobsStorage

functionapp=functionspyfa
func azure functionapp fetch-app-settings $functionapp

func start

func azure functionapp publish $functionapp

```

The end state of your function code should look like

```

import azure.functions as func
import logging

app = func.FunctionApp()

@app.queue_trigger(arg_name="azqueue", queue_name="outqueue",
                               connection="AzureWebJobsStorage") 
def QueueExample(azqueue: func.QueueMessage):
    logging.info('Python Queue trigger processed a message: %s',
                azqueue.get_body().decode('utf-8'))

```

[Source](https://learn.microsoft.com/azure/azure-functions/functions-create-storage-queue-triggered-function)

[Home](../README.md)