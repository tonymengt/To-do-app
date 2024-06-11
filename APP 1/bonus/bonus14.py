# program with decupling
from parse14 import parse
from convert14 import convert

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
results = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {results} meters")

if results < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")


    