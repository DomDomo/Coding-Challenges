import itertools as it
def choose_best_sum(t, k, ls):
    combos = list(it.combinations(ls, k))
    distances = []
    for i in range(len(combos)):
        if sum(combos[i]) not in distances:
            distances.append(sum(combos[i]))
    distances.sort()
    distances.reverse()
    for i in range(len(distances)):
        if distances[i] <= t:
            return distances[i]
    return