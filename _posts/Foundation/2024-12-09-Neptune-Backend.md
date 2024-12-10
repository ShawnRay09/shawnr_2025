---
layout: post
title: Neptune Backend
description: Work for Neptune's Backend
type: issues
comments: True
---

# Shawn.py Postman API Testing

I created a Shawn.py file to do testing and inputted this code into the file. Essentially, what this code does is setup the api/shawn as an endpoint that handles get and post requests. 

<img src="{{site.baseurl}}/images/shawnpy.png" width="700" alt="shawnpy">

<img src="{{site.baseurl}}/images/postzoom.png" width="500" alt="postzoom">

This part handles the post part and accepts the incoming JSON data and adds it to the stored data. It then sends back a confirmation message letting the user know that that data has been successfully stored, "Data Recieved". If that data is invalid it will return an error message with a 400 status code.

<img src="{{site.baseurl}}/images/getzoom.png" width="500" alt="getzoom">

This part handles get requests and sends all of the stored data from the post requests as a JSON reponse.

## Postman POST Request Success

<img src="{{site.baseurl}}/images/postpy.png" width="700" alt="postpy">

## Postman GET Request Success
<img src="{{site.baseurl}}/images/getpy.png" width="700" alt="getpy">


# Neptune with Postman API

I put this code in our main.py file in our Neptune_backend. It sets an endpoint at api/classes and allows that endpoint to handle GET requests. Whenever
a GET request is sent to the endpoint, it will return a list full of different classes that have been defined.


<img src="{{site.baseurl}}/images/classlist.png" width="700" alt="classlist">


<img src="{{site.baseurl}}/images/postmanget.png" width="900" alt="postmanget">

# Neptune Frontend to Backend

<video width="640" height="360" controls>
  <source src="{{site.baseurl}}/images/cspfrontback.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
