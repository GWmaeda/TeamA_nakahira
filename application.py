# application.py
from flask import Flask, render_template, request
import random
# タロットカード（大アルカナ22枚）と意味
TAROT_CARDS = [
    {"name": "愚者", "meaning": "自由、冒険、無限の可能性"},
    {"name": "魔術師", "meaning": "創造、意志、始まり"},
    {"name": "女教皇", "meaning": "直感、知恵、神秘"},
    {"name": "女帝", "meaning": "豊かさ、母性、成長"},
    {"name": "皇帝", "meaning": "支配、安定、責任"},
    {"name": "法王", "meaning": "伝統、信仰、助言"},
    {"name": "恋人", "meaning": "選択、愛、調和"},
    {"name": "戦車", "meaning": "勝利、意志、前進"},
    {"name": "力", "meaning": "勇気、忍耐、内なる力"},
    {"name": "隠者", "meaning": "探求、孤独、内省"},
    {"name": "運命の輪", "meaning": "転機、幸運、変化"},
    {"name": "正義", "meaning": "公平、バランス、正義"},
    {"name": "吊るされた男", "meaning": "犠牲、視点の転換、忍耐"},
    {"name": "死神", "meaning": "終わり、再生、変容"},
    {"name": "節制", "meaning": "調和、節度、癒し"},
    {"name": "悪魔", "meaning": "誘惑、束縛、執着"},
    {"name": "塔", "meaning": "崩壊、衝撃、解放"},
    {"name": "星", "meaning": "希望、癒し、インスピレーション"},
    {"name": "月", "meaning": "不安、幻想、直感"},
    {"name": "太陽", "meaning": "成功、喜び、活力"},
    {"name": "審判", "meaning": "覚醒、決断、再生"},
    {"name": "世界", "meaning": "完成、達成、統合"}
]

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
        tarot = random.choice(TAROT_CARDS)
        tarot_card = tarot["name"]
        tarot_meaning = tarot["meaning"]
        return render_template('index.html', result=result, fortune=fortune, poem=poem, membership=membership, tarot_card=tarot_card, tarot_meaning=tarot_meaning)
    else:
        return render_template('index.html', result=None, fortune=None, poem=None, membership=membership, tarot_card=None, tarot_meaning=None)

@application.route('/weekly')
def weekly():
    tarot = random.choice(TAROT_CARDS)
    tarot_card = tarot["name"]
    tarot_meaning = tarot["meaning"]
    weekly_messages = [
        "今週は新しい挑戦に最適なタイミング。直感を信じて行動しましょう。",
        "人間関係に変化が訪れる予感。柔軟な心で受け入れて。",
        "小さな幸せを大切に。焦らず一歩ずつ進むことで運気が上昇します。",
        "過去の経験が今週のヒントに。自分を信じて前進しましょう。",
        "休息も大切な運気アップの鍵。無理せずリフレッシュを。"
    ]
    weekly_message = random.choice(weekly_messages)
    shiitake_advices = [
        "今週は、あなたの“やさしさ”が周りに伝わる時です。無理せず、心の声に耳を傾けてみてください。",
        "自分を責めず、できることから始めてみましょう。小さな一歩が大きな変化につながります。",
        "あなたの“好き”を大切に。周囲の期待よりも、自分の気持ちを優先してOKです。",
        "疲れた時は、好きな香りや色でリラックスを。自分を癒す時間を持ちましょう。",
        "今週は“受け入れる”ことがテーマ。新しい出会いや出来事も、やさしく受け止めてみて。"
    ]
    shiitake_advice = random.choice(shiitake_advices)
    return render_template('weekly.html', tarot_card=tarot_card, tarot_meaning=tarot_meaning, weekly_message=weekly_message, shiitake_advice=shiitake_advice)

if __name__ == "__main__":
    # Elastic Beanstalkではこのブロックは無視されますが、ローカルテスト用として残します。
    application.run(debug=True)
    application.run(debug=True)