#!/usr/bin/env python3
import sys


def parse_cli() -> dict[str, int]:
    has_exception = False
    inv = {}
    input_order = 0
    for arg in sys.argv[1:]:
        input_order += 1
        try:
            name, qty_str = arg.split(':')
            qty: int = int(qty_str)
        except ValueError:
            print(f"Error: invalid input at item {input_order}")
            has_exception = True
            continue
        if name in inv:
            print(f'Redundant item {name} - discarding')
            continue
        inv[name] = qty
    if len(sys.argv) == 1 or has_exception:
        print("Each parameter must follow this format:",
              "<item_name>:<quantity>")
    print(inv)
    return inv


if __name__ == "__main__":
    parse_cli()
