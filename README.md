# bartender-backend

Backend for some website, integrated with 
Cloudinary for media storage. 

## Requirements
- Docker
- docker-compose

## How to Run
1. Create `.env` files with format below
   ```
   API_KEY=<your-api-key>
   API_SECRET=<your-api-secret>
   CLOUD_NAME=<your-cloud_name>
   SECRET_KEY='changeme'
   CLEARDB_DATABASE_URL='mysql://user:password@hosts:3306/db-name'
   DEPLOY=DEV
   ```
2. Build the container (once the docker image was build, no need to repeat this step unless there are changes in the dockerfiles)
   ```
   docker build . -t bartender-backend 
   ```
3. Run the container <br>
   ```
   docker-compose up
   ```
4. Run the migration <br>
   ```
   docker-compose exec web python manage.py migrate
   ```




# Docs
Here is the API docs 
 - [Markdown](docs/docs.md)
 - [Postman](https://documenter.getpostman.com/view/8693382/TVejiWJX)
