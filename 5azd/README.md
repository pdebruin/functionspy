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

The template assumes it is created in the root of a repository, while here it is created in a folder. Move the GitHub Actions file in .github/workflows to the root, and add the working-directory explicitly like:
```
jobs:
  build:
    runs-on: ubuntu-latest
    defaults: 
      run:
        working-directory: ./5azd

```

While modifying existing templates, you may want to rollback your code to a past version that worked, which goes like:
```
git revert --no-commit <commit#>..HEAD
git commit
```

[Source](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/configure-devops-pipeline)

[Home](../README.md)