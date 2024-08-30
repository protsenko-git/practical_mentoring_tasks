import argparse
from custom_hashmap import HashMap


def main():
    parser = argparse.ArgumentParser(description='HashMap Implementation.')
    parser.add_argument('--size', type=int, default=10, help='Initial size of the HashMap')
    args = parser.parse_args()

    with HashMap(size=args.size) as hash_map:
        hash_map.insert("planet", "Earth")
        hash_map.insert("country", "Ukraine")
        hash_map.insert("region", "Lvivska")
        hash_map.insert("city", "Lviv")
        hash_map.insert("street", "Zamknena")

        print(hash_map.get("planet"))
        print(hash_map.get("country"))
        print(hash_map.get("region"))
        print(hash_map.get("city"))
        print(hash_map.get("street"))


if __name__ == "__main__":
    main()
