from typing import Generator


def fibonacci_generator(l: int) -> Generator[int, str, None]:
    x, y = 0, 1
    while True:
        command = yield x
        if command == "RESET":
            x, y = 0, 1
        x, y = y, x + y
        if x >= l:
            break

gen = fibonacci_generator(100)
for i in gen:
    print(i)
    if i == 89:
        gen.send("RESET")
