from flask import Flask, render_template
from Utils import SCORES_FILE_NAME
from Utils import BAD_RETURN_CODE as ERROR
from os.path import exists

app = Flask('__main__')


@app.route('/')
def show_score():
    file = SCORES_FILE_NAME
    if exists(file):
        with open(file, 'r', encoding='utf8') as score_file:
            score = score_file.readline()
            return render_template('/my_score.html', game_score=score), 200
    else: 
        return render_template('error.html', error=ERROR), ERROR


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
