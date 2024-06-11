# # program with decupling
# feet_inches = input("Enter feet and inches: ")

# def convert(feet_inches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])

#     meters = feet * 0.3048 + inches * 0.0254
#     return meters

# results = convert(feet_inches)

# if results < 1:
#     print("Kid is too small.")
# else:
#     print("Kid can use the slide.")



def strength(password):
    if len(password) >= 8:
        length = True

    for i in password:
        if i.upper():
            upper = True
        if i.isdigit():
            digit = True
    
    if upper == True and digit == True and length == True:
        return 'Strong Password'
    else:
        return 'Weak Password'
    
print(strength('hPbT9lX91IX'))



