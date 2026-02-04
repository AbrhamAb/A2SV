def watermelon(weight):
    if weight > 2 and weight % 2 == 0:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    print(watermelon(int(input().strip())))
