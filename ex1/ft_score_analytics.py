#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    score_list: list[int] = []
    i = 0
    j = 1
    args_len = len(sys.argv)
    while args_len > 1:
        try:
            score_list.append(int(sys.argv[j]))
        except Exception:
            print(f"Invalid parameter: \'{sys.argv[j]}\'")
        i += 1
        j += 1
        args_len -= 1
    if len(score_list) == 0:
        print("No scores provided.", end=" ")
        print("Usage: python3 ft_score_analytics.py <score1> ,<score2> ...")
    else:
        print(f"Scores processed: {score_list}")
        print(f"Total players: {len(score_list)}")
        print(f"Total score: {sum(score_list)}")
        print(f"Average score: {sum(score_list) / len(score_list)}")
        print(f"High score: {max(score_list)}")
        print(f"Low score: {min(score_list)}")
        print(f"Score range: {max(score_list) - min(score_list)}")
