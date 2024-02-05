weight = float(input("hi enter  your   weight: "))
height = float(input(" hi enter your height: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")