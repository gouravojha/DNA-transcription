import re
x = str(input())
lst = re.split("[^A-Z]*",x)
for i in range(len(lst)):
    if lst[i] == "G":
        lst[i] = "C"
    elif lst[i] == "C":
        lst[i] = "G"    
    elif lst[i] == "T":
        lst[i] = "A"
    elif lst[i] == "A":
        lst[i] = "U"
    else:
        lst[i] = ""    
rna = ''.join(map(str, lst))
print(rna)
