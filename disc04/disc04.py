# Q1: Insect Combinatorics​
def paths(m, n):
    def insect(lm, ln):
        if [lm, ln] == [m, n]:
            return 1
        elif lm == m:
            return insect(lm, ln+1)
        elif ln == n:
            return insect(lm+1, ln)
        else:
            return insect(lm+1, ln) + insect(lm, ln+1)
    return insect(1, 1)


# Q2: Max Product​
def max_product(numlist=[]):
    for element in numlist:
        assert element > 0 and type(element) == int
    def find_max(i=0, currentMax=0):
        if (len(numlist) - 2) == i:
            return currentMax
        else:
            for j in range(i+2, len(numlist), 2):
                currentMax = max(currentMax, numlist[i] * numlist[j])
        return max(currentMax, find_max(i+1, currentMax))
    return find_max(0, 0)

# Q3: Sum Fun​

def sums(n, m):
    def build_list(k, j, kList, result):
        if k > m:
            return result
        if j > m:
            return result + (build_list(k+1, 1, [], result))
        if kList == [] and k == j:
            build_list(k, j+1, [], result)
        else:
            if sum(kList) + j <= n - k:
                if (kList == [] and k != j) or j != kList[-1]:
                    newKList = kList + [j]
                    if sum(newKList) == n - k:
                        result.append([k] + newKList)
                    else:
                        build_list(k, 1, newKList, result)
                build_list(k, j+1, kList, result)
            else:
                build_list(k+1, 1, kList, result)
        return result
    return build_list(1, 1, [], [])

print(sums(5, 3))

# almost works
# test case fails: first element of output list is [2, 2, 1] for some reason
            

