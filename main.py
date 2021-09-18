import psycopg2
from flask import Flask,render_template,request,url_for


def create_table():
    con = psycopg2.connect(host="localhost", database="Clients", user="postgres", password="atoato06")
    cur = con.cursor()
    cur.execute("CREATE TABLE  assembly56(name TEXT, email TEXT, phone TEXT, password TEXT)")
    con.commit()
    cur.close()
    con.close()

def insert(name1,email1,phone1,password1):
    con = psycopg2.connect(host="localhost", database="Clients", user="postgres", password="atoato06")
    cur = con.cursor()
    cur.execute("INSERT INTO PEOPLE(name,email,phone,password) VALUES(%s,%s,%s,%s)",(name1,email1,phone1,password1))
    con.commit()
    cur.close()
    con.close()
    
    



app = Flask(__name__)
@app.route('/')
def home():
    create_table()
    insert("ghh","grygr","676767676","ufurghurg")
    return render_template('home.html')
    
    
if __name__ == '__main__':
    app.run(debug =True)
    