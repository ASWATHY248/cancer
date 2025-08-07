import pandas as pd
import sklearn.linear_model as lm
mydata =pd.read_csv("weight_predict_real.csv")
x = mydata[["height", "age", "bmi", "muscle_mass", "body_fat"]]
y = mydata[["weight"]]
model =lm.LinearRegression()
model.fit(x,y)
print("coefficient:", model.coef_)
print("coefficient:", model.intercept_)
getHeight = int(input("Enter the height in cm:"))
getAge = int(input("Enter the age:"))
getBmi = float(input("Enter the bmi:"))
getMusclemass = float(input("Enter the muscle mass:"))
getBodyfat = float(input("Enter the body fat:"))
print(model.predict([[getHeight, getAge, getBmi, getMusclemass, 24.49561779]]))

