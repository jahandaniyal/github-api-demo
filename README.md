# github-api-demo
A service for checking whether the provided GitHub repository is popular or not. </br>
Here, popular GitHub repository means one for which score >= 500 where score = num_stars * 1 + num_forks * 2.

## Service Description
- Given a github owner and repository name, this service will tell you if this repository is popular or not.
- Requires `access token` for restricted repositories. This token is passed as `**X-Github-Token**` in the Header
- Public repositories do not require any access token - however, GitHub API would restrict the number of requests you can make in this case.
- Response time: 150-300 ms.
- Uses docker for easy deployment.
- API documentation using OpenAPI specification (flasgger library enables this feature).
- Health check and monitoring using Prometheus and Grafana.

## Tech Stack
- Flask
- Marshmallow
- Pytest
- Prometheus
- Grafana
- Docker
- Flasgger - for generating OpenAPI specifications.
- Additional libraries:
  - requests

## OpenAPI specification
https://app.swaggerhub.com/apis/jahandaniyal/git-hub_api_demo_app/0.0.1

## Running the application
This application uses docker for building and running locally, tests are also run in dockerised container. </br>
Use the **Makefile** targets or alternative commands (shown below) to **build, run and test** the application.
 
### Build
**`make build`** or, </br>
**`docker-compose build --no-cache`**
### Run
**`make run`** or, </br>
**`docker-compose up`**
### Test
**`make test`** or, </br>
**`docker-compose up test`**

### USER Endpoints
* **/api/stats/{owner}/{repository}**
   * GET
   * Headers: X-Github-Token (Optional)

#### Application Demo
- To play around with the application, run the app and head over to : http://localhost:5000/apidocs/
- Expand the GET method, and click on `**Try it out**`.
- You will need to fill in **owner** and **repo**. example,
  - owner -> octocat
  - repo -> Hello-World
  - Then execute the request - as shown in the image below.
 - Alternatively, you can use **postman** or **curl** to try out the application.
![image](https://user-images.githubusercontent.com/4581090/161806246-a243be2e-6b48-46c4-81df-398c364eceed.png)

## Monitoring the application
### Check up-time
- Up-time status of the application can be viewed using : http://localhost:9090/targets 
- Stats are updated every 5 seconds, could also be changed in prometheus configuration (prometheus.yml).
![image](https://user-images.githubusercontent.com/4581090/161802349-73d267cc-3300-4c2e-86c0-faa37c0341ee.png)

### Metrics
- Metrics can be monitored using Grafana dashboard.
- However additional setup must be done to add datasource and upload the dashboard (using grafana_dashboard.json in /monitoring directory)
- To configure grafana dashboard:
  - Login to http://localhost:3000/login using **username**- admin , **password** - admin@123
  - Add a datasource prometheus, in URL use **http://172.16.238.11:9090**. 
  - Save and Test.
  - Now, add a new dashboard by clicking **'+'** icon from the left sidebar. Select **Import**, then copy the contents of **grafana_dashboard.json** and load.
  - Now you can access the dashboard we just created from the Home Screen.
![image](https://user-images.githubusercontent.com/4581090/161802245-144b1993-0e2b-4d13-b032-36726546fa48.png)

## Improvements
- Implement a caching mechanism for example using redis or memcached.
- For production environment use a alternative WSGI server like Gunicorn running behind Nginx Proxy.
  - This would also features like rate-limiting with burst possibility, rolling-restart etc.
 - Implement Logging for the python modules.
 - Make a scalable deployment for example using kubernetes.
