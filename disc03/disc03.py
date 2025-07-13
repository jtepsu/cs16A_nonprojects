# Q1
def swipe(n):
    if n >= 10:
        print(n % 10)
        swipe(n // 10)
        print(n % 10)
    else:
        print(n)

# Q2
def skip_factorial(n):
    if n <= 2:
        return n
    else:
        return n * skip_factorial(n - 2)

# Q3
def is_prime(n):    
    "checks whether n can be evenly divided by any number between 1 and n"
    def f(i):        
        if n % i == 0:            
            return False        
        elif n - i == 1:            
            return True        
        else:            
            return f(i + 1)    
    return f(2)

# Q4
def hailstone(n):
    steps = 1
    print(int(n))
    if n % 2 == 0:
        steps += hailstone(n / 2)
    elif n > 1:
        steps += hailstone((n * 3) + 1)
    return steps


# Q5
def has_seven(n):
    if n < 7:
        return False
    elif n % 7 == 0:
        return True
    else:
        while n >= 7:
            if n % 10 == 7:
                return True
            n = n // 10
        return False

def sevens(n, k):

    def play(i=1, who=1, direction=1):
        print(f"Player {who} says {i}")
        if i < n:
            if has_seven(i + 1):
                direction = direction * (-1)
            if (who + direction) > k:
                return play(i+1, 1, direction)
            elif (who + direction) == 0:
                return play(i+1, k, direction)
            else:
                return play(i+1, who + direction, direction)
        else:
            return who
        
    return play()
        

