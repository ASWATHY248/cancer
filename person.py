import pandas as pd
import sklearn.linear_model as lm
from sklearn.preprocessing import LabelEncoder

mydata = pd.read_csv("persons.csv")

le_gender = LabelEncoder()
le_bodytype = LabelEncoder()
mydata["gender_encoded"] = le_gender.fit_transform(mydata["Gender"])
mydata["bodytype_encoded"] = le_bodytype.fit_transform(mydata["BodyType"])

x =mydata[["Age", "gender_encoded", "bodytype_encoded", "Height"]]
y = mydata["Weight"]

model = lm.LinearRegression()
model.fit(x, y)

age = int(input("Enter age: "))
gender = input(f"Enter gender {list(le_gender.classes_)}: ")
bodytype = input(f"Enter bodytype {list(le_bodytype.classes_)}: ")
height = int(input("Enter height: "))


gender_encoded = le_gender.transform([gender])[0]
bodytype_encoded = le_bodytype.transform([bodytype])[0]

predicted_weight = model.predict([[age, gender_encoded, bodytype_encoded, height]])
print("Predicted weight:", predicted_weight[0])