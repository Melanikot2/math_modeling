import random

flower = ['Трициртис', 'Психотрия возвышенная', 'Каллистемон']
color = ['Цвет звезды в шоке', 'Цвет яйца дрозда', 'Серобуромалиновый', 'Цвет паука, замышляющего преступление', 'Цвет лягушки в обмороке']

color2 = []
for i in range(0, len(color)):
    color2.append(color[random.randint(0, len(color) - 1)])

print(dict(zip(flower, color2)))