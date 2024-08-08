import random


def solution():
    data = []
    for i in range(5):
        result = ''.join(str(random.randint(0, 9)) for _ in range(8))
        data.append(result)
    data = [number.replace("5", "6") for number in data]

    with open('test.txt', 'w') as file:
        file.write('\n'.join(data))


if __name__ == '__main__':
    solution()




