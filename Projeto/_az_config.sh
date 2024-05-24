SUBSCRIPTION="Azure subscription 1"
RESOURCEGROUP="dmaismarmitaria_group"
LOCATION="brazilsouth"
PLANNAME="ASP-dmaismarmitariagroup-8d66"
PLANSKU="F1"
SITENAME="dmaismarmitaria"
RUNTIME="PYTHON|3.12"

az webspp config set --resource-group $RESOURCEGROUP --name $SITENAME --startup-file "uvicorn app.main:app --host 0.0.0.0 --port 8000"