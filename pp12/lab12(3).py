print("Obliczenie wskaźnika BMI")
weight = float(input("wprowadź wagę(kg): "))
height = float(input("wprowadź wzrost(cm): "))

def calc_bmi(weight, height_in_m):
    return weight/height_in_m **2
print(calc_bmi(weight,height))

def bmi_cat(bmi):
    if bmi < 18.5:
        return "niedowaga"
    elif bmi < 25:
        return "waga prawidłowa"
    elif bmi < 30:
        return "nadwaga"
    else:
        return "otyłość"

bmi = calc_bmi(weight,height * .01)
category = bmi_cat(bmi)
print("wskaźnik bmi: ",round(bmi,2))
print("kategoria:",category)

