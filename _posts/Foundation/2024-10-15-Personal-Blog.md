---
layout: post
title: Shawn Ray's Sprint 2 Personal Blog
description: Personal Blog about Sprint 2
type: issues
comments: True
---
## What I Taught


```python

```

We taught lesson 3.8 which was iterations
1. Loops
    -For Loops
    -While Loops
    -Do-While Loops
    -Infinite Loops
2. Nested-If Statements
3. Try/Except
4. Dictionaries

## What I learned


```python

```





<table border="1" style="border-collapse: collapse; width: 70%;">
    <tr>
        <th>Lesson</th>
        <th>Thing Learned 1</th>
        <th>Thing Learned 2</th>
    </tr>

    <tr>
        <td><a href="https://nighthawkcoders.github.io/portfolio_2025/csp/big-idea/p1/3-1-1" target="_blank">Lesson 3.1</a></td>
        <td contenteditable="true">Introduction to Python syntax and basic data types</td>
        <td contenteditable="true">How to use variables and print statements</td>
    </tr>

    <tr>
        <td><a href="https://nighthawkcoders.github.io/portfolio_2025/csp/big-idea/home" target="_blank">Lesson 3.2</a></td>
        <td contenteditable="true">Understanding conditionals and if-else statements</td>
        <td contenteditable="true">Logical operators and their role in decision-making</td>
    </tr>

    <tr>
        <td><a href="https://nighthawkcoders.github.io/portfolio_2025/csp/big-idea/3-3/p1" target="_blank">Lesson 3.3</a></td>
        <td contenteditable="true">Introduction to loops, focusing on for loops</td>
        <td contenteditable="true">How loops help automate repetitive tasks</td>
    </tr>

    <tr>
        <td><a href="https://nighthawkcoders.github.io/portfolio_2025/csp/big-idea/p1/3-4" target="_blank">Lesson 3.4</a></td>
        <td contenteditable="true">Working with while loops and conditions</td>
        <td contenteditable="true">Difference between for and while loops</td>
    </tr>

    <tr>
        <td><a href="https://nighthawkcoders.github.io/portfolio_2025/csp/big-idea/3-5/p1" target="_blank">Lesson 3.5</a></td>
        <td contenteditable="true">Introduction to functions and defining reusable code</td>
        <td contenteditable="true">How to pass arguments to functions</td>
    </tr>

    <tr>
        <td><a href="https://nighthawkcoders.github.io/portfolio_2025/csp/big-idea/3-6/p1" target="_blank">Lesson 3.6</a></td>
        <td contenteditable="true">Understanding return values in functions</td>
        <td contenteditable="true">Best practices for function naming and modularity</td>
    </tr>

    <tr>
        <td><a href="https://nighthawkcoders.github.io/portfolio_2025/csp/big-idea/3-7/p1" target="_blank">Lesson 3.7</a></td>
        <td contenteditable="true">Introduction to lists and how to manipulate them</td>
        <td contenteditable="true">Basic list methods like append, remove, and sort</td>
    </tr>

    <tr>
        <td><a href="https://nighthawkcoders.github.io/portfolio_2025/csp/big-idea/3-8/p1" target="_blank">Lesson 3.8</a></td>
        <td contenteditable="true">Working with dictionaries and key-value pairs</td>
        <td contenteditable="true">How to iterate through a dictionary using loops</td>
    </tr>

    <tr>
        <td><a href="https://nighthawkcoders.github.io/portfolio_2025/csp/big-idea/p1/3-10" target="_blank">Lesson 3.10</a></td>
        <td contenteditable="true">Introduction to error handling with try-except blocks</td>
        <td contenteditable="true">How to debug common errors in Python code</td>
    </tr>
    </table>



## Extra Summary of what I learned

Throughout our teaching we learned:
- Simplify complex concepts then work back to complex. Ex. Popcorn hacks were simple to an extent, but homework hacks combined them all.
- Every student learns differently, adapt presentation to all. Ex. Popcorn hacks, pictures, examples.
- Answering questions for students in a way that makes sense
- Prepare ourselves for the lesson. Ex. Practicing explaining, think about possible questions that could be asked.

