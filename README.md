# Installation steps
## Environment Preparation
1. Download the Virtual Machine provided through team OneDrive.
2. Install necessary virtual drivers to run on the local machine.
3. Environment should be prepared with the following MySQL configuration:
        * MySQL 3.7 or higher
        * Username: root
        * Password: please
4. Environment should be prepared with the following Python configuration:
        * Python 3.8 or higher
        * Pip3
5. Enviroment should be prepared with the following Python plugins:
        * django
        * djangorestframework
        * django-filter
        * django-crispy-forms
        * mysql-client
  
## Service Preparation
1. Deploy MySQL script to populate MySQL with the database and tables.
2. Select the new `bikeshop` database.
3. Deploy MySQL script to populate the tables with data.

## Running the code
1. To run the API, execute `python3.8 manage.py runserver <IP1:PORT1>`.
2. To run the frontend, execute `python3.8 manage.py runserver <IP2:PORT2>`.
3. Either IP1 and IP2 must be different, or PORT1 and PORT2 must be different.

## Accessing the API directly
1. Visit the IP and PORT specified for the API server.
2. Navigate to `IP:PORT/api/v0`.
3. For searching functionality, use query string `?search=<TEXT>`.
4. For pagination functionality, use query string `?limit=<LIMIT>&offset=<OFFSET>`.
5. For default functionality, access the URI for that specific endpoint.
