import numpy as np

def my_dummy_levenshtein_distance(s1, s2):
    """Dummy implementation of the Levenstein distance which results in exponential execution time"""
    if len(s1) == 0 or len(s2) == 0:
        return max(len(s1), len(s2))
    if s1[0] == s2[0]:
        return my_dumy_levenshtein_distance(s1[1:], s2[1:])
    else:
        return 1 + min(my_dumy_levenshtein_distance(s1, s2[1:]), my_dumy_levenshtein_distance(s1[1:], s2), my_dumy_levenshtein_distance(s1[1:], s2[1:]))

def my_dp_levenshtein_distance(s1, s2):
    """Implementation using bottom-up dynamic programming, resulting in O(NM) execution time"""
    distance = np.zeros([len(s1)+1, len(s2)+1])
    for i in range( len(s1)+1):
        for j in range( len(s2)+1):
            if i == 0 or j == 0:
                distance[i, j] = max(i, j)
            elif s1[i-1] == s2[j-1]:
                distance[i, j] = distance[i-1, j-1]
            else:
                distance[i, j] = 1 + min([distance[i, j-1], distance[i-1, j], distance[i-1, j-1]])
    return distance[i,j]
