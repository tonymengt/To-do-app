# def get_avg():
#     with open("APP 1/bonus/files/data.txt", 'r') as file:
#         data = file.readlines()
#     values = data[1:]
    
#     # final = []
#     # for i in values:
#     #     final.append(float(i.strip('\n')))
#     # return final

#     for i, j in enumerate(values):
#         values[i] = j.strip('\n')
#     return values
    
#     # values = [float(i) for i in values]

#     # average = sum(values) / len(values)
#     # return average


# avg = get_avg()
# print(avg)




# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     x = min(grades)
#     y = max(grades)
#     return x, y

def get_max():
    grades = [9.6, 9.2, 9.7]
    arr = []
    arr.append(min(grades))
    arr.append(max(grades))
    return arr

print(f"Max: {get_max()[1]}, Min: {get_max()[0]}")