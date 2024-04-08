# functionspy

## 5 azd
The previous steps described creating functions locally, deploying them to Azure and setting up version control with automation. Azure developer cli (azd) provides an integrated way to do this all at once. 

Make sure you have [the latest version of azd installed](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd).

Next, select a template from ``` azd template list ``` or [the template library](https://azure.github.io/awesome-azd). The official [todo sample](https://github.com/Azure-Samples/todo-python-mongo-swa-func) is a good starting point; it includes more Azure services than needed, but you can easily remove them. 

Create a virtual environment
```
azd version
azd auth login
azd init --template Azure-Samples/todo-python-mongo-swa-func
azd pipeline config

```

[Source]()

[Home](../README.md)