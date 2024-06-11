# try:
#     width = float(input('Enter rectangle width: '))
#     length = float(input('Enter rectangle length: '))
#     if width == length :
#         exit('That looks like a square.')
    
#     area = width * length
#     print(area)
# except ValueError:
#     print('Please enter a number')
    

try:
    value = float(input('Enter value: '))
    total_value = float(input('enter total_value: '))
    
    percent = (value/total_value) *100
    print(f"that is {percent}%")
    
except ValueError:
    print('Please try again with a number value.')

except ZeroDivisionError:
    print('Your total value cannot be zero.')