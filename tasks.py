students = ["Riya", "Arjun", "Priya", "Dev", "Zara", "Meera"]
# Do all of this in as few lines as possible:

# Reverse the list
# Extract only the students whose name has more than 4 characters
# Print them in uppercase, numbered from 1 using enumerate

students.reverse()

long_names = [s for s in students if len(s) > 4]

for i, name in enumerate(long_names, start=1):
    print(f"{i}. {name.upper()}")




# items  = ["apple", "banana", "mango", "kiwi", "grape"]
# prices = [30, 80, 60, 120, 50]
# ```
# Using a single list comprehension, create a list of strings like `"apple - ₹27.0"` but only for items that cost more than ₹50, with a 10% discount applied to the price.

# Expected output:
# ```
# ['banana - ₹72.0', 'mango - ₹54.0', 'kiwi - ₹108.0']
items  = ["apple", "banana", "mango", "kiwi", "grape"]
prices = [30, 80, 60, 120, 50]

result = [
    f"{item} - ₹{price * 0.9}"
    for item, price in zip(items, prices)
    if price > 50
]

print(result)    






# records = [
#     ("Arjun", 85, "Mumbai"),
#     ("Priya", 92, "Delhi"),
#     ("Dev",   78, "Pune"),
#     ("Zara",  92, "Chennai"),
#     ("Riya",  85, "Ahmedabad"),
# ]
# ```
# Do the following:
# - Sort records by score descending, then by name ascending when scores are tied
# - Print the top 3 students with their rank, name and score
# - Find all students who scored above the average score

# Expected output:
# ```
# Rank 1: Priya — 92
# Rank 2: Zara — 92
# Rank 3: Arjun — 85
# Above average (86.4): Priya, Zara


records = [
    ("Arjun", 85, "Mumbai"),
    ("Priya", 92, "Delhi"),
    ("Dev",   78, "Pune"),
    ("Zara",  92, "Chennai"),
    ("Riya",  85, "Ahmedabad"),
]

# Sort by score descending (-score), then name ascending
sorted_records = sorted(records, key=lambda r: (-r[1], r[0]))

# Print top 3
for rank, (name, score, city) in enumerate(sorted_records[:3], start=1):
    print(f"Rank {rank}: {name} — {score}")

# Average and above-average students
avg = sum(r[1] for r in records) / len(records)
above = [r[0] for r in records if r[1] > avg]
print(f"\nAbove average ({avg}): {', '.join(above)}")




# Print all prime numbers between 1 and 50 using a for loop and an inner loop to check divisibility.

for num in range(2, 51):
    is_prime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")


# Write a function that takes any number of strings and returns the longest one. If two are equal length, return the first.

def longest_string(*Args):
    return max(Args, key=len)

print(longest_string("apple", "banana","banana", "cherry", "date"))
