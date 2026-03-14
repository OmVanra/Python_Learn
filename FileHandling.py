# The only way to open files — always use with
with open("file.txt", "r") as f:
    content = f.read()


# . File modes — the 4 you actually use
# "r"
# Read. File must exist. Default mode.
# "w"
# Write. Creates file or wipes it if it exists.
# "a"
# Append. Creates file or adds to end.
# "x"
# Create. Fails if file already exists.
# "w" silently destroys existing content. If you want to add to a file, use "a". If you want to avoid overwriting, use "x".

# Reading — 3 ways, know when to use each
# read() — entire file as one string (small files only)
with open("file.txt") as f:
    content = f.read()
    print(content)

# readlines() — all lines as a list
with open("file.txt") as f:
    lines = f.readlines()        # [line1\n, line2\n, ...]
    lines = [l.strip() for l in lines]  # strip \n from each

# Iterate line by line — best for large files
with open("file.txt") as f:
    for line in f:              # reads one line at a time
        print(line.strip())


# Writing
with open("file.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("Welcome to Python.")

# Appending
with open("file.txt", "a") as f:
    f.write("\nAppended text.")

# Creating
with open("new_file.txt", "x") as f:
    f.write("New file created.")


# JSON — what you'll use most in real projects
import json

# Writing
with open("data.json", "w") as f:
    json.dump([1,2,3], f)

# Reading
with open("data.json", "r") as f:
    data = json.load(f)
    print(data)


# Error handling — always do this in real code
try:
    with open("file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")


# The real-world pattern you'll write 100 times
import json, os

# Load → modify → save back
def load_data(path, default=None):
    if not os.path.exists(path):
        return default if default is not None else {}
    with open(path) as f:
        return json.load(f)

def save_data(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

# Usage
users = load_data("users.json", default=[])
users.append({"name": "Priya", "role": "admin"})
save_data("users.json", users)