
iteam = {
    "pen":10,
    "Pencil": 10,
    "scissor": 50,
    "paper":300,
    "Note Book":200,
}

print("Welcome to stationery shop")
print("pen:10\n Pencil:10\n scissor:50\n paper:300\n Note Book:200\n")

totalcost=0

order1=input("enter iteam name")

if order1 in iteam :
  totalcost += iteam[order1]
  print(f"{order1} is added")

more_order= input("wanna order more? yes/no")

if more_order == "yes":
  order2 =input("enter iteam name")

if order2 in iteam:
  totalcost +=iteam [order2]
  print("another  iteam added")


else:
  print("wrong iteam")


print(f"total cost is {totalcost}")