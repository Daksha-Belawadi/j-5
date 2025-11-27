import sys
if len(sys.argv) == 4:
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
    print("User provided values:")
else:
    # Default values if not provided
    principal = 10000
    rate = 5
    time = 2
    print("No input given - using default values:")

simple_interest = (principal * rate * time) / 100

print("Principal =", principal)
print("Rate =", rate)
print("Time =", time)
print("Simple Interest =", simple_interest)
