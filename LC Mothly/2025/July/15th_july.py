# Valid Word LC 3136

word="234Adas"

def isValid(word):
    if len(word)<3:
        return False
    
    has_vowel= False
    has_consonant = False

    for c in word:
        if c.isalpha():
            if c.lower() in "aeiou":
                has_vowel = True
            else:
                has_consonant = True
        elif not c.isdigit():
            return False
    return has_vowel and has_consonant


print(isValid(word))  # Output: True