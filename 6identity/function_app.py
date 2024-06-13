import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

# @app.route(route="put_message")
# @app.service_bus_queue_output(arg_name="msg",
#                               connection="NAMESPACE_CONNECTION_STR",
#                               queue_name="servicebusqueuename")
# def HttpExample(req: func.HttpRequest, msg: func.Out [str]) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if name:
#         # msg.set("test")
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#              status_code=200
#         )

@app.service_bus_queue_trigger(arg_name="msg", queue_name="servicebusqueuename", connection="NAMESPACE_CONNECTION_STR") 
def ServicebusExample(msg: func.ServiceBusMessage):
    logging.info('Python ServiceBus Queue trigger processed a message: %s', msg.get_body().decode('utf-8'))
