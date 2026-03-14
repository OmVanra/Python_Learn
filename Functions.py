#  Functions are first-class objects — you can pass them as arguments.

# → *args collects extra positional args into a tuple. **kwargs collects keyword args into a dict.

# → Default arguments must come after required ones in the signature.

# Basic function
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Priya"))             # Hello, Priya!
print(greet("Priya", "Hi"))       # Hi, Priya!

# *args and **kwargs
def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4))           # 10

def profile(**info):
    for k, v in info.items():
        print(f"{k}: {v}")

profile(name="Sam", age=30, role="dev")

# Lambda — anonymous one-liner
square = lambda x: x**2
nums = [3, 1, 4, 2]
print(sorted(nums, key=lambda x: -x)) # desc