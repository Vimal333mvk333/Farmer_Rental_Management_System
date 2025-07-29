from flask import Flask, render_template, request, redirect
import mysql.connector
from datetime import date

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vimal@24",
    database="farmer_rental2"
)
cursor = db.cursor(dictionary=True)

@app.route('/')
def index():
    cursor.execute("SELECT * FROM farmers")
    farmers = cursor.fetchall()
    return render_template('index.html', farmers=farmers)

@app.route('/add_farmer', methods=['POST'])
def add_farmer():
    name = request.form['name']
    contact = request.form['contact']
    total_rent = request.form['total_rent']
    balance = request.form['balance']
    cursor.execute("INSERT INTO farmers (name, contact, total_rent, balance) VALUES (%s, %s, %s, %s)",
                   (name, contact, total_rent, balance))
    db.commit()
    return redirect('/')

@app.route('/delete_farmer', methods=['POST'])
def delete_farmer():
    name = request.form['name']
    contact = request.form['contact']
    cursor.execute("DELETE FROM rent_additions WHERE farmer_id IN (SELECT farmer_id FROM farmers WHERE name=%s AND contact=%s)", (name, contact))
    cursor.execute("DELETE FROM transactions WHERE farmer_id IN (SELECT farmer_id FROM farmers WHERE name=%s AND contact=%s)", (name, contact))
    cursor.execute("DELETE FROM farmers WHERE name=%s AND contact=%s", (name, contact))
    db.commit()
    return redirect('/')

@app.route('/transactions/<int:farmer_id>')
def transactions(farmer_id):
    cursor.execute("SELECT * FROM farmers WHERE farmer_id = %s", (farmer_id,))
    farmer = cursor.fetchone()
    cursor.execute("SELECT * FROM transactions WHERE farmer_id = %s ORDER BY payment_date DESC", (farmer_id,))
    transactions = cursor.fetchall()
    return render_template('transactions.html', farmer=farmer, transactions=transactions)

@app.route('/add_rent/<int:farmer_id>', methods=['POST'])
def add_rent(farmer_id):
    amount = float(request.form['amount'])
    cursor.execute("UPDATE farmers SET total_rent = total_rent + %s, balance = balance + %s WHERE farmer_id = %s",
                   (amount, amount, farmer_id))
    cursor.execute("INSERT INTO rent_additions (farmer_id, amount_added, addition_date) VALUES (%s, %s, %s)",
                   (farmer_id, amount, date.today()))
    db.commit()
    return redirect(f'/transactions/{farmer_id}')

@app.route('/pay/<int:farmer_id>', methods=['POST'])
def pay(farmer_id):
    amount = float(request.form['amount'])
    cursor.execute("UPDATE farmers SET balance = balance - %s WHERE farmer_id = %s", (amount, farmer_id))
    cursor.execute("INSERT INTO transactions (farmer_id, amount_paid, payment_date) VALUES (%s, %s, %s)",
                   (farmer_id, amount, date.today()))
    db.commit()
    return redirect(f'/transactions/{farmer_id}')

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
