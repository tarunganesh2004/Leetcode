# LC 2070

items = [
    [193, 732],
    [781, 962],
    [864, 954],
    [749, 627],
    [136, 746],
    [478, 548],
    [640, 908],
    [210, 799],
    [567, 715],
    [914, 388],
    [487, 853],
    [533, 554],
    [247, 919],
    [958, 150],
    [193, 523],
    [176, 656],
    [395, 469],
    [763, 821],
    [542, 946],
    [701, 676],
]
queries = [
    885,
    1445,
    1580,
    1309,
    205,
    1788,
    1214,
    1404,
    572,
    1170,
    989,
    265,
    153,
    151,
    1479,
    1180,
    875,
    276,
    1584,
]

def maxBeauty(items,queries):
    items.sort()
    sorted_queries=sorted(enumerate(queries),key=lambda x:x[1])
    # print(sorted_queries)

    max_beauty=0
    res=[0]*len(queries)
    j=0

    for idx,max_price in sorted_queries:
        while j<len(items) and items[j][0]<=max_price:
            max_beauty=max(max_beauty,items[j][1])
            j+=1
        
        res[idx]=max_beauty
    return res


print(maxBeauty(items,queries))