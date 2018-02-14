#The TypeError message was because the next line to calculate ctemp is expecting a number and not a string. The 'str' type from raw_input was converted to
#'float' in line 2 to resolve this error.

#The program returned result as 0.0 degrees Celsius always because the brackets were incorrect. This problem was resolved by rearranging the formula in
#line 3 with brackets at proper positions

ftemp = raw_input("Enter degrees in Fahrenheit: ")
ftemp = float(ftemp)
ctemp = ((ftemp - 32) * 5)/9
print ftemp, "degrees Fahrenheit is", ctemp, "degrees centigrade"
