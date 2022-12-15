/*
    Title: 'wilson_financial_db_init_frame'.sql
    Author: Brittany Kyncl
    Date:   10.30.22
    Description: wilson_financial database initialization script.
*/

-- drop database user if exists 
DROP USER IF EXISTS 'financial_user'@'localhost';


-- create financial_user and grant them all privileges to the wilson_financial database 
CREATE USER 'financial_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'finance';

-- grant all privileges to the wilson_financial database to user financial_user on localhost 
GRANT ALL PRIVILEGES ON wilson_financial.* TO 'financial_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS Assets;
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Billing;
DROP TABLE IF EXISTS Rates;

-- create the Clients table 
CREATE TABLE Clients (
    client_id     INT             NOT NULL        AUTO_INCREMENT,
    client_name   VARCHAR(75)     NOT NULL,
    phone_number  VARCHAR(75)     NOT NULL,
    initialization_date  DATE     NOT NULL,

    PRIMARY KEY(client_id)
); 

-- create the Rates table 
CREATE TABLE Rates (
    transaction_type_id     INT             NOT NULL        AUTO_INCREMENT,
    transaction_type_name   VARCHAR(75)     NOT NULL,
    transaction_fee  INT    NOT NULL,

    PRIMARY KEY(transaction_type_id)
); 

-- create the Transactions table 
CREATE TABLE Transactions (
    transaction_id     INT             NOT NULL        AUTO_INCREMENT,
    transaction_type_id  INT     NOT NULL,
    client_id  INT NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_amount INT NOT NULL,
     
    PRIMARY KEY(transaction_id),

    CONSTRAINT transaction_type_id
    FOREIGN KEY(transaction_type_id)
        REFERENCES Rates(transaction_type_id),
        
    FOREIGN KEY(client_id)
        REFERENCES Clients(client_id)
);  

-- create the Assets table
CREATE TABLE Assets (
    asset_acct_id   INT  NOT NULL        AUTO_INCREMENT,
    client_id  INT NOT NULL,
    assets   INT     NOT NULL,
    
    PRIMARY KEY(asset_acct_id),

	CONSTRAINT client_id
    FOREIGN KEY(client_id)
        REFERENCES Clients(client_id)
);

-- create the Billing table 
CREATE TABLE Billing (
    bill_id    INT             NOT NULL        AUTO_INCREMENT,
    transaction_id   INT    NOT NULL,
    client_id  INT    NOT NULL,
    transaction_type_id INT NOT NULL,
    transaction_fee    INT NOT NULL,

    PRIMARY KEY(bill_id),

    CONSTRAINT transaction_id
    FOREIGN KEY(transaction_id)
        REFERENCES Transactions(transaction_id),

    FOREIGN KEY(client_id)
        REFERENCES Clients(client_id),

   FOREIGN KEY(transaction_type_id)
        REFERENCES Rates(transaction_type_id),
	
    FOREIGN KEY(transaction_fee)
        REFERENCES Rates(transaction_type_id)
);

-- insert rates table
INSERT INTO Rates(transaction_type_name, transaction_fee)
    VALUES('Invest', '300');

INSERT INTO Rates(transaction_type_name, transaction_fee)
    VALUES('Withdraw', '100');
	
INSERT INTO Rates(transaction_type_name, transaction_fee)
    VALUES('Deposit', '50');

-- insert client records
INSERT INTO clients(client_name, phone_number, initialization_date)
    VALUES('Samuel Samethon', '402-569-5689', '2016/10/16');

INSERT INTO clients(client_name, phone_number, initialization_date)
    VALUES('Bartha Barthomieux', '402-321-5645', '2020/06/05');

INSERT INTO clients(client_name, phone_number, initialization_date)
    VALUES('Freudithan Fahrenheit', '402-489-6978', '2017/12/19');

