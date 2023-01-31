import csv

nfile = open("salesreport.csv", "w+")
fileheader = "Customer ID    , Calculated Total\n"
nfile.write(fileheader)
counter = 250
bucket = 0
countdown = 340
meh = 0

with open("sales.csv", "r") as infile:
    csvobj = csv.reader(infile, delimiter=",")
    header = next(csvobj)
    for row in csvobj:
        test = int(row[0])
        if test > counter:
            line = "{}, ${}\n".format(counter, bucket)
            print(line)
            nfile.write(line)
            bucket = 0
            counter = counter + 1
        else:
            counter = counter + 0
        totlist = []
        cid = row[0]
        sub = row[3]
        subint = float(sub)
        totlist.append(subint)
        tax = row[4]
        taxint = float(tax)
        totlist.append(taxint)
        fre = row[5]
        freint = float(fre)
        totlist.append(freint)
        tot = sum(totlist)
        bucket = bucket + tot
        print(tot)
        countdown = countdown - 1
        if countdown == counter:
            line = "{}, ${}\n".format(counter, bucket)
            print(line)
            nfile.write(line)
        else:
            meh = (
                meh + 1
            )  # I know this isn't a realistic way to build it. Kinda McGyvered it at the end, but it works!


nfile.close()
