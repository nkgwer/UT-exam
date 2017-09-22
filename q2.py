import number_lists

num_list = [number_lists.zero, number_lists.one, number_lists.two, number_lists.three,
            number_lists.four, number_lists.five, number_lists.six, number_lists.seven,
            number_lists.eight, number_lists.nine]


def search_for_num(lst):
    for i, num in enumerate(num_list):
        if num[0] == lst[0] and num[1] == lst[1] and num[2] == lst[2] and num[3] == lst[3] and num[4] == lst[4]:
            return i
    print("Something went wrong")
    return


f = open("out1.txt", "r")

xin = []

for row in f:
    xin.append(row)

xin = list(map(list, zip(*xin)))
position = 0
buff = []
x_len = len(xin)
ret = ""
while position < x_len:
    if xin[position][0] == " " and xin[position][2] == " " or xin[position][0] == "\n":
        buff = list(map(list, zip(*buff)))
        for index, strings in enumerate(buff):
            buff[index] = "".join(buff[index])
        ret += str(search_for_num(buff))
        buff = []
        position += 1
        continue
    buff.append("".join(xin[position]))
    position += 1

print(ret)
