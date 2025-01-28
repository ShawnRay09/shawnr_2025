---
layout: post
title: CRUD Functions
description: Explaination of CRUD Functions
type: issues
comments: True
---

# Neptune
Welcome to **Neptune**, the ultimate online platform for students! At Neptune, students can collaborate, share ideas, and utilize a suite of powerful tools to boost their productivity and excel in their studies.
## Features
- **Collaboration:** Connect with fellow students, work together on projects, and share resources.
- **Productivity Tools:** Make use of various tools like Gemini to enhance your efficiency and manage your time effectively.
- **Community:** Join a vibrant community of motivated students who are all striving to be their best.
Join Neptune today and become the most productive student you can be!

### My Feature

My feature is used as a schedule where students can send a list of their classes and it will store in the "classes" table.

### Intializing the Table

The "Class" Model is defined with the code below and includes three key fields or columns, "_period", "_pick", and "_user". 
 - "_period" represents the period of the certain class
 - "_pick" represents the name of the class
 - "_user" represents the id of the user that has selected that class

 ```python
class Class(db.Model):
    __tablename__ = 'classes'

    id = db.Column(db.Integer, primary_key=True)
    _period = db.Column(db.String(255), nullable=False)
    _pick = db.Column(db.String(255), nullable=False)
    _user = db.Column(db.String(255), nullable=False)
```

This code below initializes the model with the given values

 ```python
def __init__(self, period, pick, user):
    self._period = period
    self._pick = pick
    self._user = user
```
### Initialization Function

The function named "InitClasses()" is defined and will populate the table with sample data when the database is intialized

```python
def initClasses():  
    with app.app_context():
        db.create_all()

        m1 = Class(user="1", pick="AP World", period="5")
        m2 = Class(user="2", pick="AP Calculus", period="1")
        m3 = Class(user="3", pick="Biology", period="3")
        m4 = Class(user="4", pick="Physics", period="4")

        classes = [m1, m2, m3, m4]

        for message in classes:
            try:
                message.create()
            except IntegrityError:
                db.session.remove()
```
## Working Initialization and Restore Demonstration

<video width="640" height="360" controls>
  <source src="{{site.baseurl}}/images/initialization-restore.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Create Function

The code below defines a create method named "create()" that will add a new class to the table. 

```python
def create(self):
    try:
        db.session.add(self)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
```

In the the API file named classses.py, an endpoint is defined at api/classes/add that handles post, get, put, and delete requests. It validates the user's input ensuring that all 3 required fields have been filled out and then uses the defined create method to add the record to the table

```python
@staticmethod
def post():
    try:
        body = request.get_json()

        if not body or 'period' not in body or 'user' not in body or 'pick' not in body:
            return {"message": "Invalid request. All 3 categories are required."}, 400

        period = body['period']
        pick = body['pick']
        user = body['user']

        new_class = Class(period=period, pick=pick, user=user)
        new_class.create()

        return new_class.read(), 201
    except Exception as e:
        return {"message": f"Error adding class: {str(e)}"}, 500
```

### Read Function

This code below in the model file defines a read method in which the it retrieves the data for a class and returns it as a dictionary

```python
def read(self):
    return {
        'id': self.id,
        'pick': self._pick,
        'period': self._period,
        'user': self._user,
    }
```

In the API file, the code below retrieves all the data from api/class/add by calling the defined read() function for each record

```python
@staticmethod
def get():
    try:
        classes = Class.query.all()
        return [class_item.read() for class_item in classes], 200
    except Exception as e:
        return {"message": f"Error fetching classes: {str(e)}"}, 500
```

### Update Function

This code below defines the update function named "update()" that will modify the table's data. It accepts a dictionary of inputs and updates the relevant fields, then commits the changes to the table.

```python
def update(self, inputs):
    if not isinstance(inputs, dict):
        return self

    pick = inputs.get("pick", "")
    period = inputs.get("period", "")
    user = inputs.get("user", "")

    if pick:
        self._pick = pick
    if period:
        self._period = period
    if user:
        self._user = user

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return None
    return self
```

Then in the api file, this code below uses the previously defined update function to accept incoming JSON data that contains the id of the row that the user would like to change, the new data that the user would like to change it to, and finally replace the data and commit it

```python
@staticmethod
def put():
    data = request.get_json()
    if data is None:
        return {'message': 'Post data not found'}, 400

    classss = Class.query.get(data['id'])
    if classss is None:
        return {'message': 'Class not found'}, 404

    classss._pick = data["pick"]
    db.session.commit()
    return jsonify(classss.read())
```

### Delete Function

The delete functionionality is handled in the API file which uses the session.delete method which interacts with the table directly.
It is pretty straightforward as the code below essentially just a delete method to api/class/add to delete row or class based on its id

```python
@staticmethod
def delete():
    try:
        body = request.get_json()
        if not body or 'id' not in body:
            return {"message": "Invalid request. ID is required."}, 400

        class_to_delete = Class.query.get(body['id'])
        if not class_to_delete:
            return {"message": "Class not found."}, 404

        db.session.delete(class_to_delete)
        db.session.commit()

        return {"message": "Class deleted successfully."}, 200
    except Exception as e:
        return {"message": f"Error deleting class: {str(e)}"}, 500
```
## Postman requests

### Working Post

<img src="{{site.baseurl}}/images/postmanpost.png" width="900" alt="postman">

### Error

This is an error that occurs when the user only fills out 2 of the 3 required categories.

<img src="{{site.baseurl}}/images/postmanerror.png" width="900" alt="postman">

## Working CRUD Functions Demonstration

<video width="640" height="360" controls>
  <source src="{{site.baseurl}}/images/crudfunction.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>