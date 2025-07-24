# tree

def tree(label, branches=[]):    
    for branch in branches:        
        assert is_tree(branch), 'branches must be trees'    
    return [label] + list(branches)

def label(tree):    
    return tree[0]

def branches(tree):   
    return tree[1:]

def is_leaf(tree):    
    return not branches(tree)

def is_tree(tree):    
    if type(tree) != list or len(tree) < 1:        
        return False    
    for branch in branches(tree):        
        if not is_tree(branch):            
            return False    
    return True

t2 = tree(5, [tree(6), tree(7)])
t1 = tree(3, [tree(4), t2])


# Q2: has path
def has_path(t, p):
    if label(t) == p[0]:
        if len(p) > 1:
            if not is_leaf(t):
                return has_path(branches(t)[0], p[1:]) or has_path(branches(t)[1], p[1:])
            else:
                return False
        else:
            return True
    else:
        return False
#print(has_path(t1, [3, 5, 6]))

# Q3: find path
def find_path(t, x):
    if label(t) != x:
        if is_leaf(t):
            return None
        else:
            for i in branches(t):
                path = find_path(i, x)
                if path is not None:
                    return [label(t)] + path
    else:
        return [label(t)]
    return None

#print(find_path(t1, 7))
    