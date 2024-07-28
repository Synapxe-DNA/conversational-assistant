# Backend

## Backend Server

### Run backend detached

1. Go to root folder
2. Run `make backend-start` to start the backend server

### Run backend

#### This allows you to see the logs

1. Go to root folder
2. Run `make backend-run` to start the backend server

#### Stop backend

1. Go to root folder
2. Run `make backend-stop` to stop the backend server

## Speech services

### Setting up .env file

1. Create a `.env` file in the backend folder using the template in `.env.sample`

#### Getting Speech Resource ID

1. Select the correct resource
2. Under 'Resource Management' click on properties
3. Copy the 'Resource ID' from the properties tab and add it into your `.env` file

<img src="images/resourceid.png" alt="drawing" width="200"/>

### Getting Speech Region

1. In the same resource management tab, click on 'Keys and Endpoint'
2. Copy the 'Location/Region' into your `.env` file
