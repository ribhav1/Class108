import random
import plotly_express as px

dice_list = []
count = []

num = 0

while num <= 100:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_list.append(dice1 + dice2) 
    count.append(num)
    num += 1

print(count, dice_list)

bar_graph = px.bar(x=dice_list, y=count)
bar_graph.show()