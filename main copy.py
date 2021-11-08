import random
import plotly.figure_factory as ff

dice_list = []
count = []

num = 0

while num <= 100:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_list.append(dice1 + dice2)
    count.append(num)
    num += 1

# print(count, dice_list)

bar_graph = ff.create_distplot([dice_list], ['result'])
bar_graph.show()