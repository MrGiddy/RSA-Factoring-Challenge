#!/usr/bin/python3

def factors(n):
    for i in range(2, n+1):
        if n % i == 0:
            return int(n/i), i


def main():
    with open(__import__('sys').argv[1], 'r') as f:
        for line in f:
            factor1, factor2 = factors(int(line))
            print(f"{int(line)}={factor1}*{factor2}")

if __name__ == "__main__":
    main()
