from test_framework import generic_test


def num_combinations_for_final_score(final_score, play_scores):
    combos = [[1] + [0] * final_score for _ in play_scores]
    for i in range(1, final_score + 1):
        for j in range(len(play_scores)):
            x = combos[j-1][i]
            y = combos[j][i - play_scores[j]] if i >= play_scores[j] else 0
            combos[j][i] = x + y
    return combos[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
