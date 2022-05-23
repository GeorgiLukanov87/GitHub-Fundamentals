string = input()
testing = []
while not string == 'End':
    testing.append(string)
    string = input()

for word in testing:
    if word == 'SoftUni':
        testing.remove(word)

result_list = []
word = ""

for element in testing:
    for letter in element:
        word += letter * 2
    result_list.append(word)
    word = ""

for element in result_list:
    print(element)


