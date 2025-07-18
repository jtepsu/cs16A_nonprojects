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
    def build_list(k, j, kList):
        result = []
        if k > m:
            return result
        if j > m:
            return result.append(build_list(k+1, 1, kList))
        if kList is None:
            kList = []
        if sum(kList) + j <= n - k:
            newKList = kList.append(j)
            if sum(kList) == n:
                result.append([k] + newKList)
                result.append(build_list(k+1, j, newKList))
            else:
                result.append(build_list(k, 1, newKList))
            result.append(build_list(k, j+1, kList))
        else:
            result.append(build_list(k+1, 1, kList))
        return result
    return build_list(1, 1, [])
# doesn't work
# RecursionError: maximum recursion depth exceeded in comparison
            

