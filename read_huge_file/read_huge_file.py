from typing import Generator


def read_large_file(file_path: str) -> Generator[str, None, None]:
    with open(file_path, "r") as file:
        while True:
            data = file.read(1024 * 1024)
            if not data:
                break
            yield data
