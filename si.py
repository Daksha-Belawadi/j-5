if len(sys.argv) == 4: 
principal = sys.argv[1] 
rate = sys.argv[2] 
time = sys.argv[3] 
print("User provided input values:") 
else: 
print("No input given - using default values:") 
principal = "1000" 
rate = "5" 
time = "2" 
# Calculation 
simple_interest = (eval(principal) * eval(rate) * eval(time)) / 100
