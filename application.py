# application.py
from flask import Flask, render_template, request
import random

# Flaskのインスタンス。WSGIアプリケーションオブジェクトは'application'
application = Flask(__name__) 

PRIZES = ["アタリ！", "ハズレ", "もう一度", "参加賞"]

FORTUNES = ["大吉", "吉", "中吉", "小吉", "凶"]

# 占い結果ごとのポエム（お告げ）
FORTUNE_POEMS = {
    "大吉": "新しい風があなたに幸運を運びます。<br>迷わず進めば、道は必ず開けるでしょう。",
    "吉": "小さな幸せが積み重なり、大きな喜びとなる日です。<br>感謝の気持ちを忘れずに。",
    "中吉": "努力が実を結ぶタイミング。<br>焦らず、着実に歩みましょう。",
    "小吉": "周囲との調和を大切に。<br>穏やかな心が運気を呼び込みます。",
    "凶": "休息も大切な一歩。<br>無理せず、心身を整える時間にしましょう。"
}

@application.route('/', methods=['GET', 'POST'])
def index():
    # 簡易的な会員フラグ（本来はセッション/DBで管理）
    membership = False
    if request.method == 'POST':
        result = random.choice(PRIZES)
        fortune = random.choice(FORTUNES)
        poem = FORTUNE_POEMS.get(fortune, "")
        return render_template('index.html', result=result, fortune=fortune, poem=poem, membership=membership)
    else:
        return render_template('index.html', result=None, fortune=None, poem=None, membership=membership)

if __name__ == "__main__":
    # Elastic Beanstalkではこのブロックは無視されますが、ローカルテスト用として残します。
    application.run(debug=True)