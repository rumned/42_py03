#!/usr/bin/env python3
import typing
import random


player_list = [
    'Karina',
    'Chaewon',
    'Yeri',
    'Kazuha',
]

action_list = [
    'Sing',
    'Dance',
    'Beatbox',
    'Aegyo',
    'Livestream',
    'Eat',
    'Drink',
    'Sleep',
]

Generator = typing.Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(player_list)
        action = random.choice(action_list)
        yield (name, action)


def consume_event(
    rand_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while rand_list:
        picked = random.choice(rand_list)
        rand_list.remove(picked)
        yield picked


if __name__ == '__main__':
    gen = gen_event()
    i = 1
    while i <= 1000:
        print(f"Event no: {i}",
              f"{next(gen)[0]} is doing {next(gen)[1]}ing")
        i += 1

    pl_ev_tuple_list = []
    for j in range(1, 11):
        pl_ev_tuple_list.append(next(gen))
    print(f"Built a list of 10 events: {pl_ev_tuple_list}")
    consume = consume_event(pl_ev_tuple_list)
    for k in consume:
        print(f"Got event from list: {k}")
        print(f"Remains in list: {pl_ev_tuple_list}")
