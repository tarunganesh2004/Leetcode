# Find the Kth-Character in the String Game I LC 3304

k=5

def kthCharacter(k):
    return chr(97+(k-1).bit_count())

print(kthCharacter(k))  