# We will calculate the cost of insurance for various individuals

# This function will house the insurance estimate formula, and print a statement with the person in question's name and cost 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name = "this person"):   # Sex is 0 for Female/AFAB and 1 for Male/AMAB. Smoker is 0 for non-smokers and 1 for smokers
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  
  print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")
  return estimated_cost

# This function will find the difference between costs, and name the people in the comparison
def calculate_insurance_difference(cost1, cost2, name1 = "this amount", name2 = "that amount"):
  costs_list = [cost1, cost2]
  difference = max(costs_list) - min(costs_list)   # This assurse that the costs will always be subtracted correnctly

  print("The estimated difference in insurance cost between " + name1 + " and " + name2 + " is " + str(difference) + " dollars.")
  return difference

# Maria's insurance cost 
maria_insurance_cost = calculate_insurance_cost(28, 0, 26.2, 3, 0, name = "Maria")

# Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(35, 1, 22.2, 0, 1, name = "Omar")

# Coda's insurance cost 
coda_insurance_cost = calculate_insurance_cost(22, 1, 25.0, 0, 0, name = "Coda")

# Demy's insurance cost 
demy_insurance_cost = calculate_insurance_cost(22, 0, 23.9, 0, 1, name = "Demy")

print("\n")   # Separates costs and differences

#Cost differences
maria_vs_omar = calculate_insurance_difference(maria_insurance_cost, omar_insurance_cost, "Maria", "Omar")
coda_vs_demy = calculate_insurance_difference(coda_insurance_cost, demy_insurance_cost, "Coda", "Demy")
mo_vs_cd = calculate_insurance_difference(maria_vs_omar, coda_vs_demy)   # Difference between the difference between Maria and Omar, and the difference between Coda and Demy
