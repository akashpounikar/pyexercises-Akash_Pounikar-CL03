"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: list of random numbers     
# 2. Process: sort the list in ascending, descending and reverse order
# 3. Out: We will get the original list, ascending order, descending order and reverse order of the original list
# 4. My four orders, and which ones modify the original:  the four orders are ascending order, descending order, reverse order and original order. The original list is not modified in any of the four orders.


# Your code below
numbers = [500, 750, 1200, 600, 900, 1500, 400, 1100]

print("1. Original order:", numbers) 

ascending_numbers = sorted(numbers) 
print("2. Ascending order:", ascending_numbers) 

descending_numbers = sorted(numbers, reverse=True)  
print("3. Descending order:", descending_numbers)

reversed_numbers = numbers[::-1]
print("4. Reverse original order:", reversed_numbers)

print("Original list is still unchanged:", numbers) 

