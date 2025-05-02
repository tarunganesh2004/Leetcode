# Push Dominoes LC 838

dominoes= "RR.L"

def pushDominoes(dominoes):
    n = len(dominoes)
    dominoes = list(dominoes)
    l = 0  # noqa: E741
    r = 0

    while l < n:
        while r < n and dominoes[r] == '.':
            r += 1

        if l == r:
            l += 1  # noqa: E741
            r += 1
            continue

        if r == n:
            break

        if dominoes[l] == dominoes[r]:
            for i in range(l, r):
                dominoes[i] = dominoes[l]
        elif dominoes[l] == 'R' and dominoes[r] == 'L':
            for i in range(l + 1, r):
                dominoes[i] = '.'
        else:
            for i in range((l + r) // 2, (l + r) // 2 + 1):
                dominoes[i] = '.'

        l = r + 1  # noqa: E741
        r = l

    return ''.join(dominoes)

print(pushDominoes(dominoes))  # Output: "RR.L"