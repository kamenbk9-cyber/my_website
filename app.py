from flask import Flask, render_template, send_file
import sqlite3
import random
import io

app = Flask(__name__)
db_path = "result.db"

def get_db():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/dog_image/<int:id>")
def dog_image(id):
    conn = get_db()
    row = conn.execute("SELECT img FROM dogs WHERE [index] = ?", (id,)).fetchone()
    conn.close() 
    return send_file(io.BytesIO(row["img"]), mimetype="image/jpeg")

@app.route("/")
def index():
    conn = get_db()
    rows = conn.execute("SELECT * FROM dogs").fetchall()
    random_dogs = random.sample(range(342), 16)
    look_all = [rows[i:i+5] for i in range(0, 20, 5)]
    conn.close()
    return render_template("index.html", rows=rows, random_dogs=random_dogs, look_all=look_all)

@app.route("/info/<int:id>")
def info(id):
    conn = get_db()
    dog = conn.execute("SELECT * FROM dogs WHERE [index] = ?", (id,)).fetchone()
    conn.close()
    print(dog["descr"])
    return render_template("info_dog.html", dog=dog)

@app.route("/category_pastushi")
def category_pastushi():
    conn = get_db()
    dogs = conn.execute("SELECT * FROM dogs WHERE task LIKE '%Пастушьи%'").fetchall()
    conn.close()
    return render_template("category_pastushi.html", dogs=dogs)

@app.route("/category_ohota")
def category_ohota():
    conn = get_db()
    dogs = conn.execute("SELECT * FROM dogs WHERE task LIKE '%Охотничьи%'").fetchall()
    conn.close()
    return render_template("category_ohota.html", dogs=dogs)

@app.route("/category_boyz")
def category_boyz():
    conn = get_db()
    dogs = conn.execute("SELECT * FROM dogs WHERE task LIKE '%Бойцовские%'").fetchall()
    conn.close()
    return render_template("category_boyz.html", dogs=dogs)

@app.route("/category_company")
def category_company():
    conn = get_db()
    dogs = conn.execute("SELECT * FROM dogs WHERE task LIKE '%Компаньоны%'").fetchall()
    conn.close()
    return render_template("category_company.html", dogs=dogs)

@app.route("/category_decorate")
def category_decorate():
    conn = get_db()
    dogs = conn.execute("SELECT * FROM dogs WHERE task LIKE '%Декоративные%'").fetchall()
    conn.close()
    return render_template("category_decorate.html", dogs=dogs)

@app.route("/category_sluzheb")
def category_sluzheb():
    conn = get_db()
    dogs = conn.execute("SELECT * FROM dogs WHERE task LIKE '%Служебные%'").fetchall()
    conn.close()
    return render_template("category_sluzheb.html", dogs=dogs)

@app.route("/catalog")
def catalog():
    conn = get_db()
    dogs = conn.execute("SELECT * FROM dogs ORDER BY name").fetchall()
    dogs_letter = {}
    for dog in dogs:
        letter = dog["name"][0]
        if letter not in dogs_letter:
            dogs_letter[letter] = [[]]
        if len(dogs_letter[letter][-1]) == 5:
            dogs_letter[letter].append([])
        dogs_letter[letter][-1].append(dog)
    conn.close()
    return render_template("catalog.html", dogs_letter=dogs_letter)

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

if __name__ =="__main__":
    app.run(debug=True)