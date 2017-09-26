import number_lists

list_of_numbers = [number_lists.one, number_lists.two, number_lists.three,
                   number_lists.four, number_lists.five, number_lists.six, number_lists.seven,
                   number_lists.eight, number_lists.nine, number_lists.zero]
list_of_numbers = list(map(list, list_of_numbers))
f = open("out3.txt", "r")
xin = []
for row in f:
    xin.append(list(row)[:-1])
print(list_of_numbers)

