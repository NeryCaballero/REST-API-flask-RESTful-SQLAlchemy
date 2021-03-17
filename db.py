from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()





# SQLAlchemy() is going to link to our flask app.
# And it's going to look at all of the objects that we tell it to.
# And then it's going to allow us to map those objects to rows in a database.



# For example:

# When we create an item model object that has a column called name and a column called price,

# it's going to allow us to very easily put that object into our database.

# It will save the indicated object's properties into the database.

# And that's what SQLAlchemy excels at which makes things really easy.
