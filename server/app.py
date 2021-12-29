from re import template
from flask import Flask,request,jsonify,render_template,session
from sqlalchemy import create_engine
from config import db,db_url
from crawling import crawling


def create_app():
  app=Flask(__name__)
  
  app.secret_key='dhwlscjf!ohjincheol42931998'
  
  database=create_engine(db_url,encoding='utf-8',max_overflow=0)
  
  
  @app.route('/',methods=['GET'])
  def home():
    if 'user' in session: 
      return render_template('blackboard.html')
    return render_template('main.html')
  
  
  @app.route('/get',methods=['GET'])
  def get():
    if 'user' in session: 
      return render_template('blackboard.html')
    
    
    return render_template('signup.html')
  
  #회원가입
  @app.route('/sign-up',methods=['GET','POST'])
  def sign_up():
    if 'user' in session: 
      return render_template('blackboard.html')
    
    user_id=request.form['id']
    user_password=request.form['pw']
    user_name=request.form['name']
    
    search=database.execute("select * from sign_up where user_id='%s'"%(user_id)).fetchall()
    
    if search: #이미 존재하면 
      
      return render_template('signup.html')
    else: 
      
      input=database.execute("insert into sign_up values (NULL,'%s','%s','%s')"%(user_name,user_id,user_password))
        
      return render_template('login.html')
    
    
  
    
  #login 화면 이동 
  @app.route('/login-form',methods=['GET'])
  def login_form():
    return render_template('login.html')
  
  
  #로그인
  @app.route('/login',methods=['POST'])
  def login():
    
    app.user_id=request.form['id']
    app.user_password=request.form['pw']
    
    rows=database.execute("select * from sign_up where user_id='%s'"%(app.user_id)).fetchall()
    
    if len(app.user_id)==0 or len(app.user_password)==0:
      return render_template('login.html')
    else:
      if rows:
        courselist=crawling(app.user_id,app.user_password) #크롤링 api 에 유저 정보 넘기기
        
        for row in rows:
          if row[3]==app.user_password:
            
            session['user']=app.user_id
            session['user_course']=courselist
            
            return render_template('blackboard.html',courselist=courselist)
      else:
        return render_template('login.html')

  #로그아웃
  @app.route('/logout', methods=['GET'])
  def logout():
    session.pop('user', None)
    return render_template('main.html')

  
  
    

  return app
