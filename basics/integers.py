x = 1.4
y = 2.67

# Round to decrease the number of digits after a float
z = round(x + y)
print(z)

# Another way to format on python is
input1 = float(input('Write the first number: '))
input2 = float(input('Write the second number: '))

# We can also pass the number of digits to round
z = (input1 / input2)

# This is used to made a good example of the format
print(f"{z:.2f}")
