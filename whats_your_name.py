# HackerRank Problem: What's Your Name?
# Language: Python
# Author: Abrham

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input().strip()
    last_name = input().strip()
    print_full_name(first_name, last_name)
