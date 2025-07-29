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
