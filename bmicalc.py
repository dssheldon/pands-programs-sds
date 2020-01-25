# This program will calculate the bmi of a person and
#  let them know whether they are within or outside the
#   acceptable range

height = float(input("Enter your height in cms: "))
weight = float(input("Enter your weight in kgs: "))

bmi = round((weight) / ((height/100)**2),2)

if bmi < 18.5:
    bmitext = "underweight."
elif bmi >= 25.0:
    bmitext = "overweight."
else:
    bmitext = "within range."

print("Your bmi is", bmi, "and you are currently", bmitext)
