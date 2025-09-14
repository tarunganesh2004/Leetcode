# Sort Vowels in a String LC 2785

s="lEetcOde"

def sortVowels(s):
    vowels = 'aeiouAEIOU'
    vowel_chars = sorted([c for c in s if c in vowels])
    result = []
    vowel_index = 0

    for char in s:
        if char in vowels:
            result.append(vowel_chars[vowel_index])
            vowel_index += 1
        else:
            result.append(char)

    return ''.join(result)

print(sortVowels(s))