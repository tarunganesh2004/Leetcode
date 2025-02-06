# Reverse Words in a String LC 151

s="the sky is blue"

def reverseWords(s):
    # return " ".join(s.split()[::-1]) single line solution

    # split the string
    s=s.split()
    # reverse the list
    s=s[::-1]
    # join the list
    s=" ".join(s)
    return s

print(reverseWords(s))