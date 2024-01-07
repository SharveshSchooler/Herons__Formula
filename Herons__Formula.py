a=int(input("Enter a size of the side in cm"))
b=int(input("Enter a size of the side in cm"))
c=int(input("Enter a size of the side in cm"))

s =(a + b + c) / 2
Area_of_Scalene_Trinagle = ((s)*(s-a)*(s-b)*(s-c))**0.5
print(Area_of_Scalene_Trinagle,"cm")