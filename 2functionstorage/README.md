# functionspy

## 2 Function storage
This sample follows [1 Function](../1function/) and extends it with an output binding to a storage account queue. 

```
functionapp=functionspyfa
func azure functionapp fetch-app-settings $functionapp
func azure functionapp publish $functionapp
```

```
import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="HttpExample", auth_level=func.AuthLevel.ANONYMOUS)
@app.queue_output(arg_name="msg", queue_name="outqueue", connection="AzureWebJobsStorage")
def HttpExample(req: func.HttpRequest, msg: func.Out [func.QueueMessage]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        msg.set(name)
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
```

[Source](https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-output-binding-storage-queue-cli)

[Home](../README.md)