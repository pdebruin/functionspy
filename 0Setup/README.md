# functionspy

## 0 Setup
Warning: This page is opinionated :-) You can create Azure Functions in various ways including in the Azure portal, in VS Code and in the command-line. My preference is to create code with the least number of dependencies, and with the option to add it to version control for cicd. That is why this page describes steps to install tools on your local device. As a  shortcut, you can also use Azure cloud shell that has these installed. 

Before developing Azure Functions, install the following prerequisites:
Azure command-line interface
Python version supported by Functions version
Azurite storage emulator

Install core tools
```
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-$(lsb_release -cs)-prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list'
sudo apt-get update
sudo apt-get install azure-functions-core-tools-4
func --version
```

Create a virtual environment
```
python -m venv .venv
source .venv/bin/activate
sudo apt-get install python3-venv
```

[Source](https://learn.microsoft.com/azure/azure-functions/create-first-function-cli-python)

[Ref guide](https://learn.microsoft.com/azure/azure-functions/functions-reference-python)

[Home](../README.md)