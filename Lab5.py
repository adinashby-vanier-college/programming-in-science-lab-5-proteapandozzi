# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    #empty_space = "*" + "" + (n-2) + "" + "*" /n 

   ''' n = 5
    i = 0
    while i = n:
        return n * ""
    elif i == 0 or i == 1
            return "*" + " " + "n-2" + " "
            '''


        
    
        
   
   
   
   
   


# 1
# 12
# 123
# 1234
def number_pattern(n):
    screen = ""
    i = 1
    while i <= n:
        j = 1
        line = ""

        while j <= i:
            line = line + str(j)
            j += 1

        #print (line)
        line += "\n"
        screen += line
        i += 1
    return screen.strip()

#print (number_pattern(4))
#number_pattern(9)
#number_pattern(0)

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
  total = 0
  i = 1
  while i <= n:
      total += i
      i += 1
  return total

#print(sum_of_natural_numbers(5))       
  
  
  
  
  
  
    

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    return ""