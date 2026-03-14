# A tuple is collection that is ordered, immutable (cannot be changed) and allows duplicate values, can store mixed data types.

t= ()
t1 = (1,2,3,4,5)
t2 = ("apple", "banana", "cherry")
t3 = (1, "hello", 3.14, True, None)
t4 = ((1,2), (3,4), (5,6))

t5 = (1,)
print(t5)

t6 = (10,20,30,40,50)
print(t6[0])
print(t6[-1])
print(t6[1:4])
print(t6[::-1])

# commone methods
len(t6)
t6.count(10)
t6.index(10)
min(t6)
max(t6)
sum(t6)

# tuple unpacking
person = ("om", 19, "Mumbai")
name, age, city = person
print(name, age, city)

# tuple as dictionary keys because immutable
locations = {
    (10,20): "Mumbai",
    (30,40): "Delhi",
    (50,60): "Pune"
}
print(locations[(10,20)])

# tuple packing
point = 10,20
print(point)