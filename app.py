import psycopg2
from flask import Flask,render_template,request,url_for
from send_email import send_email
from send_email1 import  send_email1
from flask_sqlalchemy import SQLAlchemy

"""def create_table():
    con = psycopg2.connect(host="localhost", database="Clients", user="postgres", password="atoato06")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS accountantsman22(name TEXT, email TEXT, phone TEXT, message TEXT)")
    con.commit()
    cur.close()
    con.close()

def insert(name1,email1,phone1,message1):
    con = psycopg2.connect(host="localhost", database="Clients", user="postgres", password="atoato06")
    cur = con.cursor()
    cur.execute("INSERT INTO accountantsman(name,email,phone,password) VALUES(%s,%s,%s,%s)",(name1,email1,phone1,message1))
    con.commit()
    cur.close()
    con.close()"""
    
    
    



app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:atoato06@localhost/Clients'#creating a connection to the database created in postgres
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://ejvkvbweenjzsv:23a268364cda275c198d65d776417297d8c2dedf255362a4ce922654e2d7ce63@ec2-54-145-188-92.compute-1.amazonaws.com:5432/d2tmeh23ocr46p' 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)#an object of sqlalchemy
class Data(db.Model):#this class creates a table and adds its columns
    __tablename__ = 'accounts14'#defining table name
    id=db.Column(db.Integer,primary_key=True)#creating the colums in the table database created
    name=db.Column(db.String())
    email=db.Column(db.String(120))
    phone = db.Column(db.String(60))
    message=db.Column(db.Text())
    
    def __init__(self,name,email,phone,message):
        self.name=name
        self.email=email
        self.phone=phone
        self.message=message






@app.route('/')
def home():
    return render_template('home.html')
@app.route('/accounting')
def accounting():
    return render_template('accounting.html')

@app.route('/tax')
def tax():
    return render_template('tax.html')

@app.route('/payroll')
def payroll():
    return render_template('payroll.html')

@app.route('/business_advice')
def business_advice():
    return render_template('business_advice.html')

@app.route('/other_services')
def other_services():
    return render_template('other_services.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')


@app.route('/thank_you', methods=['POST','GET'])
def thank_you():
    if request.method == 'POST':
        username = request.form.get('name1')
        mail = request.form.get('email1')
        num = request.form.get('phone1')
        msg = request.form.get('msg1')
        if mail == "" or username == "" or num == "" or msg =="":
            message = "Please fill in the forms"
            return render_template('contactus.html',message=message)
        else:
            #insert(username,mail,num,msg)
            data=Data(username,mail,num,msg)
            db.session.add(data)
            db.session.commit()
            
            try:
                send_email(username,mail,num,msg)
                send_email1(username,mail)
                return render_template('thankyou.html')
            except:
                error = "There was a problem submitting your form. Please try again"
                return render_template('contactus.html',error=error)
            
    else:
        return render_template('home.html')

@app.route('/thank_you2', methods=['POST','GET'])
def thank_you2():
    if request.method == 'POST':
        username = request.form.get('name1')
        mail = request.form.get('email1')
        num = request.form.get('phone1')
        msg = request.form.get('msg1')
        if mail == "" or username == "" or num == "" or msg =="":
            message = "Please fill in the forms"
            return render_template('contactus.html',message=message)
        else:
            #insert(username,mail,num,msg)
            data=Data(username,mail,num,msg)
            db.session.add(data)
            db.session.commit()
            
            try:
                send_email(username,mail,num,msg)
                send_email1(username,mail)
                return render_template('thankyou.html')
            except:
                error = "There was a problem submitting your form. Please try again"
                return render_template('contactus.html',error=error)
                
    else:
        return render_template('contactus.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')
        
    
    
    
if __name__ == '__main__':
    app.run(debug =True)
    