"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: We input information about a marketing campaign.
# 2. Process: We read the information, change it, remove one field, and display every field with its value.
# 3. Out: The updated campaign details.
# 4. My object, my five fields, and why those: I chose a marketing campaign with fields for name, channel, target audience, budget, and start date because these are essential pieces of information for managing a campaign.

# Your code below
campaign = {
    "name": "Summer Product Launch",
    "channel": "Instagram",
    "target_audience": "Young adults aged 18-30",
    "budget": 1200,
    "start_date": "2026-06-01",
    "status": "Active"
}

# Read one field
print("Campaign name:", campaign["name"])

# Ask for a field that does not exist safely
print("Location:", campaign.get("location", "Location not available"))

# Change one field
campaign["budget"] = 1500

# Remove one field
del campaign["start_date"]


# Display every remaining field and its value
print("\n Updated campaign details:")
for field, value in campaign.items():
    print(field + ":", value)