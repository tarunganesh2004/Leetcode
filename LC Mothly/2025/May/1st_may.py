# Maximum Number of Tasks You Can Assign LC 2071


from collections import deque

def maxTaskAssign(tasks, workers, pills, strength):
    tasks.sort()
    workers.sort()

    def canFinish(k):
        # top k strength workers finish k weaker tasks (greedy)
        # if any worker fail we cannot complete exact k tasks
        # if less strength worker can finish the some tasks then next high strength worker can also finish
        n = len(workers)
        queue = deque()
        currPills = pills
        tIdx = 0
        for wIdx in range(n - k, n):  # k workers for k tasks
            while tIdx < k and tasks[tIdx] <= workers[wIdx] + strength:
                queue.append(tasks[tIdx])
                tIdx += 1

            # Case 1 : worker cannot finish any task so k workers cannot finish the taks
            if not queue:
                return False

            # Case 2 : worker does not require pill to finish weaker task save the pill
            if queue[0] <= workers[wIdx]:
                queue.popleft()

            # Case 3 : worker require pill
            else:
                if currPills == 0:
                    return False
                currPills -= 1
                queue.pop()
        return True

    res = 0
    l, r = 0, min(len(tasks), len(workers))  # noqa: E741
    while l <= r:
        mid = (l + r) // 2
        if canFinish(mid):
            l = mid + 1  # noqa: E741
            res = mid
        else:
            r = mid - 1
    return res

tasks=[3,2,1]
workers=[0,3,3]
pills=1
strength=1
print(maxTaskAssign(tasks, workers, pills, strength))  # Output: 3