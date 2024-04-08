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

The advantage of using an azd template is that you get a good start for both the function code as well as the infrastructure-as-code. 

The template creates assumes it is created in the root of a repository. In this case, it is created a in folder, and the GitHub Actions file in .github/workflows has to be moved/copied to the root. And then the action needs to know its working-directory explicitly like:
```
jobs:
  build:
    runs-on: ubuntu-latest
    defaults: 
      run:
        working-directory: ./5azd

```

[Source](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/configure-devops-pipeline)

[Home](../README.md)