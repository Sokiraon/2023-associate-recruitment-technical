def solution():
    total = int(input())
    lines = []
    for i in range(total):
        lines.append(input())
    all_valid = True
    error_codes = []
    for line in lines:
        items = line.split(' ')
        if items[1] == "false":
            all_valid = False
            error_codes.append(items[2])
    if all_valid:
        print("Yes")
    else:
        print("No")
        print(' '.join(error_codes))


if __name__ == '__main__':
    solution()
