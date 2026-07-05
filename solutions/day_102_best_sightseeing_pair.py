def max_score_sightseeing_pair(values):
    best = 0
    best_i = values[0]
    for j in range(1, len(values)):
        best = max(best, best_i + values[j] - j)
        best_i = max(best_i, values[j] + j)
    return best