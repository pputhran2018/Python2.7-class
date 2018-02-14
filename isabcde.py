# Program to read a string and determine if it is abcdearian (i.e. if the letters in the string are in dictionary order, regardless of the case)
# 
# Recursive function returns True if string is abcdearian and False otherwise
# Function ignores non-letter characters and treats all alphabetic characters as lower case
# 
# Program loops until user types end of file(Control-D)
#
# Priyanka Puthran, MHI 289I, Winter 2018
#

#
# Recursive function to check if string is abcdearian or not
#
def isabcde(s):
    # Ignore all non-letter characters, if any
    s = filter(str.isalpha,s)
    # Treat all alphabetic characters as lower case
    s = s.lower()
    # Base case : String of 1 character
    if len(s) == 1: 
        return True
    # now see if the 1st alphabet comes before the 2nd alphabet in the dictionary;
    # if so, check the same with the 2nd and 3rd alphabets, and so on
    elif s[0] <= s[1]:
        return isabcde(s[1:])
    # if prior alphabet does not come before the next alphabet in the string, loop out
    else:
        return False

#
# Main function to get string from user and check if string is abcdearian or not
#
def main():
    while True:
        try:
            string = raw_input('The string? ')
            if isabcde(string) == True:
                print string, 'is abcdearian'
            else:
                print string, 'is not abcdearian'
        # User wants to quit
        except EOFError:
            string = ''
            break
        # User enters only numbers or special characters or combination of both, but no alphabets
        except IndexError:
            string = ''
            break
    return string
    
main()
