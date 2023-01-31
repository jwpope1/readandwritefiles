import csv

with open("EmployeePay.csv", "r") as infile:
    csvobj = csv.reader(infile, delimiter=",")
    header = next(csvobj)
    for row in csvobj:
        first = row[1]
        last = row[2]
        salary = row[3]
        bonus = row[4]
        line1 = "First Name: {}\t Last Name: {}\n".format(first, last)
        print(line1)
        line2 = "Salary: ${}\n".format(salary)
        print(line2)
        line3 = "Bonus: {}\n".format(bonus)
        print(line3)
        print("##################################\n")
