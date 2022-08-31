"""This contains all routes information for gwee"""
import os
import secrets
from flask import render_template, flash, redirect, send_from_directory, url_for, request, current_app,session
from review_post import app, photos

from review_post.models import Admin, Post
from review_post.forms import PostForm, RegisterForm, LoginForm



from review_post import db
from flask_login import login_user, login_required, current_user


def save_photo(photo):
    rand_hex  = secrets.token_hex(10)
    _, file_extention = os.path.splitext(photo.filename)
    file_name = rand_hex + file_extention
    file_path = os.path.join(app.root_path,'static/img', file_name)
    photo.save(file_path)
    return file_name


@app.route("/")
def index():
    """index page of web app"""
    return render_template("index.html")


@app.route("/home")
def home():
    """home page of web app"""
    posts = Post.query.order_by(Post.id.desc()).all()
    promo_posts = Post.query.filter(Post.tag == "Promotion").all()
    trend_posts = Post.query.filter(Post.tag == "Trending").all()
    alert_posts = Post.query.filter(Post.tag == "Alert").all()

    return render_template("home.html", posts = posts, promoPosts = promo_posts, trendPosts = trend_posts, alertPosts = alert_posts)


@app.route("/Login", methods= ['GET', 'POST'])
def login():
    """login page
    For GET requests, display the login form. 
    For POSTS, login the current user by processing the form. """
    # print (db)
    form = LoginForm()

    
    if form.validate_on_submit():
        attempt_admin = Admin.query.filter_by(username=form.username.data).first()
        
        if attempt_admin and attempt_admin.isvalid_password(
            attempt_password = form.password.data
            ):
            
            login_user(attempt_admin)
            session.permanent = True
            flash(f'Success! you are logged in as :{attempt_admin.username}', category='success')
            return redirect(url_for('adminpanel'))
        else:
            
            flash('Username and password are not match! Please try again', category='danger')
    return render_template("login.html", form=form)
    
# @app.route('/static/img/<filename>')
# def get_image(filename):
#     return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

    
@app.route('/adminpanel', methods =['GET', 'POST'])
@login_required
def adminpanel():
    """Admin panel"""
    form = PostForm()
   
        
 
 
    if form.validate_on_submit():

        description = form.description.data
        tag = form.tag.data
        
        # filename = photos.save(form.photo.data)
        # file_url = url_for('get_image', filename = filename)
        file_name = save_photo(request.files.get('photo'))
        
        post = Post(description = description,image_url = file_name, tag = tag ,owner = current_user.username)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been submitted','success')
    

    
    posts = Post.query.order_by(Post.id.desc()).all()
    promo_posts = Post.query.filter(Post.tag == "Promotion").all()
    trend_posts = Post.query.filter(Post.tag == "Trending").all()
    alert_posts = Post.query.filter(Post.tag == "Alert").all()

   
    
    return render_template("adminpanel.html", form = form, posts = posts, promoPosts = promo_posts, trendPosts = trend_posts, alertPosts = alert_posts)


@app.route("/register")
def register():
    """Register page"""
    # form = RegisterForm()
    # if form.validate_on_submit():
    #     user_to_create = User(


    #     )


