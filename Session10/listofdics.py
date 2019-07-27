huy = {
    "Name": "Huy",
    "Role": "Waiter",
    "Hours": 12,
    "Salary per Hour($)": 0.8
}
tung = {
    "Name": "Tung",
    "Role": "Cook",
    "Hours": 24,
    "Salary per Hour($)": 1.5
}
mduc = {
    "Name": "M. Duc",
    "Role": "Manager",
    "Hours": 20,
    "Salary per Hour($)": 2
}
emp = [huy, tung, mduc]
don = {
    "Name": "Don",
    "Role": "Waiter",
    "Hours": 12,
    "Salary per Hour($)": 0.9
}
hduc = {
    "Name": "H. Duc",
    "Role": "Waiter",
    "Hours": 14,
    "Salary per Hour($)": 0.7
}
emp.append(don)
emp.append(hduc)
# print(*emp, sep="\n")
budget = 0
for i in range(0,len(emp)):
    monthly_wage = (emp[i]["Hours"]) * (emp[i]["Salary per Hour($)"])
    budget += monthly_wage
    name = (emp[i]["Name"])
    print("The monthly wage of", name, "is", monthly_wage, "$")
print("The required budget is", budget)
a = {
    "Name": "a",
    "Role": "Waiter",
    "Hours": 100,
    "Salary per Hour($)": 0.9
}
emp.append(a)
budget1 = 0
for i in range(0,len(emp)):
    monthly_wage = (emp[i]["Hours"]) * (emp[i]["Salary per Hour($)"])
    budget1 += monthly_wage
    name = (emp[i]["Name"])
    print("The monthly wage of", name, "is", monthly_wage, "$")
print("The required budget is", budget1)