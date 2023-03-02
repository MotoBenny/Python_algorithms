# Insertion sort

Example list: [1, 8, 6, 4, 6, 8, 3, 2]

Insertion sort begins by finding the length of the unsorted list, This gives us a
number we can use to control the number of iterations.

We then assign a variable to the value of the 2nd item in the list (this is index 1)

[img](img1.png)

Once we have this value, we compare it against the value in our list, immediately
to its left (index 1 -1, or index 0) within a while loop.

Effectively saying, While the value to the left of our current number is greater than
our current number, Swap their positions in the list.

In this case, the value to the left of current value is less than current value, so
we do nothing, except move to the next iteration of the for loop.

[img](img2.png)

Now we grab the next value in our list, so current value now = 6, the value to the left of current value
is greater than out current value, so inside our while conditional we swap those values

[img](img3.png)

We then proceed to repeat this process until the end list is completely sorted, we
cannot leave our whileloop until our value to the left of our current is less than
the current, In this case all the values to the left of our current are properly sorted.
Then we move on to the nest iteration of our for loop, until we hit the end of our loop,
Due to the conditional of our while loop, we know our list is now properly sorted. 

[1, 2, 3, 4, 6, 6, 8, 8]