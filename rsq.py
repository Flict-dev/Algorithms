def makeprefixsum(data: list):
    prefixsum = [0] * (len(data) + 1)
    for i in range(1, len(data) + 1):
        prefixsum[i] = prefixsum[i - 1] + data[i - 1]
    return prefixsum


def rsq(i, j, data):
    prefixsum = makeprefixsum(data)
    return prefixsum[j] - prefixsum[i]


print(rsq(2, 4, [1, 2, 3, 4, 5]))
