def bmi(height, weight):
  return round((weight / height**2),2)

h = float(input("Enter Your Height in Meters: "))
w = float(input("Enter Your weight in kg: "))

print("WELCOME TO THE INSANT BMI CALCULATOR.")

bmix = bmi(h, w)
print("your BMI is: ", bmix)

if bmix <= 18.5:
  print("YOU ARE UNDERWEIGHT")
elif 18.5 < bmix <=24.9:
  print("YOUR WEIGHT IS NORMAL.")
elif 25 < bmix <=29.29:
  print("YOU ARE OVERWEIGHT.")
else:
  print("YOU ARE OBESE.")
