---
layout: post
title: MCQ Corrections
description: Corrections for 2018 MCQ
type: issues
comments: True
---
# Question Corrections

## Question 14

<img src="{{site.baseurl}}/images/question14.png" width="900" alt="question14">

Initial Thoughts: I thought that these two codes both displayed a different number of values each. I thought the first code had 1-10, whilst the second code had 2-10, which caused me to believe that they displayed different numbers of values each, but this was simply wrong. 

Corrections: Though both codes did start at different values, the first one starting at 1, and the second one starting at 2, they both have the same number of values. The first one starts at 1 and ends at 10, whilst the second one starts at 2 and ends at 11. This is the same number of numbers displayed, but just different numbers. This is why C is the correct answer

## Question 30

<img src="{{site.baseurl}}/images/question30.png" width="900" alt="question30">

Initial Thoughts: After reading the exact quote from the question "The Analysis procedure takes approximately 1 hour to return a result, regardless of the number of videos of the given genre. All other operations happen nearly instantaneously." This caused me to believe that this would take exactly 1 hour and it was kind of a trick question. This was a careless mistake and could have been fixed from just reading the question more thoroughly.

Corrections: This approximation for 1 hour is only accurate when the analysis is called once, however it is called multiple times. To be more exact, it is called 5 times, once for the "science fiction", and 4 others for the other genres (comedy, drama, mystery, and romance). Because it was called 5 times rather than just once, we have to account for the 1 hour for each time it is called, so since it was called 5 times, it will have an approximate time of 5 hours. This is why D is the correct answer.

## Question 39

<img src="{{site.baseurl}}/images/question39.png" width="900" alt="question39">

Initial Thoughts: I assumed that open standards and protocols were more connected with the back-end and coding work reguarding that certain internet communication. Because of this I thought that this would affect some things like how fast the back-end and front-end talked with each other, and certain aspects of the connection between back-end and front-end like that.

Corrections: Knowing that this question is asking in the context of a more general and front-end view, open standards allow developers to connect their devices and work, and open protocols help with them to share solutions without any conflictions or errors. This is why A is the correct answer as it helps them build and develop new software because of the benefits of communication.

## Question 42

<img src="{{site.baseurl}}/images/question42.png" width="900" alt="question42">

Initial Thoughts: I was not familiar with Internet protocol versions, how each differ, and what they exactly do so I just unfortunately guessed on this one. My logic was that 128-bit compared to 32-bit is a 4 times difference. This caused me to believe that A was the correct answer but it is way different than I thought

Corrections: After doing some research, I learned that IPv4 has about 4.3 billion different unique addresses, whilst IPv6 uses way more variables and values which makes the number of different and unique addresses to be astronomically huge. This means that the only answer that makes sense is 2^96 because every other value can be easily calculated from just simply multiplying 4.3 billion by them, but 2^96 times 4.3 billion is an extremely huge number. This means that the answer is D.

## Question 43

<img src="{{site.baseurl}}/images/question43.png" width="900" alt="question43">

Initial Thoughts: My mind first went towards the fact that there are so many steps. Because there are so many steps when running this code for a certain amount of items, I assumed that it would take a long time to run and for all these steps to be completed. However I was completely wrong in thinking this because I learned now that it is all about the patterns.

Corrections: This shows a polynomial pattern. To be more exact, after adding the next 10 items, the number of steps increases by 300, then 500, then 700, then 900, and so on and so forth. This pattern shows that the program runs within a reasonable time, and obviously the program runs and works if this is successfully displaying. So, from all of this logic, we can deduce that the answer is A.

## Question 48

<img src="{{site.baseurl}}/images/question48.png" width="900" alt="question48">

Initial Thoughts: I thought that 25% of the answers were supposed to be successful, and 75% were supposed to be unsuccessful. Simple mishap on my end and could be fixed easily by reading the question.

Corrections: Since the first if statement counts the correct/successful attemps, we must make 75% of the numbers in the code output successful attempts. So, when generating a random number between 1 and 100, we need 75 of them to work, so less than or equal to 75 is 75 numbers that are successful when generated by the code. So the answer must be D.

## Question 50

<img src="{{site.baseurl}}/images/question50.png" width="900" alt="question50">

Initial Thoughts: I did not exactly know the exact definitions of both a linear and binary search, so I was forced to guess on these. I also knew it was not III because it is checking each element, so it doesn't matter if the list is sorted or not.

Corrections: 
Binary Search: Divides the storted list in half repeatedly to find the target item, this helps when the target item is near the middle.

Linear Search: Goes through each element one by one starting from the beginning to find the target item, this helps when the target item is near the front or is the first element in the list.

So, this code undergoes a linear search because it searches through each element for the target element in list using a for loop. Therefore, the correct answer is B

## Question 52

<img src="{{site.baseurl}}/images/question52.png" width="900" alt="question52">

