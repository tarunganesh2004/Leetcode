# H-Index

citations=[5,1,2,4,1]

def find_Index_Brute(citations):
    citations.sort(reverse=True)
    h_index=0

    for i in range(len(citations)):
        if i+1<=citations[i]:
            h_index=i+1
        
    return h_index

print(find_Index_Brute(citations))