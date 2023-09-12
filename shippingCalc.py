weight = 8.4

# Ground Shipping
if (weight <= 2):
    cost = weight * 1.5 + 20
elif (weight <= 6):
    cost = weight * 3.0 + 20
elif (weight <= 10):
    cost = weight * 4.0 + 20
else:
    cost = weight * 4.75 + 20

print(cost)