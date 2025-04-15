import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("employees.csv")

name_count = 0
hire_count = 0
dob_count = 0
city_count = 0

for employee in data["name"]:
    if employee is None or pd.isna(employee):
        name_count += 1

for date in data["hire_date"]:
    x = date.split("-")
    if date is pd.isna(date):
        hire_count += 1
    else:
        if int(x[0]) < 2015:
            hire_count += 1

dob_count = (data['birth_date'] > data['hire_date']).sum()

eids = set(data['eid'])
eid_count = (~data['reports_to'].isin(eids)).sum()
city_counts = data['city'].value_counts()
for y in city_counts:
    if y == 1:
        city_count += 1

ids = data["eid"]
salaries = data["salary"]
plt.hist(salaries, log=True, edgecolor='black')
plt.xscale('log')
plt.title('Salary Distribution (Log Scale)')
plt.xlabel('Salary')
plt.ylabel('Employees')
plt.savefig('plot')

print(f"First name assertion count: {name_count}")
print(f"Hire date before 2016: {hire_count}")
print(f"DOB is after hire date: {dob_count}")
print(f"Reports_to EID does not exist: {eid_count}")
print(f"Only one employee in a city: {city_count}") 
