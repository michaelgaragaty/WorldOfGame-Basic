from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    scores = open(SCORES_FILE_NAME, 'a')
    scores.close()

    with open(SCORES_FILE_NAME, 'r', encoding='utf8') as my_cur_score:
        current_score = my_cur_score.readline()

    with open(SCORES_FILE_NAME, 'w', encoding='utf8') as new_cur_score:
        POINTS_OF_WINNING = (difficulty * 3) + 5
        print(POINTS_OF_WINNING)
        if current_score == '':
            new_score = 0 + POINTS_OF_WINNING
            total_score = new_cur_score.write(str(new_score))
        else:
            new_score = int(current_score) + POINTS_OF_WINNING
            total_score = new_cur_score.write(str(new_score))
        return total_score
