# using (read) reads all the file at once
p = "test.txt"

with open (p, "r") as f:
    print(f.read())
