---
layout: post
title: Sprint 3 Summary
description: Shawn Ray's Journey through Sprint 3
type: issues
comments: True
---
# Introduction / Project Overview

Sprint 3 asked us to plan, design, code, and finally create a fully interactive social media platform for others to chat and interact with. For Mr. Brown's period 1 class, our theme was "Shared Interests" in which we decided to do the subtheme of school subjects. The website had to include front-end work which is the styling, and overall look of the pages and site, whilst the back-end work was the work that actually contained the data and content that was stored. We built a page where people are able to talk about certain school subjects and other topics with other people and also other aspects like a fully functional school timer with a resources tab. The main challenge was successfully connecting our back-end to our front-end whilst maintaining our fully functional website with other people working on it at the same time.

[Jupyter](https://shawnray09.github.io/flocker_frontend/shared_interests/jupyter/home/)

# Background 
The backend has a database that stores all of the data and the python based backend interacts with the database in order to use the data to send or manipulate the data to send it to the frontend. This happens with the data is called from the frontend and in our case, it is when we click "show posts". Additionally, when we pick a group and channel and send the message from the frontend to the backend, the backend stores that data in a database.

<img src="{{site.baseurl}}/images/visual.png" width="500" alt="visual">


# Team Contributions

| Role          | Name       |
|---------------|------------|
| Scrum Master  | [Shawn Ray]|
| Frontend      | [Shawn Ray, Aarav Sonara]|
| Backend       | [Arya Savlani]|
| Integrator    | [Shawn Ray]|


As shown above, I worked on the frontend work with my friend Aarav and was responsible for most of the styling, creativity, and overall front-end work. We decided to go for a purple and black color scheme because it matched well with "Jupyter" to us. My job was to setup the look of the website and create the whole structure for my back-end worker, Arya who finished the back-end work. I also had to create a pleasant experience for users on the site and make the site have a visually appealing look to it.

<img src="{{site.baseurl}}/images/chatroom.png" width="500" alt="chatroom">

# Planning
Making an issue and communicating with our other groups in our class helped us plan and design this whole project

<img src="{{site.baseurl}}/images/issue.png" width="800" alt="issue">

# Key Features

### 1. Chatroom
The chatroom was created in order to allow students to have the ability to create posts and chat with each other on certain school subjects, whether it is for help or simply because they are interested in that subject and want to talk about it. We used a system that sent the data from the user to the back-end where it was stored, and the user could pull that data any time to be able to observe what was being said, and what they can respond with


<img src="{{site.baseurl}}/images/jupyter_chatroom.png" width="500" alt="chatroom">



### 2. Timer
A timer was used in order to show students when school started and when it ends. It works by setting a 25800 timer acting as each second of the day. It is activated at 8:35, and each hour updates the timer where it will slowly say "6 hours left", then "5 hours left", and so on. Finally when the time reaches 3:45, it displays, "School is over!". There is also a circle around which fills up as the day goes by to add some creativity and make the website more visually pleasing.


<img src="{{site.baseurl}}/images/jupyter_timer.png" width="500" alt="timer">



### 3. Resources
Simple resources were provided like links, calculators, dictionaries. These are done to provide students with some support and easy access to these things. This is the easiest and probably most uneventful part of our website.


<img src="{{site.baseurl}}/images/jupyter_resources.png" width="500" alt="resources">


# What we learned

| Topic          | How it affects our coding       |
|---------------|------------|
| Postman API  | Connecting our backend to frontend allows us to create and use applications like our social media platform in order to help us communicate thoughts, ideas, and more. Additionally, connecting our backend to our frontend allows us to be able to store data that can then be recalled to display for others to see.|
| Planning      | Creating issues, canva drawings, and overall communication was essential in this project. These simple rough drafts helped us develop and enhance the final product of our social media platform. Additionally, communication with the class and teachers were essential as well because it allowed us to integrate all of our ideas in a creative and fun way.|
| Teamwork       | Speaking of communication, that plays a big part in teamwork. Working with not only our teammates but also classmates helped us organize and plan this whole project more thoroughly to ensure that things run smoother without many problems. Because all of us had a plan and communicated with each other as well as to our scrum master of scrum masters and our integrator of integrators, we were all able to integrate our platforms and creative thinking into the same website.|
| Presenting, Sharing Ideas, and Recieving Feedback    | Showing other people our social media platforms and asking for feedback helped us decide what needed to be tweaked and fixed about our website, as well as what we should add.|

# Improvements
-Next time I think adding some more individuality between each person would have been a lot better for the users. For example, a prompt could ask what class each user has each period, and the timer is individually set to show that certain class and when that certain class starts and ends rather than just a simple school timer. Additionally, it could give you those certain resources for even more quick and easy access for students to use.

-Simply more chats could have been added to increase the amount of people that would be interested in this site and using this site in general. More subjects and chats would help students by providing them more resources and places to talk in for help or entertainment.

# Overall
Looking back, I’m really proud of how the social media page turned out. It’s a feature that not only showcases our coding skills but also offers users a fun and engaging experience. Personally, I’ve gained a better understanding of how to approach both frontend design and backend logic, and I’ve learned how crucial teamwork is in bringing a project together. Overall, a great experience with a lot of learning and work put into it.
