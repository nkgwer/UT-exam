import number_lists

xin = input()
answer = ["","","","",""]
num_dict = {"0": number_lists.zero, "1": number_lists.one, "2": number_lists.two,
            "3": number_lists.three, "4":number_lists.four, "5": number_lists.five,
            "6": number_lists.six, "7": number_lists.seven, "8": number_lists.eight, "9": number_lists.nine}

for num in xin:
    for row in range(5):
        answer[row] += num_dict[num][row] + " "

f = open('out1.txt', 'w')
for line in answer:
    f.write(line+"\n")
f.close()
