---
layout: post
title: Simulation and Games HW
description: 
type: issues
comments: True
---

```python
import random

def roll_dice():
    return random.randint(1, 6)

# Test it out
print("Dice roll:", roll_dice())

```

    Dice roll: 3



```python
import random

def biased_color():
    colors = ['Red'] * 50 + ['Blue'] * 30 + ['Green', 'Yellow', 'Purple', 'Orange', 'Pink', 'Black', 'White', 'Gray', 'Cyan'] * 2
    # The total list now has 50 + 30 + (10 * 2) = 100 entries, matching the 50%, 30%, and 20% distribution
    for _ in range(10):
        print(random.choice(colors))

biased_color()

```

    Red
    Red
    Red
    Gray
    Red
    Red
    Red
    Red
    Red
    Red



```python
import random

def coin_flip_game():
    player1_heads = 0
    player2_heads = 0
    rounds = 0

    while player1_heads < 3 and player2_heads < 3:
        rounds += 1
        flip1 = random.choice(['heads', 'tails'])
        flip2 = random.choice(['heads', 'tails'])

        if flip1 == 'heads':
            player1_heads += 1
        if flip2 == 'heads':
            player2_heads += 1

        print(f"Round {rounds}: Player 1 - {flip1}, Player 2 - {flip2}")
        print(f"Score: Player 1 = {player1_heads}, Player 2 = {player2_heads}\n")

    if player1_heads == 3:
        winner = "Player 1"
    else:
        winner = "Player 2"

    print(f"{winner} wins after {rounds} rounds!")

coin_flip_game()

```

    Round 1: Player 1 - heads, Player 2 - heads
    Score: Player 1 = 1, Player 2 = 1
    
    Round 2: Player 1 - heads, Player 2 - heads
    Score: Player 1 = 2, Player 2 = 2
    
    Round 3: Player 1 - tails, Player 2 - tails
    Score: Player 1 = 2, Player 2 = 2
    
    Round 4: Player 1 - tails, Player 2 - heads
    Score: Player 1 = 2, Player 2 = 3
    
    Player 2 wins after 4 rounds!



```python

```
