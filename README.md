
# Azure

## Creating variables
     set AZ_LOCATION=eastus
     set AZ_RESOURCE_GROUP_NAME=rg-AlpacaFunctions
     set AZ_PLAN=FREE
     set AZ_FUNC_NAME=funcBuyRandomETF
     set AZ_FUNC_STORAGE_NAME=alpacafunctionsstore

## Creating resource group and storage if needed
    az group create --name %AZ_RESOURCE_GROUP_NAME% --location %AZ_LOCATION%
    az storage account create --resource-group %AZ_RESOURCE_GROUP_NAME% --name %FUNC_STORAGE_NAME% --sku Standard_LRS

## Create and deploy Azure function
Go to the folder you have the python script

    az login
    func init BuyRandomETF --python  #### this creates are sub-folder with some files
    cd BuyRandomETF
    func new --name funcBuyRandomETF --template "HTTP trigger" --authlevel "anonymous" #### this creates a subfolder in subfolder
    func start #### try locally
    az functionapp create ^
          --consumption-plan-location %AZ_LOCATION% ^
          --resource-group %AZ_RESOURCE_GROUP_NAME% ^
          --runtime python ^
          --runtime-version 3.9 ^
          --functions-version 4 ^
          --name %AZ_FUNC_NAME% ^
          --os-type linux ^
          --storage-account %AZ_FUNC_STORAGE_NAME%
    func azure functionapp publish %AZ_FUNC_NAME%
    func azure functionapp logstream %AZ_FUNC_NAME% --browser

## Quickly deploy Dash file as Azure Web App
     az login
     az webapp up 
          --name $APP_SERVICE_NAME 
          --runtime $RUNTIME 
          --resource-group $RESOURCE_GROUP_NAME 
          --sku $PLAN
  Set the appsettings for the API key (the command is in .gitignore file)


## Help commands for Azure CLI
    func --version
    az --version
    az appservice list-locations --sku FREE
    az webapp list-runtimes
    func templates list -l python

## Time triggers examples
    0 * * * * *	every minute
    0 */5 * * * *	every 5 minutes
    */15 * * * * *	every 15 seconds
    0 0 * * * *	every hour
    0 0 */6 * * *	every 6 hours
    30 5 /6 * * *	every 6 hours at 5 minutes and 30 seconds
    0 0 8-18 * * *	every hour between 8-18

    0 0 0 * * *	every day
    0 0 10 * * *	every day at 10:00:00
    11 5 23 * * *	daily at 23:05:11

    0 0 * * * 1-5	every hour on workdays
    0 0 0 * * 0	every sunday
    0 0 9 * * MON	every monday at 09:00:00
    0 0 0 1 * *	every 1st of month
    0 0 0 1 1 *	every 1st of january
    0 0 * * * SUN	every hour on sunday
    0 0 0 * * SAT,SUN	every saturday and sunday
    0 0 0 * * 6,0	every saturday and sunday
    0 0 0 1-7 * SUN	every first sunday of the month at 00:00:00

## Git

Init

    git init
    git add .
    git commit -m "initial commit"

    git remote add origin https...
    git branch -M main
    git push -u origin main

Maintain

    git add -A
    git commit -m "Update"
    git push

Update local content from Github: 

    git pull origin main


## Conda Virtual Environments for Windows:

    conda env list 
    conda create -n alpaca_env 
    conda install -n alpaca_env python #### or: conda install pip
    conda activate alpaca_env
    pip install -r requirements.txt
    conda deactivate
    conda env remove -n alpaca_env
