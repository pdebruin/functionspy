import azure.functions as func
import datetime
import json
import logging
import azurefunctions.extensions.bindings.blob as blob

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="blobname",
                               connection="BlobStorageConnectionString") 
def BlobTrigger(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
