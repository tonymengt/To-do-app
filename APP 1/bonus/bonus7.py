password = input("enter new password: ")
result = {}
if len(password)>= 8 :
    result["length"] = True
else :
    result["length"] = False
    # result.append(False)

digit = False
uppercase = False
for i in password:
    if i.isdigit():
        digit = True
    elif i.isupper():
        uppercase = True

result["digits"]= digit
result["uppercase"]= uppercase
# result.append(uppercase)

# uppercase = False
# for i in password:
#     if i.isupper():
#         uppercase = True

# result.append(uppercase)

print(result)

# all function checks the array and output True only when the entire array only contains "True" else will output "False."
if all(result.values()) == True:
    print("Strong Password")
else:
    print("Weak Password")


