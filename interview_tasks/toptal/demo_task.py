# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

def solution(A):
    # write your code in Python 3.6
    A2 = sorted(list(set(filter(lambda x: x> 0 , A))))
    if len(A2) == 0 or A2[0] > 1:
        return 1
    for i in range(1, len(A2)):
        if A2[i]- A2[i-1] > 1:
            return A2[i-1] + 1
    return A2[-1] + 1