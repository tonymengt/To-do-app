# contents = ['hello', 'hihihihihi', 'bybyby']

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# for  content, filename in zip(contents, filenames):
#     file = open(f"APP 1/bonus/files/{filename}", 'w')
#     file.write(content)
#     file.close()



# contents = ['hello']

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# for  filename in filenames:
#     file = open(f"APP 1/bonus/files/{filename}", 'w')
#     file.write('hello')
#     file.close()


# prompt = input('please enter a new name: ')
# file = open('APP 1/bonus/files/members.txt', 'r')
# content = file.readlines()
# file.close()

# print(content)

# content.append(prompt)
# file = open('APP 1/bonus/files/members.txt', 'w')
# file.writelines(content)
# file.close


files = ['a.txt', 'b.txt', 'c.txt']

for i in files:
    f = open(f'APP 1/bonus/files/{i}', 'r')
    content = f.read()
    print(content)
    f.close()
