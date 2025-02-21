from flask import Flask, render_template, request, redirect,url_for
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '19999'
app.config['MYSQL_DB'] = 'book_store'
mysql = MySQL(app)


@app.route('/')
def index():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        cursor.close()
        return render_template('index.html', books=books)

@app.route('/add' , methods=['POST','GET'])
def add():
    if request.method=='POST':
        title = request.form['title']
        author = request.form['author']
        review= request.form['review']
        page_no = request.form['page_no']
        date = request.form['date']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO books(title,author,review,page_no,date) VALUES (%s,%s,%s,%s,%s)",
                       (title,author,review,page_no,date))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)