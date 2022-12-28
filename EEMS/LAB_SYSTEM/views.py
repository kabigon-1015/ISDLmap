# -*- coding: utf-8 -*-
from flask import Flask,abort,request,redirect,url_for,render_template,flash,session
from LAB_SYSTEM import app
from LAB_SYSTEM import getData
import os

# from linebot import (
#     LineBotApi, WebhookHandler
# )
# from linebot.exceptions import (
#     InvalidSignatureError
# )
# from linebot.models import (
#     MessageEvent, TextMessage, TextSendMessage,
# )


# YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
# YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

# line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
# handler = WebhookHandler(YOUR_CHANNEL_SECRET)

# @app.route("/callback", methods=['POST'])
# def callback():
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']

#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     # handle webhook body
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         abort(400)

#     return 'OK'

# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text))

@app.route('/')
def show_entries():
    # if not session.get('logged_in'):
    #     return redirect(url_for('login'))
    getData.StudentList=[]
    getData.loadData()
    return render_template('entries/index.html',db=getData.StudentList)

# @app.route('/')
# def show_entries():
#     if not session.get('logged_in'):
#         return redirect(url_for('login'))
#     getData.StudentList=[]
#     getData.loadData()
#     return render_template('entries/index.html',db=getData.StudentList)
    

# @app.route('/login',methods=['GET','POST'])
# def login():
#     error=None
#     if request.method=='POST':
#         if request.form['username']!=app.config['USERNAME']:
#             flash('ユーザ名が異なります')
#         elif request.form['password']!=app.config['PASSWORD']:
#             flash('パスワードが異なります')
#         else:
#             session['logged_in']=True
#             flash('ログインしました')
#             return redirect(url_for('show_entries'))
#     return render_template('login.html')

# @app.route('/logout')
# def logout ():
#     session.pop('logged_in',None)
#     flash('ログアウトしました')
#     return redirect(url_for('show_entries'))

# @app.route('/register',methods=['GET','POST'])
# def register():
#     error=None
#     if request.method=='POST':
#         if request.form['password']!=request.form['password_check']:
#             flash('パスワードが一致していません')
#             return redirect(url_for('register'))
#         else:
#             flash('ユーザ登録が完了しました')
#             return redirect(url_for('login'))
#     return render_template('register.html')


