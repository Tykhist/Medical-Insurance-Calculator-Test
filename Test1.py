# We will calculate the cost of insurance for a 28-year-old, nonsmoking woman who has three children and a BMI of 26.2
age = 28
smoker = 0   # 0 for a non-smoker, 1 for a smoker
sex = 0   # 0 for female, 1 for male (assigned gender at birth)
bmi = 26.2
num_of_children = 3

# insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print('This person\'s insurance cost is', insurance_cost, 'dollars.\n')

# Age Factor: to see how much of a factor age plays in the formula, we will increase it and then find the difference between the new and old insurance costs
age += 4

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print('The change in cost of insurance after increasing the age by 4 years is', change_in_insurance_cost, 'dollars.\n')
# BMI Factor: same method as age factor, except we will revert age to its original value
age -= 4
bmi += 3.1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print('The change estimated insurance cost after increasing BMI by 3.1 is', change_in_insurance_cost, 'dollars.\n')
# Male vs. Female Factor: same method as bmi factor, except we will revert bmi to its original value
bmi -= 3.1
sex = 1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print('The change in estimated cost for being male instead of female is', change_in_insurance_cost, 'dollars.\n')
# Smoker Factor: same method as Male vs. Female factor, except we will revert sex to its original value
sex = 0
smoker = 1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print('The change in estimated cost for being a smoker is', change_in_insurance_cost, 'dollars.\n')
# And finally, Number of Children Factor: same method as smoker factor, except we will revert smoker to its original value
smoker = 0
num_of_children += 2

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print('The change in estimated cost for having an additional 2 children is', change_in_insurance_cost, 'dollars.')
