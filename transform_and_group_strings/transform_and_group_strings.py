from collections import defaultdict

def transform_and_group(names: list[str]) -> dict[int, list[str]]:
    grouped_names = defaultdict(list)
    for name in names:
        upper_name = name.upper()
        length = len(upper_name)
        grouped_names[length].append(upper_name)
    return dict(sorted(grouped_names.items()))


# Test case 1
names = ["Alice", "Bob", "Charlie", "Dave"]
assert transform_and_group(names) == {3: ["BOB"], 4: ["DAVE"], 5: ["ALICE"], 7: ["CHARLIE"]}


# Test case 2
name = ["Eve", "Mallory", "Trent", "Oscar"]
assert transform_and_group(name) == {3: ["EVE"], 5: ["TRENT", "OSCAR"], 7: ["MALLORY"]}

# Test case 3
names1 = []
assert transform_and_group(names1) == {}


# Test case 4
names2 = ["A", "BB", "CCC", "DDDD"]
assert transform_and_group(names2) == {1: ["A"], 2: ["BB"], 3: ["CCC"], 4: ["DDDD"]}
