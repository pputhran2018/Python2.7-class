# The temperature in degree C at which Vapor Pressure is approx 10mb = 7
import math

try:
    T = input('Enter temperature in degrees C: ') # read in the temperature in degrees Celsius and make it a floating number
    FT = float(T)
    VP = 6.112 * (math.exp((17.67 * FT)/(FT + 243.5)))
    print "At this temperature, the vapor pressure is approximately", VP, "millibars"

    #To estimate temp at which VP is approx 10
    #if VP > 10:
        #while (round(VP,0)) != 10:
            #FT = FT-1
            #VP = 6.112 * (math.exp((17.67 * FT)/(FT + 243.5)))
    #elif VP < 10:
        #while (round(VP,0)) != 10:
            #FT = FT+1
            #VP = 6.112 * (math.exp((17.67 * FT)/(FT + 243.5)))
    #print "The temperature at which Vapor Pressure is approximately 10mb is:"
    #print "Temperature :", FT, " Vapor Pressure:", round(VP,2)
    
except:
    print "Please enter a number " 
