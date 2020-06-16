from flask import Flask, render_template

import psycopg2

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/db')
def db():
    #conn=posgress.connection(host, puerto, usuario, password, dbname)
    #responde= conn.query('SELECT * FROM messages')
    #for row in responde:
    #    print(row[0])
    #conn.close
    conn = psycopg2.connect(
        dbname='d1hng3emapdk56',
        user='zopevjzmqgultc',
        password='73e389a80d7eff6cc32716b144dcbd6d9bc7dada696f4571e6509a7a2ca30986',
        host='ec2-18-232-143-90.compute-1.amazonaws.com',
        port='5432'
    )
    if conn==None:
        print('La conexion fallo!')
        return ''
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM messages')
    fetch= cursor.fetchall()
    for row in fetch:
        print(row[3])
    return render_template('db.html', msgs=fetch)

if __name__ == '__main__':
    app.run()