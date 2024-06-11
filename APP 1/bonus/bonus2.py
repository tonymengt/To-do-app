filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]
for i in filenames:
    i = i.replace(".", "-", 1)
    print(i)

print(filenames)

