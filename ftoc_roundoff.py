ftemp = raw_input("Enter degrees in Fahrenheit: ")
ftemp = float(ftemp)
ctemp = ((ftemp - 32) * 5)/9
print ftemp, "degrees Fahrenheit is", round(ctemp,2), "degrees centigrade"
