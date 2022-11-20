"""
Opis:
Kod oblicza i wypisuje BMI z podanej wagi i wzrostu.

Popraw błędy (zdebuguj kod)
"""
patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, h):
    return int(h // (weight * 2))

for i, patient in enumerate(patients):
    weight, height = patients[0]
    bmi = calculate_bmi(height, weight)
    print("Patient's BMI is: {}".format(bmi))
