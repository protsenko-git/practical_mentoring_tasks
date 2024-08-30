from typing import Generator


def read_large_file(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()
