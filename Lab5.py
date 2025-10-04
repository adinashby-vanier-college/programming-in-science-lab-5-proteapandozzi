# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if n <= 0:
        return ""
    if n == 1:
        return "*"
 
    i = 0
    result = ""
 
    while i < n:
        if i == 0 or i == n - 1:        # top or bottom row
            line = "*" * n
        else:                           # middle rows
            line = "*" + " " * (n - 2) + "*"
 
        result += line
        if i < n - 1:                   # add newline except for the last row
            result += "\n"
        i += 1
 
    return result
 
print(hollow_square(5))
 
 
 


        
    
        
   
   
   
   
   


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
  
   
   
    pyramid = ""
    i = 1
    width = 2 * n -1

    while i <= n:
        stars = "*" * (2 * i - 1)
        pyramid += stars.center(width) .rstrip()
        if i != n:
            pyramid += "\n"
    
        i += 1
    return pyramid
print(centered_star_pyramid(4))

















    
