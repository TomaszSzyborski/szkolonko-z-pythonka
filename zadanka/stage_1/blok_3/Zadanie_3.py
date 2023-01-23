"""
Opis:
Kod oblicza i wypisuje BMI z podanej wagi i wzrostu.

Popraw błędy (zdebuguj kod)
"""


def calculate_bmi(weight: int, height: float) -> int:
    return int(weight // (height ** 2))


if __name__ == '__main__':
    patients = [{"weight": 70, "height": 1.8}, {"weight": 80, "height": 1.9}, {"weight": 150, "height": 1.7}]

    for patient in patients:
        bmi = calculate_bmi(**patient)
        print(f"Patient's BMI is: {bmi}")
