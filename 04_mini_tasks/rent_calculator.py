Monthly_rent = float(input("Enter the monthly rent"))
number_of_days = int(input("Enter the number of days"))

per_day_rent = Monthly_rent / number_of_days
weekly_rent_estimate = per_day_rent * 7

print(f"The monthly rent of the  place : {Monthly_rent: .2f} ")
print(f"The per day rent of the  place :{per_day_rent:.2f}")

print(f"The weekly  rent of the  place : {weekly_rent_estimate: .2f}")

