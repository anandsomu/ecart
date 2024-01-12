Python Django Application.

Following APIs are part of this:
* User Signup/Login
* Get Items
* Get Total Price of the selected Items


<br>

Requirements:-
* Python 3.9
* Django 3.2
* Django Rest Framework 3.12.4
* Postgresql 13

Steps to set up on local without docker:-
1. Set up postgres database.
   <details>
   <summary>You could use some help...</summary>
   <pre>
   sudo -u postgres psql
   create database <em>database_name</em>;
   create user <em>username</em> with encrypted password '<em>password</em>';
   grant all privileges on database <em>database_name</em> to <em>username</em>;
   </pre>
   </details>
4. Copy the file `sample.env` with new file name `.env` and update the variable accordingly.
5. Run `make start` to start the server.

To create default superuser run `make superuser`, credentials will be printed on console.

<br>
Api documentation is present with OpenAPI specs. Serve swagger ui with OpenAPI specs in docker:-

`docker run -p 80:8080 -e SWAGGER_JSON=/schema.yml -v ${PWD}/openapi/ws-openapi-spec.yaml:/schema.yml swaggerapi/swagger-ui
`

<br/>

Steps to set up on local with docker:-
1. Copy the file `sample.doc.env` with new file name `.doc.env` and update the variable according.
2. Run `make docker` to start server.

To create default superuser run `make docker-superuser`, credentials will be printed on console.

For running django shell plus use `make docker-shell` to start shell.

The Frontend is a ReactJs Application.

For limited time, the application is hosted on DigitalOcean Droplets.
Take it for a spin, visit the url: http://147.182.225.162

ScreenShots:

![Login](./screens/login.png)
<br>

![Signup](./screens/signup.png)
<br>

![Signup](./screens/signup-2.png)
<br>

![Login](./screens/login-2.png)
<br>

![Item List](./screens/item_list.png)
<br>

![Selected Item List](./screens/selected_item_list.png)
<br>

![Item Total Summary](./screens/item_total_summary.png)



