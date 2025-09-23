# Compare Version Numbers LC 165

version1="1.01"
version2="1.001"

def compareVersion(version1, version2):
    v1=version1.split('.')
    v2=version2.split('.')
    n1=len(v1)
    n2=len(v2)
    for i in range(max(n1,n2)):
        num1=int(v1[i]) if i<n1 else 0
        num2=int(v2[i]) if i<n2 else 0
        if num1>num2:
            return 1
        elif num1<num2:
            return -1
    return 0

print(compareVersion(version1,version2))