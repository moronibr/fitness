# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime

gender = input("Enter your gender (M or F): ")
birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

def main(gender, birth_str, height, weight):
    # Get the user's gender, birthdate, height, and weight.
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
   
    # Print the results for the user to see.
    print(f"Age (years): {compute_age(birth_str)}")
    print(f"Weight (kg): {kg_from_lb(weight)}")
    print(f"Height (cm): {cm_from_in(height)}")
    print(f"Body mass index: {body_mass_index(weight, height)}")
    print(f"Basal metabolic rate: {basal_metabolic_rate(gender, weight, height, birth_str)}")
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    years_int = int(years)

    return years_int


def kg_from_lb(weight):
    calculated_kg = weight * 0.45359237
    kilos = round(calculated_kg, 2)  # Round to 2 decimal places
    return kilos



def cm_from_in(inches):
    calculated_cm = inches * 2.54
    centimeters = round(calculated_cm, 2)
    return centimeters


def body_mass_index(weight, height):
    kg_from_lb(weight)
    cm_from_in(height)
    height_meter = cm_from_in(height) / 100
    calculated_bmi = kg_from_lb(weight) / (height_meter * height_meter)
    bmi = round(calculated_bmi, 2)
    return bmi 
    


def basal_metabolic_rate(gender, weight, height, birth_str):
    gender 
    age = int(compute_age(birth_str))

    if gender.lower() == "m":
        bmr_male = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        bmr = round(bmr_male, 2)
    elif gender.lower() == "f":
        bmr_female = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        bmr = round(bmr_female, 2)
    else:
         raise ValueError("Invalid gender. Please enter 'male' or 'female'.")


    return bmr







main(gender, birth_str, height, weight)

# Call the main function so that
# this program will start executing.

