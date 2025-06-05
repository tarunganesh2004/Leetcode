# Lexicographically Smallest Equivalent String LC 1061

s1="parker"
s2="morris"
baseStr="parser"

def smallestEquivalentString(s1, s2, baseStr):
    parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for a, b in zip(s1, s2):
        rootA, rootB = find(a), find(b)
        if rootA < rootB:
            parent[rootB] = rootA
        else:
            parent[rootA] = rootB

    return ''.join(find(c) for c in baseStr)

print(smallestEquivalentString(s1, s2, baseStr))  # Output: "makkek"