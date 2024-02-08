az acr login --name robsonlab
docker build frontend/. -t robsonlab.azurecr.io/webapp-frontend:v2
docker push robsonlab.azurecr.io/webapp-frontend:v2
docker build backend/. -t robsonlab.azurecr.io/webapp-backend:v2
docker push robsonlab.azurecr.io/webapp-backend:v2