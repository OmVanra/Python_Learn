d = {}
d = dict()
d = {"name": "om", "age": 19, "city": "Mumbai"}
d = dict(name="om", age=19, city="Mumbai")
d = dict([("name", "om"), ("age", 19), ("city", "Mumbai")])
d = dict(zip(["name", "age", "city"], ["om", 19, "Mumbai"]))

# get value
d.get('name')
d['name']

# update value
d['name'] = "omkar"
print(d)

# add new key value
d['email'] = "[EMAIL_ADDRESS]"
print(d)

# remove key value
d.pop('email')
print(d)

# remove last key value
d.popitem()
print(d)

# remove all key value
d.clear()
print(d)

# remove dictionary
del d
print(d)


# common methods
len(d)
d.keys()
d.values()
d.items()
d.update({})  # update multiple
d.fromkeys({})
d.setdefault({})
d.copy()
d.clear()
del d
