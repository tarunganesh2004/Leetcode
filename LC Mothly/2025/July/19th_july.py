# Remove Sub-Folders From the File System LC 1233

folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]

def removeSubfolders(folder):
    folder.sort()
    res=[folder[0]]

    for i in range(1, len(folder)):
        last=res[-1]+'/'
        if not folder[i].startswith(last):
            res.append(folder[i])
    return res

print(removeSubfolders(folder))  # Output: ['/a', '/c/d', '/c/f']