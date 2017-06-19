from flask import Flask,Request,current_app,render_template,url_for,redirect,session,flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
import config,os
from Forms import NameForm
app = Flask(__name__)
app.config["SECRET_KEY"]=config.secret_key
bootstrap=Bootstrap(app)
moment=Moment(app)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(config.basedir+'//data1.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db=SQLAlchemy(app)

from flask import request
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    print(datetime.utcnow())
    return render_template('index.html',current_time=datetime.utcnow())


@app.route('/user/<name>',methods=['GET','POST'])
def user(name):
    return  render_template("user.html",name=name)

@app.route('/userLogin',methods=['GET','POST'])
def userLogin():
    name=None
    form=NameForm()
    if form.validate_on_submit():
        old_name=session.get('name')
        if old_name is not None and old_name!=form.name.data:
            flash("looks like you have changed your name!")
        session["name"]=form.name.data
        name=form.name.data
        form.name.data=""
        return redirect(url_for('userLogin'))
    return render_template('userLogin.html',form=form,name=session.get('name'))


@app.errorhandler(404)
def page_not_fount(e):
    return render_template('404.html'),400

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'),500

if __name__ == '__main__':
    app.run(debug=True)


