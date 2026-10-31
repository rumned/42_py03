#!/usr/bin/env python3
import random


def gen_player_achievements() -> set[str]:
    num_achv = random.randint(1, len(title_list))
    return set(random.sample(title_list, num_achv))


title_list = [
    'Mastermind',
    'Philanthropist',
    'Hackerman',
    'The Answer',
    'Dragonduck',
    'Rigorous Basterd',
    'Enlightened',
    'Pentester',
    'Perfectionist',
    'Pioneer'
]

player_list = [
    'Yeri',
    'Kazuha',
    'Chaewon',
    'Karina'
]

player_titles_list = []

if __name__ == '__main__':
    for player in player_list:
        player_titles_list.append(gen_player_achievements())

    gained_achv = set().union(*player_titles_list)
    shared_achv = set.intersection(*player_titles_list)
    title_set = set().union(title_list)

    print("=== Achievement Tracker System ===")
    print()
    for i in range(len(player_list)):
        print(f"Player {player_list[i]}: {player_titles_list[i]}\n")
    print(f"\nAll distinct achievements: {gained_achv}\n")
    print(f"Common achievements: {shared_achv}\n")

    for i in range(len(player_list)):
        others: set[str] = set()
        for j in range(len(player_list)):
            if j != i:
                others = others.union(player_titles_list[j])
        print(f"Only {player_list[i]} has:",
              f"{player_titles_list[i].difference(others)}")
    print()
    for i in range(len(player_list)):
        print(f"{player_list[i]} is missing:",
              f"{title_set.difference(player_titles_list[i])}")
