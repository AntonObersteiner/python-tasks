def primes_efficient(up_to = 1000):
    is_prime_candidate = list(range(up_to + 1))
    #is_prime_candidate: [0, 1, 2, 3, 4, 5, 6, ...]
    #should become
    #is_prime_candidate: [False, False, 2, 3, False, 5, False, ...]
    if up_to < 2:
        return []

    is_prime_candidate[0] = False #not prime
    is_prime_candidate[1] = False #not prime

    #these don't do anything, just for illustration
    is_prime_candidate[2] #is not False -> remove all multiples
    is_prime_candidate[3] #is not False -> remove all multiples
    is_prime_candidate[4] #should then be False -> ignore
    is_prime_candidate[5] #is not False -> remove all multiples
    is_prime_candidate[6] #should then be False -> ignore

    check_up_to = int(up_to ** .5 + 1) #Wurzel + 1

    for p in range(2, check_up_to):
        #ignore all non-primes
        if is_prime_candidate[p] is not False:
            #remove all multiples
            #from 2 * p to the end, step by p
            for multiple in range(2 * p, up_to, p):
                is_prime_candidate[multiple] = False

    result = []
    for p in range(up_to):
        if is_prime_candidate[p] is not False:
            result += [p]

    return result


# der folgende Code ist nicht so einfach
def not_multiple(n):
    return lambda p: p % n or p == n

def primes_short(up_to = 1000):
    P = list(range(2, up_to + 1))
    if len(P) < 1:
        return P

    index = 0
    #index is separates the numbers
    #   which we know to be primes (P[ : index])
    #from those that are not necessarily primes (P[index : ])
    #the last of the certain primes: P[index - 1]
    #   is used to remove all multiples
    while P[index] < up_to ** .5:
        index += 1
        P = P[ : index] + list(filter(
            not_multiple(P[index - 1]),
            P[index : ]
        ))

    return P
