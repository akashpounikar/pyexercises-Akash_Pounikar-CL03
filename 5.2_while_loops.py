"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: user will input yes or no
# 2. Process: The program will keep asking the user until they provide a valid answer or reach the maximum number of attempts.
# 3. Out: The program will display a message indicating whether the campaign is confirmed as ready or not, along with the number of attempts used.
# 4. My stop condition, my attempt limit, my summary: The stop condition is when the user provides a valid answer ("yes" or "no"). The attempt limit is 3. The summary will include the final status of the campaign and the number of attempts used.


# Your code below
maximum_attempts = 3
attempts = 0
confirmed = False

while attempts < maximum_attempts and not confirmed:
    answer = input("Is the marketing campaign ready? (yes/no): ").strip().lower()
    attempts += 1

    if answer == "yes":
        confirmed = True

if confirmed:
    print("Campaign confirmed as ready.")
else:
    print("Campaign was not confirmed after the maximum attempts.")

print("Number of attempts used:", attempts)