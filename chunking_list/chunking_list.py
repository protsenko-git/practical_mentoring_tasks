def chunk_list(list_1: list, chunk_size: int) -> list[list]:
    chunks = []
    chunk = []
    for index, item in enumerate(list_1):
        chunk.append(item)
        if (index + 1) % chunk_size == 0:
            chunks.append(chunk)
            chunk = []
    if chunk:
        chunks.append(chunk)

    return chunks

# Test case 1
items1 = ['a', 'b', 'c', 'd', 'e', 'f']
chunk_size1 = 2
assert chunk_list(items1, chunk_size1) == [['a', 'b'], ['c', 'd'], ['e', 'f']]

# Test case 2
items = [1, 2, 3, 4, 5]
chunk_size = 3
assert chunk_list(items, chunk_size) == [[1, 2, 3], [4, 5]]

# Test case 3
items2 = []
chunk_size2 = 1
assert chunk_list(items2, chunk_size2) == []

# Test case 4
items3 = ['apple', 'banana', 'cherry']
chunk_size3 = 1
assert chunk_list(items3, chunk_size3) == [['apple'], ['banana'], ['cherry']]




