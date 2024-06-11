date = input("enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Write down you thoughts: \n")

with open(f"APP 1/bonus/journal/{date}.txt", 'w') as file:
    file.write(mood + 2* '\n')
    file.write(thoughts)