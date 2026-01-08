"""
ShadowFox Python Development Internship
Task 1 - Beginner Level
Topic: Dictionary
"""

# -------------------------------
# Program 1: Friends Name Length
# -------------------------------

friends = ["Aditya", "Rahul", "Amit", "Saurabh", "Rohit"]

friends_name_length = []

for name in friends:
    friends_name_length.append((name, len(name)))

print("Friends name with their name length:")
print(friends_name_length)


# --------------------------------
# Program 2: Expense Tracker
# --------------------------------

your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("\nYour total expenses:", your_total)
print("Partner total expenses:", partner_total)

if your_total > partner_total:
    print("You spent more money.")
elif partner_total > your_total:
    print("Your partner spent more money.")
else:
    print("Both spent the same amount.")

max_difference = 0
difference_category = ""

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > max_difference:
        max_difference = difference
        difference_category = category

print("Maximum difference category:", difference_category)
print("Difference amount:", max_difference)
