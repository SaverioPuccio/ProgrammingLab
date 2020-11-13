values=[]

file=open("shampoo_sales.csv", "r")

for line in file:
    elements = line.split(",")

    if elements[0] != 'Date':

            value=elements[1]
            values.append(float(value))

            
print(values)
print("SOMMA: {}".format(sum(values)))