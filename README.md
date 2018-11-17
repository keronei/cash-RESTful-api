# BASIC INFO
This app in built on Flask, the dependencies have been put in place by employing `pipenv`

## Getting Started

You may need python3 in order to access some of the end points, therefore it is recommended to completely employ 3.+

In order to get things working, you may need to install the dependencies by running the following(the dependencies are in the pipfile.lock, worry less).

```
pipenv install
```

once all is well, you will need to give the permission to excecute the `bootstrap.sh` file as that is what forms the launching base.

```chmod +x bootstrap.sh```

here, you might need to use `sudo` aka superuser do.


## Usage
In order to use the endpoints, run the following:
```
yourhost:5000/incomes

```
or
```
yourhost:5000/expenses
```
In order to manipulate the data via `POST` method:

```
# post new values
curl -X POST -H "Content-Type: application/json" -d '{
"amount": 2000,
"description": "something expensive :)"
}' http://yourhost:5000/expenses
```

same for income:
```
# post new values
curl -X POST -H "Content-Type: application/json" -d '{
"amount": 1000,
"description": "Medical allowances"
}' http://yourhost:5000/incomes
```

Using curl from the terminal is the recommended way but if you feel you need something more interactive the try [Postman](https://www.getpostman.com/apps) ,

![Postman Screenshot](https://github.com/keronei/cash-RESTful-api/blob/master/screenshot.png)

This gives your the same interaction.

## Finally

This is a simple REST API, much can still be done to enhance its functionality e.g adding database usage.

credits to [auth0](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/) for original guide. Find detailed explanation on their platfom.


