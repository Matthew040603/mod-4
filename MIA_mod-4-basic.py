def savings():

    gross_pay = int(input("Gross Pay: "))
    tax_rate = float(input("Current Tax Rate: "))
    expenses = int(input("Expenses: "))

    tax_rate /= 100

    savings = (gross_pay-round(gross_pay*tax_rate))-expenses

    savings *= 100

    print("Savings: " + str(savings) + " Centavos")
    return

def material_waste():

    total_material = int(input("Total Material: "))
    material_units = str(input("Material Unit (e.g. kg, lbs, etc.): "))
    num_jobs = int(input("Number of Jobs: "))
    job_consumption = int(input("Job Consumption: "))

    material_waste = total_material-(num_jobs*job_consumption)

    print("Remaining Material: " + str(material_waste) + material_units)
    return

def interest():

    principal = int(input("Principal Amount: "))
    rate = float(input("Interest Rate per Period: "))
    periods = int(input("Number of Periods: "))
    rate /= 100
    inter = principal + (principal*rate*periods)

    print("Investment value: " + str(inter))
    return

def body_mass_index():
      weight = float(input("Weight (lbs): "))
      height_ft = int(input("Height (ft): "))
      height_in = int(input("Remaining Height (in): "))

      weight /= 2.2
      height = (height_ft*12)+height_in
      height *= 0.0254

      bmi = weight/(height*height)
      if bmi>30:
          bmi_category = str("Obese")
      elif bmi>25:
          bmi_category = str("Overweight")
      elif bmi>18:
          bmi_category = str("Normal weight")
      else:
          bmi_category = str("Underweight")

      print("Weight (kg): " + str(weight) + "\nHeight (m): " + str(height) + "\nBody Mass Index: " + str(bmi) + "\nBMI Category: " + bmi_category)
      return