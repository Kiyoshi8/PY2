#for x in "turon with ice cream":

 #   print(x)


a = 200
b = 330

if b == a:
  print("b is equall than a")
else:
  print("b is not equal than a")


i = 1
while i < 6:
  print(i)
  i += 1


i = 1
while i < 6:
  print(i)
  i += 1

print("Siomai \n" *100)

#break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


#continue statament
i = 0
while i < 50:
  i += 1
  if i == 49:
    continue
  print(i)

#else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)