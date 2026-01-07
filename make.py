words=[]
with open("anslist.txt",'r') as f:
    for line in f:
        words.append(line[:-1])

print("[",end="")
for word in words:
    print(f"\'{word}\'",end=",")
print("]")