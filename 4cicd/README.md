# functionspy

## 4 CICD
This sample doesn't follow a specific previous step, although code of [an existing function](../2functionstorage/) in a repository helps to have a deployable source. 

You can configure CICD in a few ways including Azure Functions deployment center, az cli, and manually in GitHub. 

Deployment center gave me the github action yml in this folder. The changes I made:
* Update the name

* Update the AZURE_FUNCTIONAPP_PACKAGE_PATH to the folder with the function to be built

* Update the trigger (on | push | path) to only respond to changes in the function's folder 

```



```
At this point you can use the so called inner loop to develop and run functions locally and use the outerloop to store edits in version control with automated deployment to a central location for others to access them. 

When your functions are ready for production you should look at Staging slots, which help the experience of your Functions' users.

[Source](https://learn.microsoft.com/azure/azure-functions/functions-how-to-github-actions)

[Home](../README.md)
