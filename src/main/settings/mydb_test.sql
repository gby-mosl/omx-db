DROP DATABASE IF EXISTS mydb;

CREATE DATABASE mydb;

USE mydb;

CREATE TABLE companies (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    address TEXT NOT NULL,
    post_code VARCHAR(10) NOT NULL,
    city VARCHAR(255) NOT NULL
)ENGINE=INNODB;

# Creation of the user company - always on first id
INSERT INTO companies (name, address, post_code, city) VALUE ('OMEXOM Nancy', '2 Rue du Bois Jacquot', '54670', 'MILLERY');

CREATE TABLE people (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    lastname VARCHAR(255) NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    company_id INT NOT NULL,
    job VARCHAR(255),
    status BOOL DEFAULT TRUE,
    FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=INNODB;

CREATE VIEW technicians_vw AS
    (
    SELECT *
    FROM people
    WHERE job LIKE '%Etudes'
    );