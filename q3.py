import number_lists

num_dict = {"0": number_lists.zero, "1": number_lists.one, "2": number_lists.two,
            "3": number_lists.three, "4": number_lists.four, "5": number_lists.five,
            "6": number_lists.six, "7": number_lists.seven, "8": number_lists.eight, "9": number_lists.nine}


def draw_canvas(canvas_in):
    for X in canvas_in:
        for Y in X:
            print(Y, end="")
        print()


cin = list(map(int, (input().split(','))))
cin.insert(1, 0)
number_of_digits = len(str(cin[0]))
sum_of_spaces = sum(cin[3::2])
width_of_canvas = sum_of_spaces + 4*number_of_digits
height_of_canvas = max(cin[2::2]) + 5
canvas = [[" " for width in range(width_of_canvas)] for height in range(height_of_canvas)]

numbers = str(cin[0])
x_pointer = 0
y_pointer = 0
xcor = 0
ycor = 0

for i, number in enumerate(numbers):
    num_draw = num_dict[number]
    xcor += x_pointer + cin[2*i+1]
    ycor = cin[2*i+2]
    num_draw_list = list(map(list, num_draw))

    for x_offset, line in enumerate(num_draw_list):
        for y_offset, letter in enumerate(line):
            canvas[ycor+x_offset][xcor+y_offset] = letter
    if number == '1':
        x_pointer = 1
    else:
        x_pointer = 4

f = open('out3.txt', 'w')
for line in canvas:
    f.write("".join(line) + "\n")
f.close()



