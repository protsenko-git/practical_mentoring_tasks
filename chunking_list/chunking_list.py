def chunk_list(list_1, chunk_size):
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

