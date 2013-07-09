## Task 2
def dict2list(dct, keylist): return [ dct[k] for k in keylist ]

def list2dict(L, keylist): return { k:v  for (k,v) in zip(keylist,L) }

## Task 3
def listrange2dict(L):
    """
    Input: a list
    Output: a dictionary that, for i = 0, 1, 2, . . . , len(L), maps i to L[i]

    You can use list2dict or write this from scratch
    """
    return {i:L[i] for i in range(len(L))}

