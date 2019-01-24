#Tristan Meyer
#Linear System of Equations

A = float(input("Enter A: "))
B = float(input("Enter B: "))
C = float(input("Enter C: "))
D = float(input("Enter D: "))
E = float(input("Enter E: "))
F = float(input("Enter F: "))

y = ((F*A)-(D*C))/((-D*B)+(E*A))
x = (C-(B*(y)))/A
sy = str(y)
sx = str(x)
print("The solution is ("+sx+","+sy+")")