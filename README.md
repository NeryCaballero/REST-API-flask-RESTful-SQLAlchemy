# Flask RESTful API SQLAlchemy

This project is a continuation of my previous [REST API](https://github.com/NeryCaballero/REST-API-flask-RESTful-SQLite3) created with Python `flask` , `flask_restful` , `flask_jwt` and `sqlite3`.

This time I have used `SQLAlchemy`.

This API has 4 resources: `Item`, `Items`, `Store` and `Stores`. 

`authentication` has been applied with `flask_jwt`.

##  

This API is deployed on Heroku. URL = `https://nery-flask-restful-sqlalchemy.herokuapp.com`.

Note: no front-end is built. Use Postman to register and authenticate.

The API's information is stored in `heroku-postgresql`.


## The available endpoints are:

- POST `/register`: Registers a new user. 
  Information required in JSON: 

  ```json
  { 
    "username": str, 
    "password": str 
  }
  ```

## 
  
- POST `/auth` : Authenticates existing user. Provides an `access token`. 
  This token must be included on the headers of all the following requests. `Authorization = JWT <token>`
  
  Information required in JSON:
  
  ```json
  { 
    "username": str, 
    "password": str 
  }
  ```
  
  For more details on authentication go [here](https://github.com/NeryCaballero/REST-API-flask-RESTful/blob/main/flask_jwt.md), *all the way to the end*.

## 

- POST `/item/<item-name>` : Creates new item by passing the name on the URL.
  
  Information required in JSON: 

  ```json
  { 
    "price": float,
    "store_id: : int
  }
  ```  

## 

- GET `/item/<item-name>` : Reads one item by passing the name on the URL.

## 

- GET `/items`  : Reads all items.

## 

- PUT `/item/<item-name>` : Updates one item by passing the name on the URL. If the item does not exists, it will be created. 
  
  Information required in JSON:
  
  ```json
  { 
    "price": float,
    "store_id: : int
  }
  ```

## 

- DEL `/item/<item-name>` : Deletes one item by passing the name on the URL. 

##  

- POST `/store/<store-name>` : Creates new store by passing the name on the URL.

## 

- GET `/store/<store-name>` : Reads one store by passing the name on the URL.

## 

- GET `/stores`  : Reads all stores.

## 

- DEL `/store/<store-name>` : Deletes one store by passing the name on the URL. 
