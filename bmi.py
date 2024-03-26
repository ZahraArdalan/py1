height = float(input("enter your height in m :"))
weight = float (input("enter your weight in kg :"))
bmi = round (weight / (height)**2)
if bmi <18.5:
    print(f"your bmi is {bmi}, are you underweight.")
elif bmi<25: 
    print(f"your bmi is {bmi}, are you normal weight.")
elif bmi<30:
    print(f"your bmi is {bmi}, are you owerweight.")
elif bmi <35:
    print(f"your bmi is {bmi}, are you obese.") 
else:
    print(f"your bmi is {bmi}, are you clinically obese.")              


 






