# Max Difference You Can Get From Changing an Integer LC 1432

num=555

def maxDiff(num):
    # finding the max number and min number
    min_num,max_num= str(num), str(num)

    for d in max_num:
        if d != '9':
            max_num = max_num.replace(d, '9')
            break

    # replace the most significant bit with '1'
    for i,d in enumerate(min_num):
        if i==0:
            if d!="1":
                min_num = min_num.replace(d, '1')
                break
        else:
            if d!= '0' and d!=min_num[0]:
                min_num = min_num.replace(d, '0')
                break
    return int(max_num) - int(min_num)

print(maxDiff(num))  # Output: 888