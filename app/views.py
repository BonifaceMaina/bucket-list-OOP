from flask import request, render_template, redirect, url_for, session, flash

from app import app
from .models import User, Bucketlist, Items, bucketlistdict, items
from .forms import RegistrationForm, LoginForm, BucketlistForm, BucketlistItems, EditBucketListForm, EditBucketListItemsForm

USER = User()
BUCKETLIST = Bucketlist()
ITEM = Items()
@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    """homepage route"""
    error = None
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']     
        confirm_password = request.form['password']
        if password !=confirm_password:
            error = "The passwords must match"
            return render_template("index.html", form=form, error=error)
        else:
            if USER.CreateUsers(username, password) == "Registered":
                session['logged_in'] = True
                return redirect(url_for("bucketlists"))
    return render_template("index.html", form=form)

@app.route('/login',methods=['POST', 'GET'])
def login():
    """logging in the user"""
    form = LoginForm(request.form)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if USER.Login(username, password) == "Logged in successfully":
            session['logged_in'] = True
            return redirect(url_for("bucketlists"))   
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    """logging out"""
    session['logged_in'] = ''
    return redirect(url_for("login"))

@app.route('/bucketlists', methods=['POST', 'GET'])
def bucketlists():
    """showing and creating bucketlists"""
    form = BucketlistForm(request.form)
    if session['logged_in']:
        if request.method == 'POST':
            bucket = request.form['bucketlist']       
            if BUCKETLIST.CreateBucketList(bucket) == "Added bucketlist":
                return redirect(url_for("bucketlists"))
            else:
                return redirect(url_for('bucketlists'))
        else:
            buckets = BUCKETLIST.ShowBucketLists()
            return render_template("bucketlist.html", form=form, bucketlistdict=buckets)
    return redirect(url_for("login"))

@app.route('/bucketlistitems', methods=['POST', 'GET'])
def bucketlistitems():
    """getting the individual items for a bucketlist"""
    form = BucketlistItems(request.form)
    if session['logged_in'] is True:        
        if request.method == 'POST':
            item = request.form['bucketitem']       
            if ITEM.CreateItems(item) == "Item added":
                return redirect(url_for("bucketlistitems"))
            else:
                return redirect(url_for("bucketlistitems"))
        return render_template("bucketlistcontents.html", form=form, bucketitemdict=items)
    return redirect(url_for("login"))

@app.route('/editbucketlist', methods=['POST'])
def editbucketlist():
    """editing the bucketlist"""
    form = EditBucketListForm(request.form)
    if session.get('logged_in'):
        key = request.form['key']
        value = request.form['value']
        if BUCKETLIST.EditBucketList(int(key), value) == "Edit successful":
            return redirect(url_for("bucketlists"))
        else:
            return render_template("index.html")
    return redirect(url_for('login'))

@app.route('/deletebucketlist', methods=['POST'])
def deletebucketlist():
    """deleting a bucketlist"""
    item = request.form['key']
    if BUCKETLIST.DeleteBucketLists(int(item)) == "Deleted Item":
        return redirect(url_for("bucketlists"))
    else:
        return redirect(url_for("login"))

@app.route('/editbucketlistitems', methods=['POST'])
def editbucketlistitems():
    """editing bucketlist items"""
    form = EditBucketListItemsForm(request.form)
    key = request.form['key']
    value = request.form['value']
    if ITEM.EditItems(int(key), value) == "Edit Successful":
        return redirect(url_for("bucketlistitems"))
    else:
        return redirect(url_for("index"))

@app.route('/deletebucketlistitems', methods=['POST'])
def deletebucketlistitems():
    """deleting bucketlist items"""
    item = request.form['key']
    if ITEM.DeleteItems(int(item)) == "Item deleted":
        return redirect(url_for("bucketlistitems"))
    else:
        return redirect(url_for("bucketlistitems"))

