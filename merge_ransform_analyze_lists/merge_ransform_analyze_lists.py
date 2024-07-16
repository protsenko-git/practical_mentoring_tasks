import math


def merge_transform_analyze(*lists: list[int]) -> dict[str, list[int]]:
    grouped_elements = list(zip(*lists))
    results = {
        "sums": [],
        "products": [],
        "maxs": [],
        "mins": [],
    }
    for group in grouped_elements:
        results["sums"].append(sum(group))
        results["mins"].append(min(group))
        results["maxs"].append(max(group))
        results["products"].append(math.prod(group))
    return results


# Test case 1
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

assert merge_transform_analyze(list1, list2, list3) == {
    'sums': [12, 15, 18],
    'products': [28, 80, 162],
    'maxs': [7, 8, 9],
    'mins': [1, 2, 3]
}

# Test case 2
list1 = [-1, 0, 1]
list2 = [-2, 0, 2]
list3 = [-3, 0, 3]

assert merge_transform_analyze(list1, list2, list3) == {
    'sums': [-6, 0, 6],
    'products': [-6, 0, 6],
    'maxs': [-1, 0, 3],
    'mins': [-3, 0, 1]
}

# Test case 3
list1 = []
list2 = []
list3 = []

assert merge_transform_analyze(list1, list2, list3) == {
    'sums': [],
    'products': [],
    'maxs': [],
    'mins': []
}


# Test case 4
list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]

assert merge_transform_analyze(list1, list2, list3) == {
    'sums': [9, 12],
    'products': [15, 48],
    'maxs': [5, 6],
    'mins': [1, 2]
}
