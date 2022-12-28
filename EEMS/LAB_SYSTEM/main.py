from tkinter.font import nametofont
from flask import Flask, render_template, request
import sqlite3
import get_calendar
import getData
import numpy as np

#各部屋のブッキング回避未実装

#Flaskオブジェクトの生成
app = Flask(__name__)

def get_db(g):
    name = g
    dbname = 'C:/Users/hayat/Downloads/nyutaishitu/nyutaishitu/nyutaishitu/EEMS/LAB_SYSTEM/main.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    a = []
    for row in cur.execute('SELECT * FROM user'):
        if name == row[0]:
            cur.close()
            conn.close()
            return row[1],row[2]
    cur.close()
    conn.close()
    return "unknown", 1

def get_db_ver2(g):
    userdata = g
    dbname = 'C:/Users/hayat/Downloads/nyutaishitu/nyutaishitu/nyutaishitu/EEMS/LAB_SYSTEM/main.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    a = []
    for row in cur.execute('SELECT * FROM user'):
        if userdata == row[1]:
            cur.close()
            conn.close()
            return row[1],row[2]
    cur.close()
    conn.close()
    return "unknown", 1

def update_image(mail, avatar):
    #avatar = int(avatar)
    dbname = 'C:/Users/hayat/Downloads/nyutaishitu/nyutaishitu/nyutaishitu/EEMS/LAB_SYSTEM/main.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    str_spl = 'UPDATE user SET image = '+avatar+' WHERE mail = "'+mail+'"'
    print(str_spl)
    cur.execute(str_spl)
    conn.commit()
    cur.close()
    conn.close()

def calendar():
    g= get_calendar.main()
    g_new = []

    for i in g:
        g_tmp = []
        if i == []:
            g_new.append(g_tmp)
            continue
        g_tmp.append(i[0])
        j = i[1:]
        for k in j:
            tmp1, tmp2 = get_db(k)
            g_tmp.append(tmp1)
            g_tmp.append(tmp2)
        g_new.append(g_tmp)

    getData.StudentList=[]
    getData.loadData()
    g_tmp = []
    g_tmp.append("")
    for n in getData.StudentList:
        if n.status == "1":
            tmp1, tmp2 = get_db_ver2(n.name)
            g_tmp.append(tmp1)
            g_tmp.append(tmp2)
    print(g_tmp)

    del_count = []
    for a in range(len(g_tmp)):
        print(a)
        if a % 2 == 1:
            for b in g_new:
                if g_tmp[a] in b:
                    del_count.append(a)
                    del_count.append(a+1)
    for y in sorted(del_count, reverse=True):
        g_tmp.pop(y)

    g_new.append(g_tmp)
    print(g_new)
    return g_new

@app.route("/")
def hello():
    g_new = calendar()

    return render_template("main.html", g_new = g_new)


@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login_post():  
    mail = request.form.get('mail')
    #avatar = request.form.get('avatar')

    #update_image(mail, avatar)
    #g_new = calendar()
    items = [i+1 for i in range(120)]
    prob_1 = [0.01]*50
    prob_2 = [0.01]*30
    prob_3 = [0.0075]*20
    prob_4 = [0.004]*10
    prob_5 = [0.001]*10
    prob = prob_1+prob_2+prob_3+prob_4+prob_5
    result = np.random.choice(items, 1, p=prob)

    result = result[0]
    result = str(result)
    update_image(mail, result)
    #str_result = "../static/img/character (" + result + ").png"

    tmp1, tmp2 = get_db(mail)
    result=int(result)
    return render_template("gacha.html", str = result, name = tmp1)

@app.route('/return', methods=['POST'])
def return_map():
    g_new = calendar()
    return render_template("main.html", g_new = g_new)

if __name__ == "__main__":
    app.run(debug=True)