# Vowel Spellchecker LC 966

wordList=["KiTe","kite","hare","Hare"]
queries=["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]

def spellchecker(queries, wordList):
    def devowel(word):
        return ''.join('*' if c in 'aeiou' else c for c in word.lower())

    exact_words = set(wordList)
    case_insensitive = {}
    vowel_error = {}

    for word in wordList:
        lower_word = word.lower()
        if lower_word not in case_insensitive:
            case_insensitive[lower_word] = word
        devoweled_word = devowel(word)
        if devoweled_word not in vowel_error:
            vowel_error[devoweled_word] = word

    result = []
    for query in queries:
        if query in exact_words:
            result.append(query)
        elif query.lower() in case_insensitive:
            result.append(case_insensitive[query.lower()])
        elif devowel(query) in vowel_error:
            result.append(vowel_error[devowel(query)])
        else:
            result.append("")

    return result

print(spellchecker(queries, wordList))