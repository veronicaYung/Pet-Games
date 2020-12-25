Veronica Yung

## **GAME SUMMARY**

Pet games is made up of of a collection of simple activities that lead up to an ultimate game where each user competes to be on the leaderboard. The difficulty of this ultimate game depends on the user's progress bar. Each activity in the game corresponds to a skill, the more skills you build up, the more you will be equipped to do well in the final competing game. These activities are targeted towards kids to help them develop sequencing, association by shape and preference skills. 

**TUTORIALS**

There are two possible tutorials— bathing and baking. In these tutorials, the user must select the correct sequence of steps to accomplish their goal of either bathing or baking.  When the user plays the game more often, they will be able to create patterns from a very young age, this will help them establish the ability to create sequences in their every day lives.

**INTUITION**

This is inspired by Pokemon's feature, "Guess that Pokemon," the user is expected to associate a shadow of an animal with the name of the animal. Having the ability to associate items with shapes is crucial when helping kids recognize everyday items or faces. 

**FOOD COURT**

When the user chooses a food item to feed to their pet, depending on whether or not it is considered healthy, the user will either gain or lose points. Before leaving the food court, if the user gets at least 5 points, their progress bar will go up. Being able to distinguish between healthy from unhealthy foods by knowing when your progress bar goes up teaches the user what they should eat to be rewarded. 

## Runtime/Space Complexity Analysis

1. Dictionaries 
- Function: progbar() and drawbar()
▪ This function reads in from a file that records the user’s activity list
▪ Because the activities are added from most recently completed to old data, I
decided to use dictionaries because it would be really fast to get data to draw
the new progress bar and because keys are unique, it allowed me to only got
the most recent activity of the user
    - This action of calling the value with a key is O(1) because dictionaries store the
    key as a hash value, all hash values are unique and thus the call to get a value
    does not require you to check every item in the list to return the value.

2. Collision function

- For every rock in rock list → O(n), n being number of rocks in rock list
▪ Draw rock hitbox → perform action
▪ Check if the player and rock collide →
    - Write score into text file →  all of these actions are O(1), happens once
    • Call leaderboard                 regardless of how many rocks you have
    • Close game
    - Draw rock and check collision for n amount of times, n being the amount of rocks
    ▪ Number of rocks in list can vary from 1-10 depending on the delay
    - Everything under is constant time and will only run once no matter how many rocks you
    have (getting hit ends game, writes score and goes to leader board)
    - Therefore, the current worst-time runtime complexity is O(n), n can be modified so that
    the upper bound of n can be greater than 10

3. Leaderboard sorting

- Merge Sort
    - Each partition halves the previous length of the list
    • If the length of the list is 8, we see 2^3 = 8, meaning you would only
    need to half the list 3 times
    ▪
    - Therefore, the splitting of merger sort is O(logn)
    - Again with our example, because we have to split the list 3 times, we have to do
    n amount of work to each subset of the original list. The actual merge list is the
    work that has to be done every level and therefore if we combine the amount of
    work needed to be executed for each level, we have O(n*logn)
    - Knowing how merge sort works, the worst, best, and average case would be
    O(n*logn) since it would have to keep on splitting the list until it reaches the
    base case regardless of if the list is sorted or not.

## Trade-offs

1. Opening files
    - using the open( ) function is efficient, it ‘s time complexity is constant→ O(1).

    Trade offs:

    - Saving files on computer take up space, depending on file size, it can vary
    - If you save it on your local drive→ it would take hard drive space

2. Merge sort

- Efficient in terms of time complexity → O(nlogn) in all 3 cases

Trade offs:

- Cumulative size of all levels of partition add up to n amount of items in list
- not sorting in-place using swaps, but to perform the merge, we store left and
right part of list in temporary arrays
- In worst case, left and right mini arrays will have size n/2 each and so the
temporary space would be O(n), which is the space complexity.
