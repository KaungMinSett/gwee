# Gwee
#### Video Demo: https://youtu.be/zb8JONF12qA
<html>
 <div align = "center"> 
  <img src = "/review_post/static/img/Gwee_gwee.png">
  </div>

#### This is my final project for [Cs50x,introduction to computer science course](https://learning.edx.org/course/course-v1:HarvardX+CS50+X/home). 

<p>The project is designed to serve as foodie network in local where admin or users could review any foodie hangout places. The innovative part of the project would be we could check the trending foods based on charisma, promotion places, and food issues all together in one place. The project is still in development phase. As for now, I have completed admin part where I can start of my website.
 </p>
 <p>
  In static folder, this is where every image I used in my web app and styling contents such as css and javascript files reside. 
  And there is template folder in which html files I used to construct the skeleton of my web pages exist.
  And init.py is where I initialize my whole web app. It contains my database URI and secret key.
  In forms.py, I construct all forms used to accept inputs from users.
  Models.py is used to define my data structure and database for my web app.
  In routes.py, it is where every route information is processed and replied. This is the brain of my web app.
  And manage.py file is used to create new admin through scripts. I didn't want to create admin using UI for security issues.
  And all of my used libararies and frameworks are lised in requirements.txt 
 </p>
- How to setup the Project
 1. pip install -r requirements.txt
 2. install PostgreSQL
 3. Create your own secretkey, Database username, Database password, Database URl in .env file
 4. python run.py

<hr>

  #### Used Main Technology
- Database      : PostgreSQL
- SQL toolkit   : SQLAlchemy
- CSS framework : Bootstrap
- JavaScript Library : JQuery
- Web framework : Flask



#### RoadMap
- [x] Website Layout
- [x] Admin Login
- [x] session timeout 
- [x] photo upload
- [x] Admin Post
- [x] Admin  Post delete
- [x] Pagination
</html>
