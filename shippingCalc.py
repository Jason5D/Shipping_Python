weight = 4.8

# Ground Shipping
if (weight <= 2):
    groundCost = weight * 1.5 + 20
elif (weight <= 6):
    groundCost = weight * 3.0 + 20
elif (weight <= 10):
    groundCost = weight * 4.0 + 20
else:
    groundCost = weight * 4.75 + 20

print("Ground Cost: " + str(groundCost))

# Premium Shipping
premium = 125
print("Premium Cost: " + str(premium))

# Drone Shipping
if (weight <= 2):
    droneCost = weight * 4.5
elif (weight <= 6):
    droneCost = weight * 9
elif (weight <= 10):
    droneCost = weight * 12
else:
    droneCost = weight * 14.25

print("Drone Cost: " + str(droneCost))