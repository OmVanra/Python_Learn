# Creating lists — all the ways

# Literal — most common
nums    = [1, 2, 3, 4, 5]
fruits  = ["apple", "mango", "banana"]
mixed   = [1, "hello", 3.14, True, None]   # any types
nested  = [[1,2], [3,4], [5,6]]            # list of lists
empty   = []

# From other types
chars   = list("hello")        # ['h','e','l','l','o']
r       = list(range(5))       # [0, 1, 2, 3, 4]
r2      = list(range(2,10,2))  # [2, 4, 6, 8]

# Multiply to fill
zeros   = [0] * 5              # [0, 0, 0, 0, 0]
pattern = ["x", "o"] * 3       # ['x','o','x','o','x','o']


# 2. Indexing & slicing — interactive visualizer
# Slicing rules — s[start:stop:step]
s = ["a","b","c","d","e"]

print(s[0])       # "a"        — index 0 (first)
print(s[-1])      # "e"        — last element
print(s[1:4])     # ["b","c","d"] — stop is EXCLUSIVE
print(s[:3])      # ["a","b","c"] — from start
print(s[2:])      # ["c","d","e"] — to end
print(s[::2])     # ["a","c","e"] — every 2nd
print(s[::-1])    # ["e","d","c","b","a"] — reversed!
print(s[-3:])     # ["c","d","e"] — last 3


# .append(x)
# Add x to the end
a=[1,2]; a.append(3) #→ [1,2,3]
# .extend(iter)
# Add all items from iterable
a=[1,2]; a.extend([3,4]) #→ [1,2,3,4]
# .insert(i, x)
# Insert x at index i
a=[1,3]; a.insert(1,2) #→ [1,2,3]
# .remove(x)
# Remove first occurrence of x
a=[1,2,2]; a.remove(2) #→ [1,2]
# .pop(i=-1)
# Remove & return item at i
a=[1,2,3]; a.pop() #→ 3, a=[1,2]
# .index(x)
# Return index of first x
a=["a","b","c"].index("b") #→ 1
# .count(x)
# Count occurrences of x
[1,2,2,3].count(2) #→ 2
# .sort()
# Sort in-place (modifies list)
[3,1,2].sort() #→ [1,2,3]
# .reverse()
# Reverse in-place
[1,2,3].reverse() #→ [3,2,1]
# .copy()
# Shallow copy of the list
# b = a.copy() # b is independent
# .clear()
# Remove all items
a=[1,2,3]; a.clear() #→ []
# sorted(a)
# Returns new sorted list
sorted([3,1,2]) #→ [1,2,3], a unchanged



# Pattern: [expression for item in iterable if condition]

# ── Basic ──────────────────────────────────────────────
squares   = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

doubled   = [x * 2 for x in [3, 1, 4, 1, 5]]
# [6, 2, 8, 2, 10]

upper     = [s.upper() for s in ["hi", "bye"]]
# ['HI', 'BYE']

# ── With filter (if condition) ─────────────────────────
evens     = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

long_words = [w for w in ["hi","python","go"] if len(w) > 3]
# ['python']

# ── Expression with if/else (ternary) ─────────────────
labels    = ["even" if x%2==0 else "odd" for x in range(5)]
# ['even','odd','even','odd','even']

# ── Nested loops ──────────────────────────────────────
pairs     = [(x,y) for x in [1,2] for y in ["a","b"]]
# [(1,'a'),(1,'b'),(2,'a'),(2,'b')]

# ── Flatten a nested list ────────────────────────────
matrix    = [[1,2],[3,4],[5,6]]
flat      = [n for row in matrix for n in row]
# [1, 2, 3, 4, 5, 6]

# ── Real-world examples ───────────────────────────────
prices   = [120, 45, 300, 89, 210]
on_sale  = [p * 0.9 for p in prices if p > 100]
# [108.0, 270.0, 189.0]  — 10% off items > 100

emails   = ["  A@B.COM  ", "c@d.com", " E@F.ORG"]
clean    = [e.strip().lower() for e in emails]
# ['a@b.com', 'c@d.com', 'e@f.org']



# Create a list of 5 numbers. Square each one using a list comprehension. Then filter only those > 10. Do it all in two lines.

list_example = [3,4,5,6,7]
task_1 = [x**2 for x in list_example ]
task_2 = [x for x in task_1 if x > 10]
print("task_1",task_1)
print("task_2",task_2)