# 👨‍🌾 Farmer Rental Management System

A web-based project built using **Flask (Python)** and **MySQL** for managing rent payments and balances of farmers. The system allows adding farmers, updating rent, tracking transactions, and managing outstanding balances—all in a simple browser interface.

---

## 📁 Files Included

- `app.py`: The main Flask backend file.
- `farmer_rental2.sql`: SQL script to create the required database and tables.
- `run_project_corrected.bat`: Windows batch file to automatically run the project.
- `templates/`: HTML templates folder (you should include `index.html`, `transactions.html` here).

---

## ✅ Requirements

Make sure you have the following installed:

### 🔧 Software
- Python 3.x
- MySQL Server
- A browser (for accessing the app at `http://127.0.0.1:5000`)

### 📦 Python Packages

Install using `pip`:

```bash
pip install flask mysql-connector-python
```

---

## 🛠️ Database Setup

1. Open MySQL (Workbench or CLI).
2. Run the script in `farmer_rental2.sql`.

This creates:

### 📊 Tables

- **`farmers`**: Stores farmer details, rent, and balance.
- **`transactions`**: Records payments made by farmers.
- **`rent_additions`**: Records rent increases for farmers.

```sql
CREATE DATABASE IF NOT EXISTS farmer_rental2;
USE farmer_rental2;

CREATE TABLE IF NOT EXISTS farmers (
    farmer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    contact VARCHAR(50),
    total_rent DECIMAL(10,2),
    balance DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    farmer_id INT,
    amount_paid DECIMAL(10,2),
    payment_date DATE,
    FOREIGN KEY (farmer_id) REFERENCES farmers(farmer_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS rent_additions (
    addition_id INT AUTO_INCREMENT PRIMARY KEY,
    farmer_id INT,
    amount_added DECIMAL(10,2),
    addition_date DATE,
    FOREIGN KEY (farmer_id) REFERENCES farmers(farmer_id) ON DELETE CASCADE
);
```

---

## 🚀 How to Run

### Option 1: Run using Command Line

```bash
python app.py
```

### Option 2: Run using Batch File (Windows)

Double-click `run_project_corrected.bat`. It will open the app in your default browser.

---

## 🧠 Project Features

- ➕ **Add Farmer**: Name, contact, initial rent, balance.
- 💰 **Add Rent**: Increase total rent and balance.
- 💸 **Record Payment**: Decrease balance and log payment date.
- 🧾 **View Transactions**: Show history of all payments.
- ❌ **Delete Farmer**: Deletes farmer and all related transactions.

---

## 🌐 Web Interface (Templates Folder)

- `index.html`: Shows all farmers and links to transactions.
- `transactions.html`: Displays transaction history and forms for rent and payments.

---

## ⚠️ Configuration

Make sure your MySQL username and password in `app.py` match your MySQL setup:

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="farmer_rental2"
)
```

---

## 📌 Suggestions for Future Enhancements

- Add Admin Login and Authentication
- Input validation for forms
- Export transactions as CSV
- Mobile responsive layout
- Cloud deployment (e.g., Heroku, Render)

---

## 💡 Author

Created by [Vimal Kumar M].  
GitHub:(https://github.com/Vimal333mvk333)

---

## 📝 License

This project is open-source and free to use for educational purposes.
