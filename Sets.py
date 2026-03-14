# set is unordered (indexing and slicing are not allowed) collection of unique elements and mutable.

# creating sets
s = set()
s = set()
s = {1,2,3,4,5}
s = {"apple", "banana", "cherry"}
s = {1, "hello", 3.14, True, None}
s = {(1,2), (3,4), (5,6)}
s = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5}
print(s)

# common methods
len(s)
s.add(6)
s.update([7,8,9])
s.remove(1)
s.discard(2)
s.pop()
s.clear()
s.copy()
del s

# set operations
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1.union(s2)
s1.intersection(s2)
s1.difference(s2)
s1.symmetric_difference(s2)
s1.issubset(s2)
s1.issuperset(s2)
s1.isdisjoint(s2)

# frozenset
f = frozenset({1,2,3,4,5})
print(f)

# frozen set is immutable and can be used as dictionary keys
d = {frozenset({1,2,3}): "om", frozenset({4,5,6}): "omkar"}
print(d)

