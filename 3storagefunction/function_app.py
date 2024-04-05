import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.queue_trigger(arg_name="azqueue", queue_name="outqueue",
                               connection="AzureWebJobsStorage") 
def QueueExample(azqueue: func.QueueMessage):
    logging.info('Python Queue trigger processed a CICD message: %s',
                azqueue.get_body().decode('utf-8'))
