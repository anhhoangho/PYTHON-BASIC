def oilfield(filepath):
    pass

def find(of):
    pass

def pipelength(of):
    pass

# main script starts here

print("Lab 7 - Exercise 6\n")

filepath = input("Enter the path of the data file: ").strip()
of = oilfield(filepath)
y = find(of)
pipelen = pipelength(of)

print("The main pipeline is the line y =",y)
print("The total pipeline length is {:1.2f}".format(pipelen))
