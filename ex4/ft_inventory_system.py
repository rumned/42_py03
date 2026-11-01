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
        except Exception as e:
            print(f"Error: invalid input at item {input_order} -- "
                  f"{e}")
            has_exception = True
            continue
        if name in inv:
            print(f'Redundant item {name} - discarding')
            continue
        inv[name] = qty
    if len(sys.argv) == 1:
        print("No items received.")
        print("Each parameter must follow this format:",
              "<item_name>:<quantity>\n")
    elif has_exception is True:
        print("Each parameter must follow this format:",
              "<item_name>:<quantity>\n")
    print(f"Inventory: {inv}")
    return inv


def display_stats(inv: dict[str, int]) -> None:
    if not inv:
        return
    item_keys = list(inv.keys())
    item_vals = sum(inv.values())
    print(f"Item list: {item_keys}")
    print(f"Total quantity of the {len(item_keys)}",
          f"items: {item_vals}")
    for name in inv:
        qty = inv[name]
        print(f"Item {name} represents",
              f"{(qty/item_vals * 100):.2f}%")
    item_keys.sort(key=lambda item: inv[item])
    most = item_keys[-1]
    least = item_keys[0]
    print(f"Item most abundant: {most}",
          f"with quantity {inv[most]}")
    print(f"Item least abundant: {least}",
          f"with quantity {inv[least]}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    print()
    inv = parse_cli()
    display_stats(inv)
    inv['sayur'] = 1
    print(f"Updated inventory: {inv}")
