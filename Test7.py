names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]


total_cost = 0
i = 0
while i < len(actual_insurance_costs):
  total_cost += actual_insurance_costs[i]
  i += 1


average_cost = total_cost / len(actual_insurance_costs)
print("Average Insurance Cost: " + str(average_cost) + " dollars.")


for i in range(0, len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  difference = insurance_cost - average_cost
  print("The insurance cost for " + str(name) + " is " + str(insurance_cost) + " dollars.")

  if difference > 0:
    print("The insurance cost for " + str(name) + " is " + str(difference) + " above average.")
  elif difference < 0:
    difference *= -1
    print("The insurance cost for " + str(name) + " is " + str(difference) + " below average.")
  else:
    print("The insurance cost for " + str(name) + " is equal to the average.")


updated_estimated_costs = [round(11/10 * cost, 1) for cost in estimated_insurance_costs]
print("Updated estimated costs: " + str(updated_estimated_costs))
