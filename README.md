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
    * requests
    * radon (for local) or xenon (for CI/Testing)

## Service Preparation
1. Deploy MySQL script to populate MySQL with the database and tables.
2. Select the new `bikeshop` database.
3. Deploy MySQL script to populate the tables with data.

## Running the code
1. To run the API, execute `python3.8 api/manage.py runserver <IP1:PORT1>`.
2. To run the frontend, execute `python3.8 web/manage.py runserver <IP2:PORT2>`.
3. Either IP1 and IP2 must be different, or PORT1 and PORT2 must be different.

## Accessing the API directly
1. Visit the IP and PORT specified for the API server.
2. Navigate to `IP:PORT/api/v0`.
3. For searching functionality, use query string `?search=<TEXT>`.
4. For pagination functionality, use query string `?limit=<LIMIT>&offset=<OFFSET>`.
5. For default functionality, access the URI for that specific endpoint.

## Continuous Integration and Testing
* Continuous Integration is provided by Jenkins, through GitHub Actions.
    * See the `.github/workflows` directory for pipeline/workflow.
* Automated testing now performs two checks on the applications.
    * Django natively supports testing, provided by the `python3.8 manage.py test` command set.
    * Xenon (a wrapper for Radon) is an automated metrics suite, checking the cyclomatic complexity against a threshold value.
          * We use Xenon to verify that our code has a minimum complexity rank of B, keeping maintainability high.
    * If the Django tests fail, or if Xenon reports a complexity ranking lower than B, the automated tests will fail.
          * In either of these cases, the code will need to be revised accordingly.
