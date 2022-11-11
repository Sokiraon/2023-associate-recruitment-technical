def size_transform(size):
    if size == "S":
        return 0
    elif size == "M":
        return 1
    elif size == "L":
        return 2
    elif size[-1] == "S":
        return 1 - len(size)
    else:
        return 1 + len(size)


def solution():
    data = []
    for i in range(4):
        data.append(input())
    sizes = data[1].split(' ')
    sizes = [size_transform(size) for size in sizes]
    sizes.sort()
    requires = data[-1].split(' ')
    requires = [size_transform(require) for require in requires]
    i = 0
    while True:
        target = requires[i]
        if sizes[-1] < target:
            break
        else:
            index = 0
            while sizes[index] < target:
                index += 1
            sizes.pop(index)
            i += 1
        if i == len(requires):
            return "Yes"
    return "No"


if __name__ == '__main__':
    print(solution())
