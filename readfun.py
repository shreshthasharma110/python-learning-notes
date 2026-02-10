p="test.txt"

with open (p, 'r') as f:
    for line in f:
        print(line.rstrip())  

# here r.strip removes all the spaces, tabs and lines ,