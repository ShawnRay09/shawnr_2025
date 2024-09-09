---
layout: page 
title: Pictures of my Dog
search_exclude: true
permalink: /PicturesofmyDog/
---
<img src="{{site.baseurl}}/images/IMG_0201.JPEG" alt="DI1" width="325" height="auto"> <img src="{{site.baseurl}}/images/IMG_3296.PNG" alt="DI2" width="225" height="auto">
<img src="{{site.baseurl}}/images/IMG_5724.JPG" alt="DI3" width="25%" height="auto">
<img src="{{site.baseurl}}/images/IMG_5626.JPG" alt="DI4" width="25%" height="auto"> <img src="{{site.baseurl}}/images/IMG_4385.JPG" alt="DI5" width="40%" height="auto"> <img src="{{site.baseurl}}/images/IMG_4090.JPG" alt="DI6" width="30%" height="auto"> <img src="{{site.baseurl}}/images/IMG_9831.thumbnail.jpg" alt="DI3" width="40%" height="auto">


<h1>Click Here to Learn a Random Fact About my Dog!</h1>

<button onclick="showRandomFact()">Click here!</button>

<p id="fact"></p>

<script>
    // Array of random dog facts
    const dogFacts = [
        "My dog's name is Teddy Ray",
        "My dog is 11 years old",
        "He is a maltipoo, which is a maltese and poodle mix",
        "He loves to go on walks and sleep in his bed",
        "He loves to eat and is always asking for food",
        "He is 8 pounds",
        "He barks a lot at other dogs",
        "He is old and unfortunately barely knows any tricks",
        "We adopted him 5 years ago",
        "He is very lazy at at times and loves to be pet"
    ];

    // Function to show a random fact
    function showRandomFact() {
        const randomIndex = Math.floor(Math.random() * dogFacts.length);
        const randomFact = dogFacts[randomIndex];
        document.getElementById('fact').textContent = randomFact;
    }
    </script>
