# Battery Riddle Brute Force

I watched _MindYourDecisions_ YouTube video on (Could you pass this interview? The famous batteries and flashlight logic puzzle)[https://youtu.be/Zm1PUSfUMnE].

Since there are only 70 ways to arrange four '1's and four '0's, I thought I'd just test these strategies.

## Results

``` Text
Array: [0, 0, 1, 0, 1, 1, 1, 0], Winner: Strategy1! 3, 7, 5
Array: [0, 0, 0, 1, 1, 1, 0, 1], Winner: Strategy1! 3, 7, 4
Array: [0, 1, 1, 0, 1, 0, 0, 1], Winner: Strategy3! 7, 2, 2
Array: [1, 1, 0, 0, 0, 1, 1, 0], Winner: Strategy3! 1, 1, 1
Array: [1, 0, 0, 0, 0, 1, 1, 1], Winner: Strategy1! 4, 8, 7
Array: [1, 1, 0, 0, 0, 1, 0, 1], Winner: Strategy3! 1, 1, 1
Array: [1, 0, 0, 1, 1, 0, 0, 1], Winner: Strategy3! 6, 4, 4
Array: [0, 1, 0, 1, 0, 0, 1, 1], Winner: Strategy1! 4, 6, 7
Array: [0, 0, 1, 1, 0, 1, 1, 0], Winner: Strategy1! 2, 3, 6
Array: [1, 1, 1, 0, 0, 0, 1, 0], Winner: Strategy3! 1, 1, 1
Array: [1, 0, 0, 0, 1, 1, 1, 0], Winner: Strategy1! 3, 7, 5
Array: [0, 1, 0, 0, 1, 1, 0, 1], Winner: Strategy1! 3, 7, 5
Array: [0, 1, 0, 0, 1, 1, 1, 0], Winner: Strategy1! 3, 7, 5
Array: [0, 0, 1, 1, 0, 1, 0, 1], Winner: Strategy1! 2, 3, 6
Array: [1, 0, 1, 0, 1, 0, 1, 0], Winner: Strategy3! 5, 5, 3
Array: [0, 1, 0, 1, 0, 1, 1, 0], Winner: Strategy3! 8, 6, 6
Array: [0, 0, 1, 1, 0, 0, 1, 1], Winner: Strategy1! 2, 3, 7
Array: [1, 1, 0, 1, 1, 0, 0, 0], Winner: Strategy3! 1, 1, 1
Array: [1, 0, 1, 1, 1, 0, 0, 0], Winner: Strategy1! 2, 3, 3
Array: [0, 1, 0, 0, 1, 0, 1, 1], Winner: Strategy1! 4, 8, 7
Array: [1, 0, 0, 1, 0, 1, 0, 1], Winner: Strategy2! 6, 4, 6
Array: [1, 0, 0, 0, 1, 1, 0, 1], Winner: Strategy1! 3, 7, 5
Array: [1, 0, 0, 1, 0, 1, 1, 0], Winner: Strategy2! 6, 4, 6
Array: [0, 0, 1, 0, 1, 1, 0, 1], Winner: Strategy1! 3, 7, 5
Array: [0, 0, 0, 1, 0, 1, 1, 1], Winner: Strategy1! 4, 8, 6
Array: [1, 1, 1, 1, 0, 0, 0, 0], Winner: Strategy3! 1, 1, 1
Array: [0, 1, 1, 1, 1, 0, 0, 0], Winner: Strategy3! 2, 2, 2
Array: [0, 1, 0, 1, 0, 1, 0, 1], Winner: Strategy3! 8, 6, 6
Array: [1, 1, 0, 1, 0, 0, 1, 0], Winner: Strategy3! 1, 1, 1
Array: [0, 1, 0, 1, 1, 0, 1, 0], Winner: Strategy3! 8, 6, 4
Array: [0, 0, 1, 1, 1, 1, 0, 0], Winner: Strategy1! 2, 3, 4
Array: [0, 1, 1, 0, 0, 0, 1, 1], Winner: Strategy3! 4, 2, 2
Array: [1, 0, 1, 0, 1, 0, 0, 1], Winner: Strategy3! 5, 5, 3
Array: [1, 0, 1, 1, 0, 1, 0, 0], Winner: Strategy1! 2, 3, 3
Array: [0, 0, 0, 1, 1, 1, 1, 0], Winner: Strategy1! 3, 7, 4
Array: [0, 1, 0, 1, 1, 1, 0, 0], Winner: Strategy1! 3, 6, 4
Array: [1, 1, 1, 0, 1, 0, 0, 0], Winner: Strategy3! 1, 1, 1
Array: [0, 0, 0, 0, 1, 1, 1, 1], Winner: Strategy1! 3, 7, 5
Array: [0, 1, 1, 1, 0, 0, 1, 0], Winner: Strategy3! 2, 2, 2
Array: [0, 0, 1, 1, 1, 0, 0, 1], Winner: Strategy1! 2, 3, 4
Array: [1, 1, 1, 0, 0, 0, 0, 1], Winner: Strategy3! 1, 1, 1
Array: [0, 1, 1, 0, 1, 1, 0, 0], Winner: Strategy3! 3, 2, 2
Array: [1, 0, 1, 0, 0, 0, 1, 1], Winner: Strategy3! 4, 5, 3
Array: [0, 1, 0, 0, 0, 1, 1, 1], Winner: Strategy1! 4, 8, 7
Array: [1, 1, 0, 1, 0, 0, 0, 1], Winner: Strategy3! 1, 1, 1
Array: [1, 0, 1, 1, 0, 0, 1, 0], Winner: Strategy1! 2, 3, 3
Array: [0, 1, 0, 1, 1, 0, 0, 1], Winner: Strategy3! 8, 6, 4
Array: [1, 0, 1, 0, 0, 1, 0, 1], Winner: Strategy3! 5, 5, 3
Array: [1, 1, 1, 0, 0, 1, 0, 0], Winner: Strategy3! 1, 1, 1
Array: [1, 0, 1, 0, 0, 1, 1, 0], Winner: Strategy3! 5, 5, 3
Array: [1, 0, 0, 1, 1, 1, 0, 0], Winner: Strategy1! 3, 4, 4
Array: [0, 1, 1, 1, 0, 0, 0, 1], Winner: Strategy3! 2, 2, 2
Array: [0, 0, 1, 0, 1, 0, 1, 1], Winner: Strategy1! 4, 8, 7
Array: [0, 1, 1, 1, 0, 1, 0, 0], Winner: Strategy3! 2, 2, 2
Array: [1, 1, 0, 0, 0, 0, 1, 1], Winner: Strategy3! 1, 1, 1
Array: [1, 0, 1, 1, 0, 0, 0, 1], Winner: Strategy1! 2, 3, 3
Array: [1, 1, 0, 0, 1, 0, 1, 0], Winner: Strategy3! 1, 1, 1
Array: [1, 0, 0, 1, 0, 0, 1, 1], Winner: Strategy2! 4, 4, 7
Array: [1, 0, 0, 0, 1, 0, 1, 1], Winner: Strategy1! 4, 8, 7
Array: [1, 0, 1, 0, 1, 1, 0, 0], Winner: Strategy3! 3, 5, 3
Array: [0, 1, 1, 0, 0, 1, 1, 0], Winner: Strategy3! 7, 2, 2
Array: [1, 1, 0, 0, 1, 1, 0, 0], Winner: Strategy3! 1, 1, 1
Array: [0, 0, 1, 1, 1, 0, 1, 0], Winner: Strategy1! 2, 3, 4
Array: [1, 1, 0, 1, 0, 1, 0, 0], Winner: Strategy3! 1, 1, 1
Array: [1, 1, 0, 0, 1, 0, 0, 1], Winner: Strategy3! 1, 1, 1
Array: [0, 1, 1, 0, 0, 1, 0, 1], Winner: Strategy3! 7, 2, 2
Array: [0, 0, 0, 1, 1, 0, 1, 1], Winner: Strategy3! 4, 8, 4
Array: [0, 0, 1, 0, 0, 1, 1, 1], Winner: Strategy1! 4, 8, 7
Array: [0, 1, 1, 0, 1, 0, 1, 0], Winner: Strategy3! 7, 2, 2
Array: [1, 0, 0, 1, 1, 0, 1, 0], Winner: Strategy3! 6, 4, 4
Strategy1: 8, Strategy2: 8, Strategy3: 7
```