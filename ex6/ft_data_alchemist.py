#!/usr/bin/env python3
import random

init_player_list = [
    'irene',
    'Seulgi',
    'wendy',
    'joy',
    'Yeri',
    'Nayeon',
    'jeongyeon',
    'Jihyo',
    'momo',
    'sana',
    'mina',
    'dahyun',
    'Chaeyoung',
    'Wonhee',
    'tzuyu',
    'Chaeryeong',
    'Karina',
    'Kazuha',
    'Chaewon',
    'Soyeon',
]

print(f"Initial list of players: {init_player_list}")
print()
names_cap = [i.title() for i in init_player_list]
print(f"New list with all names capitalized: {names_cap}")
print()
cap_player_list = [i for i in init_player_list if i == i.title()]
print(f"New list with already capitalized name: {cap_player_list}")
print()
score_dict = {i: random.randint(1, 999) for i in cap_player_list}
print(f"Score dict: {score_dict}")
average = sum(score_dict.values())/len(score_dict)
print(f"Score average is {average:.2f}")
above_avg = {i: score_dict[i] for i in score_dict if score_dict[i] > average}
print(f"High scores:{above_avg}")
