#AND values truth table 
print("True and True : ",True and True)
print("True and False : ",True and False)
print("False and True : ",False and True)
print("False and False : ",False and False)
print()
#OR values truth table 
print("True or True : ",True or True)
print("True or False : ",True or False)
print("False or True : ",False or True)
print("False or False : ",False or False)

#trying the tabular format

from tabulate import tabulate
data=[
    ["True","True",True and True],
    ["True","False",True and False],
    ["False","True",False and True],
    ["False","False",False and False],
]
print(tabulate(data,headers=["    "," AND","    "],tablefmt="grid"))

print(not(True))
print(not(False))