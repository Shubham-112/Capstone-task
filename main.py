import sys
from Addition import Addition
from Multiply import Multiply
from Division import Division
from Subtract import Subtract

print("Enter the operation to perform")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")

argumentList = sys.argv
print(argumentList)
inp = sys.argv[1];

if(inp=="1"):
    op = Addition()
elif(inp=="2"):
    op = Subtraction()
elif(inp=="3"):
    op = Division()
elif(inp=="4"):
    op = Multiply()
else:
    print("Wrong input given")
    sys.exit(0)

    
#a = input("A:")
#b = input("B:")
a = sys.argv[2]
b = sys.argv[3]
print(op.operation(a,b))
