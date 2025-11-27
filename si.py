import sys

# Expecting: python si.py principal rate
if len(sys.argv) == 3:
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
else:
    print("Please provide principal and rate as command-line arguments.")
    sys.exit(1)

si = (principal * rate) / 100
print("Simple Interest:", si)

# Validate values
if principal <= 0:
    print("Principal must be greater than 0")
elif rate <= 0:
    print("Rate must be greater than 0")
elif time <= 0:
    print("Time must be greater than 0")
else:
    simple_interest = (principal * rate * time) / 100
    print("Simple Interest =", simple_interest)
