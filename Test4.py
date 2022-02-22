def analyze_smoker(smoker_status):   # Function determines whether or not the insurance holder is a smoker, to see if insurance cost can be lowered
  if smoker_status == 1:
     print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")

def analyze_bmi(bmi_value):   # Function determines whether or not the insurance holder is at healthy BMI range, to see if insurance cost can be lowered
  if bmi_value > 30:
     print("Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI.")
  elif bmi_value >= 25 and bmi_value <= 30:
     print("Your BMI is in the overweight range. To lower your cost, you should lower your BMI.")
  elif bmi_value >= 18.5 and bmi_value < 25:
     print("Your BMI is in a healthy range.")
  elif bmi_value < 18.5:
     print("Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.")
      
  if bmi_value < 18.5:   # Statement tells insurance holder how much they should alter their BMI to save money or be healthy
     diff = 18.5 - bmi_value
     print("Increase your BMI by", round(diff, 1), "to be in the healthy weight range.")
  elif bmi_value >= 25:
     diff = bmi_value - 24.9
     print("Decrease your BMI by", round(diff, 1), "to be in the healthy weight range.")

def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):   # Function to estimate insurance cost
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  analyze_bmi(bmi)
  return estimated_cost
 
# Various insurance holder costs
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)
print('\n')
demy_insurance_cost = estimate_insurance_cost(name = 'Demy', age = 22, sex = 0, bmi = 24.0, num_of_children = 0, smoker = 1)
print('\n')
coda_insurance_cost = estimate_insurance_cost(name = 'Coda', age = 22, sex = 1, bmi = 17.6, num_of_children = 0, smoker = 0)
