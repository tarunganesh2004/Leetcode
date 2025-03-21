# Find All Possible Recipes from given supplies LC 2115

recipes=["bread"]
ingridents=[["yeast","flour"]]
supplies=["yeast","flour","corn"]

def findAllRecipes(recipes,ingridents,supplies):
    from collections import deque
    ans=[]
    seen=set(supplies)

    dq=deque([(r,ing) for r,ing in zip(recipes,ingridents)])

    prev_size=len(seen)-1
    while len(seen)>prev_size:
        prev_size=len(seen)
        for _ in range(len(dq)):
            recipe,ingridents=dq.popleft()
            if all(ing in seen for ing in ingridents):
                ans.append(recipe)
                seen.add(recipe)
            else:
                dq.append((recipe,ingridents))

    return ans

print(findAllRecipes(recipes,ingridents,supplies))