# → Python uses indentation (4 spaces) instead of braces for blocks.

# → for loops iterate over any iterable — list, string, range, dict.

# → while loops run until a condition is False. Use break and continue to control flow.


# if / elif / else
score = 72
if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "C"

# Ternary (one-liner)
result = "pass" if score >= 50 else "fail"

# for loop + range
for i in range(1, 6):
    print(i, end=" ")        # 1 2 3 4 5

# enumerate — index + value
fruits = ["apple", "mango"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# while + break
n = 10
while n > 0:
    print(n)
    n -= 2
    if n == 4: break