Throughout our process of creating the lesson, we learned:
- Dive deep into Iterations. Since we are teaching this lesson, we need to know everything about it, so the lessons and videos on college board were not going to cut it. We needed to do outside research and research any questions we had.
- Embracing Mistakes. We made many, many mistakes especially because this was a sort of self-taught lesson. Mr. Mort closed many of our pull requests and we even made the mistake of not testing things locally for one of our pull requests. However, we learned from these and never made these mistakes again, and for the future, we will never make these mistakes again.
- Time Management. We made sure to plan and manage our time with a schedule of what each person would do and when.
- Team Work. Speaking of a schedule, this helped us with teamwork where we could plan what each person would do according to everyones schedule.

## Redone Popcorn Hacks


```python
#Challenge Homework Hack for 3.3 Mathematical Expressions. (Did not do challenge hack, attempting it)

import math

def fibonacci(n):
    """Return the nth term in the Fibonacci sequence."""
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def calculate_area():
    """Calculate the area of a circle, square, or rectangle."""
    shape = input("Enter the shape (circle, square, rectangle): ").lower()
    
    if shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * (radius ** 2)
        print(f"The area of the circle is: {area:.2f}")
        
    elif shape == "square":
        side = float(input("Enter the side length of the square: "))
        area = side ** 2
        print(f"The area of the square is: {area:.2f}")
        
    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"The area of the rectangle is: {area:.2f}")
        
    else:
        print("Invalid shape. Please enter circle, square, or rectangle.")

def calculate_volume():
    """Calculate the volume of a rectangular prism, sphere, or pyramid."""
    solid = input("Enter the solid (rectangular prism, sphere, pyramid): ").lower()
    
    if solid == "rectangular prism":
        base = float(input("Enter the base length of the rectangular prism: "))
        width = float(input("Enter the width of the rectangular prism: "))
        height = float(input("Enter the height of the rectangular prism: "))
        volume = base * width * height
        print(f"The volume of the rectangular prism is: {volume:.2f}")
        
    elif solid == "sphere":
        radius = float(input("Enter the radius of the sphere: "))
        volume = (4/3) * math.pi * (radius ** 3)
        print(f"The volume of the sphere is: {volume:.2f}")
        
    elif solid == "pyramid":
        base = float(input("Enter the base length of the pyramid: "))
        width = float(input("Enter the width of the pyramid: "))
        height = float(input("Enter the height of the pyramid: "))
        volume = (1/3) * base * width * height
        print(f"The volume of the pyramid is: {volume:.2f}")
        
    else:
        print("Invalid solid. Please enter rectangular prism, sphere, or pyramid.")


if __name__ == "__main__":
    
    term = int(input("Enter the Fibonacci term to calculate (0 for the first term): "))
    print(f"The {term}th term in the Fibonacci sequence is: {fibonacci(term)}")

    
    calculate_area()

    
    calculate_volume()

```

    Enter the Fibonacci term to calculate (0 for the first term): 5
    The 5th term in the Fibonacci sequence is: 5
    Enter the shape (circle, square, rectangle): circle
    Enter the radius of the circle: 10
    The area of the circle is: 314.16
    Enter the solid (rectangular prism, sphere, pyramid): pyramid
    Enter the base length of the pyramid: 8
    Enter the width of the pyramid: 3
    Enter the height of the pyramid: 10
    The volume of the pyramid is: 80.00



```python
#3.5 Booleans Homework Hack Rework

def truth_table():
    print("A\tB\tA AND B\tA OR B\tNOT A\tNOT B\t¬(A AND B)\t¬A OR ¬B\t¬(A OR B)\t¬A AND ¬B")
    print("-" * 85)
    
    for A in [True, False]:
        for B in [True, False]:
            
            A_and_B = A and B
            A_or_B = A or B
            not_A = not A
            not_B = not B
            not_A_and_B = not (A and B)  
            not_A_or_not_B = not_A or not_B  
            not_A_or_B = not (A or B)  
            not_A_and_not_B = not_A and not_B  
            
            
            print(f"{A}\t{B}\t{A_and_B}\t\t{A_or_B}\t{not_A}\t{not_B}\t{not_A_and_B}\t\t{not_A_or_not_B}\t{not_A_or_B}\t\t{not_A_and_not_B}")


truth_table()

```

    A	B	A AND B	A OR B	NOT A	NOT B	¬(A AND B)	¬A OR ¬B	¬(A OR B)	¬A AND ¬B
    -------------------------------------------------------------------------------------
    True	True	True		True	False	False	False		False	False		False
    True	False	False		True	False	True	True		True	False		False
    False	True	False		True	True	False	True		True	False		False
    False	False	False		False	True	True	True		True	True		True

