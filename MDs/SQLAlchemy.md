# SQLAlchemy()

1. create a new file : db.py
    - import :
   ```python 
      from flask_sqlalchemy import SQLAlchemy 
   ```
   - Declare `db = SQLAlchemy()`
     SQLAlchemy() is going to link to our flask app.    
     And it's going to look at all of the objects that we tell it to. 
     And then it's going to allow us to map those objects to rows in a database.



For example, it will allow us to do something like:
when we create an item model object that has a column called name and a column called price,
it's going to allow us to very easily put that object into our database.
All that is is saving the object's properties into the database.
And that's what SQLAlchemy excels at and it makes things really easy.
It sounds like something not very useful but you'll see how simpler it makes our code.



- On app.py import `from dbimport db`
- init the app
```python
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)

```

- on the models: import `from dbimport db`
- Make each Model extend db.model:
```python
class UserModel(db.Model):
```
```python
class ItemModel(db.Model):
```
What that's going do is it's going to tell the SQLAlchemy entity that these classes,
are Models that we are going to be saving to a database and retrieving from a database.
So it's going to create a mapping between the database and these objects.


- The next thing we have to do is tell SQLAlchemy the table name where these models are going to be stored, as well as the columns.

```python
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
```

The `properties names`, ( self.id, self.username, self.password ) must match the `columns names` for them to be saved to the database.

We can have other properties and this property won't be saved to the database.

And it also won't give us an error.

It will exist in the object but it won't be in any way related to the database.

It won't be stored,

it won't be read from the database.


- on app.py: specify a configuration property
```python
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

We declare this to turn off the flask SQLAlchemy modification tracker.

It does not turn off the SQLAlchemy modification tracker.

So this is only changing the extensions behaviours

and not the underlying SQLAlchemy behaviour.

<hr>
And that's everything.

All that we've done now is we have told our app

that we have two models that are coming from

tables in our database.

The users table and the items table.

And we've told SQLAlchemy how it can read these items

by just looking at the columns.

And when it does look at the columns,

it's going to see the name and the price

and it's going to pump them in straight to the init method

and it's going to be able to create an object

for each row in our database.

The id method will also be passed in

but because there's no id parameter here it won't be used.

Okay, and that's it really.
 <hr>

# Querying.

ItemModel:

`SQLAlchemy` provides us with `db.Model` which we use to pass properties to our classes, in this case `ItemModel`. 

`.query` which is provided by `db.Model`,  is a query builder.
Check [common filter operators](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#common-filter-operators).

BEFORE: *using sqlite3*.
```python
@classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
```





AFTER: *using SQLAlchemy*.
```python
class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
```



`cls.query` says we want to query the Model and SQLAlchemy knows we're going to be building a query on the database.

Then we say `.filter_by(name=name).first()` 

Which is the same as saying `SELECT * FROM items WHERE name=name LIMIT 1`

`SQLAlchemy` gets the data, without us having to do any of the connecting, 
cursoring, iterating over rows, etcetera.

This data also gets converted to an item `model object`.

So what this is returning is an ItemModel object that has `self.name` and `self.price`.

<hr>

In the app.py we have to now tell SQLAlchemy

where to find the data.db file.

So, we're gonna tell it just that at app.config

SQLALCHEMY_DATABASE_URI is gonna be the following

and this is important, sqllite3:///data.db.

Okay, so what we are saying is that the SQLAlchemy database

is gonna live at the root folder of our project.

<hr>