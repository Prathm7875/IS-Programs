import math
n=int(input("n = "))
g=int(input("g = "))
for i in range(2,n):
    if(n%i==0):
        print("Invalid")
        break
for i in range(2,g):
    if(g%i==0):
        print("Invalid")
        break
    
x=int(input("No. selected by Alice: "))
y=int(input("No. selected by Bob: "))

A=(math.pow(g,x))%n
B=(math.pow(g,y))%n

print("\nA=",A)
print("B=",B)

k1=(math.pow(B,x))%n
k2=(math.pow(A,y))%n
print("\nk1=",k1)
print("k2=",k2)
if(k1==k2):
    print("Algorithm is correct")
else:
    print("Algorithm is wrong")
# ------------------------------------------------------------------------------------------------------------------------

# Output:

# %Run 'Python source file.py'
# n = 23
# g = 5
# No. selected by Alice: 4
# No. selected by Bob: 3

# A= 4.0
# B= 10.0

# k1= 18.0
# k2= 18.0
# Algorithm is correct
