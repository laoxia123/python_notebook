#coding:utf-8
from flask import Flask,request,render_template,redirect,url_for
import time

app=Flask(__name__)

users = [] #这里存放所有的留言

@app.route('/say/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html',says=users)
    else:
        title = request.form.get('say_title')
        text  = request.form.get('say')
        user = request.form.get('say_user')
        date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        users.append({
            "title":title,
            "text":text,
            "user":user,
            "date":date
        })
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
