Simple Docker Implementation - Two Services Connected from Different Container

How to Run:

1) Navigate to cards-api

  > Run: docker build -t api-service-one:0.0.1-SNAPSHOT .

2) Navigate to cards-api
  > Run: docker build -t api-service-two:0.0.1-SNAPSHOT .

3) Run the services
  > docker-compose up

4) Test the services
   > http://0.0.0.0:6088/       -> it will call the http://client-api:6089/
   > http://0.0.0.0:6088/test   -> call the same host default message (cards-api)
   > http://0.0.0.0:6089/       -> it will call the http://cards-api:6089/test
   > http://0.0.0.0:6089/test   -> call the same host default message (client-api)
