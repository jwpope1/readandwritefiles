import csv

nfile = open("Revisedcustomers.csv", "w+")
fileheader = "First Name    , Last Name , Country\n"
nfile.write(fileheader)

with open("customers.csv", "r") as infile:
    csvobj = csv.reader(infile, delimiter=",")
    header = next(csvobj)
    for row in csvobj:
        first = row[1]
        last = row[2]
        country = row[4]
        line = "{}, {}, {}\n".format(first, last, country)
        nfile.write(line)


nfile.close()
