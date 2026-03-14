# Given s = 'Python is awesome', reverse it, capitalize the first letter, count how many 'e's are in it, and replace 'awesome' with 'powerful'.


s = "Python is awesome"

print("reversed string :",s[::-1])

print("capitalize first latter :", s.capitalize())

print("count e :", s.count("e"))

print("replace awesome with powerful :", s.replace("awesome", "powerful"))