Initial Thoughts: I knew that the most likely order was the exact order that the question referred to, but I didn't realize that multiple ways of that same order would have the same output. This was a careless mistake and could have been fixed by just reading the questions and answers in more depth.

Corrections: I knew II was correct because it matches the question's explanation, but III is also correct because alphabetically sorting the list, then keeping the palindromes, then outputting the first letter of those palindromes gives the exact same output as the II. Therefore, the answer to this question is B

## Question 54

<img src="{{site.baseurl}}/images/question54.png" width="900" alt="question54">

Initial Thoughts: I thought the question was asking what could also be added to the list, but it was not asking that. This is why I chose n^4 because it matches the pattern of the procedures listed above, but the question was not asking that. The question was simply asking for that pattern, and this could have been fixed if I wasn't so careless and read the question further.

Corrections: n^m is the answer because it generalizes the pattern and actually answers the question that they asked. Therefore, the answer is D.

## Question 55

<img src="{{site.baseurl}}/images/question55.png" width="900" alt="question55">

Initial Thoughts: After reading the procedure, I thought that expression [response = "y" AND response = "yes"] was an OR gate instead of an AND gate. This was a careless mistake and simply again could have been avoided by reading the question with more care.

Corrections: Since the response can never be y and yes, the expression will always be false because the condition says to print a true statement when the AND gate condition has been fufilled. Since it can never be fufilled, that means that the code will always have an output of false. Therefore, D is the answer.

## Question 57

<img src="{{site.baseurl}}/images/question57.png" width="900" alt="question57">

Initial Thoughts: First off, I noticed that this was about strings and string manipulation. I know that you can convey different messages through strings by replacing the certain letters of certain words. In this case, I didn't really understand what the numbers in the procedure meant, so I assumed that it was the start and end letters, but I was wrong.

Corrections: Now I realize that the first number represents the letter that you start with, and the second number represents the number of letters that you take from that word to form the new word. In that case, to spell happy, you need the "ha" from harp, so start at the 1st letter and take two letters. This means that the procedure would require 1, 2 as the numbers because we need to start at 1, and take 2 letters. Then for puppy, same thing, we start at the 3rd letter, and end at y, so 3, 3. This means that B is the correct answer.

## Question 64

<img src="{{site.baseurl}}/images/question64.png" width="900" alt="question64">

Initial Thoughts: I wasn't familiar with what cloud computing is, but I know it is important for communication within the internet. I knew that was one of the answers, but I didn't know the other one, so I assumed it was something that helped with redundancy and speed. However this was wrong and after doing some researching this is what I came up with.

Corrections: Cloud computing is the delivery of cloud services over the internet or web. This directly relates with communication over the internet which matches one of my answers, but also it allows users to access their own storage, networking, software, and more. This brings up security concerns as each user has their own database/login so other users are able to hack into those databases and steal their information. This means that the answer is B and C.

# Questions Marked for Review / Interesting Questions

## Question 23

<img src="{{site.baseurl}}/images/question23.png" width="900" alt="question23">

Explaination: I thought this was interesting because I have not seen anything like this before. Initially I was very confused on the topic and was confused what this even meant. After realizing this was simply a representation of the connection of certain networks, I got the answer that was B because there is only 1 physical route from P to S, unlike the others. I thought this was a really creative and cool question.

## Question 26

<img src="{{site.baseurl}}/images/question26.png" width="900" alt="question26">

Explaination: I also thought this was a cool and interesting problem because I really liked how we had to visually think about the code and what it will physically do to the robot. I liked how we had to go through each line and think, "what will this do", "after that, what will this do?" I liked the visual aspect about this problem and I also thoughth the solution was pretty cool. The solution is correct because I noticed that the robot will only take right turns to the finish square without any left turns. This makes A correct because the robot will keep going straight unless a right turn was available, then it will turn right. This solution would be incorrect if there was any right turns that were not needed.

## Question 34

<img src="{{site.baseurl}}/images/question34.png" width="900" alt="question34">

Explaination: I really liked this question because at first I was very confused. I marked this question for review because at first I didn't really understand the code and had to look through line by line learning what each line did and how it affects the output and input. I finally realized that the "numPredators" is not changed at all unlike the "numMice" which allowed me to deduce that this code assumes that the number of predators does not change, whilst the number of mice is directly affected from the number of predators. This helped me deduce that the answer is D.

# Overall

<img src="{{site.baseurl}}/images/score.png" width="1300" alt="score">

Overall, I am very proud of my score of 54/66 because I thought that coming into this MCQ I would be lost and not know many of the problems. In reality, after 3 sprints of coding and learning new functions of code, this paid off as many of the coding based questions were very easy and I zoomed by them. On the other hand, this MCQ allowed me to realize that I need to study more background and knowledge of coding. For example, certain aspects of the internet and what they do. How the internet works and what parts are required. How does it help coders and people in general. These things about coding and background knowledge will help me excel as a coder and elevate my coding abilities.