# LC 2182 
import heapq
from collections import Counter


def repeatLimitedString(s,repeatLimit ) :
    # Count the frequency of each character
    count = Counter(s)

    # Create a max-heap using negative ASCII values to maintain order
    max_heap = [(-ord(c), cnt) for c, cnt in count.items()]
    heapq.heapify(max_heap)

    res = []

    while max_heap:
        # Step 1: Pop the most frequent character
        char, cnt = heapq.heappop(max_heap)
        char = chr(-char)  # Convert back to character

        # Append up to 'repeatLimit' occurrences of the character
        cur_cnt = min(cnt, repeatLimit)
        res.append(char * cur_cnt)

        # Step 2: Handle leftover occurrences of the character
        if cnt - cur_cnt > 0:
            # Check if there's another character in the heap
            if max_heap:
                # Pop the next character
                nxt_char, nxt_cnt = heapq.heappop(max_heap)
                nxt_char = chr(-nxt_char)

                # Append one occurrence of the next character
                res.append(nxt_char)

                # Push the remaining count of the next character back into the heap
                if nxt_cnt - 1 > 0:
                    heapq.heappush(max_heap, (-ord(nxt_char), nxt_cnt - 1))

                # Push the leftover occurrences of the current character back into the heap
                heapq.heappush(max_heap, (-ord(char), cnt - cur_cnt))
            else:
                # No other character left, break to avoid infinite loop
                break

    return "".join(res)


s="cczazcc"
repeatLimit=3
print(repeatLimitedString(s,repeatLimit)) # zzccac