-- Imagine building a database to catalog all the animals in a local zoo, create
-- one table to track the kind of animals, another to track the specifics on each
-- Write CREATE statements for each table that include some of the needed columns

CREATE DATABASE zoo;

CREATE TABLE animals (
	id bigserial,
	animal_type varchar(25),
	animal_environment varchar(25),
);

CREATE TABLE animal_information (
	id bigserial,
	animal_name varchar(50),
	animal_weight numeric,
	acquisition_date date,
	age numeric
);

-- create INSERT statements to load sample data into the tables
INSERT INTO animals (animal_type, animal_environment)
VALUES ('Tiger', 'Jungle'),
       ('Monkey', 'Jungle'),
       ('Hippo', 'Water'),
       ('Penguin', 'Artic');

INSERT INTO animal_information (animal_name, animal_weight, acquisition_date, age)
VALUES  ('Tony', 400, '2005-08-01', 30),
	('Wukong', 200, '2011-10-30', 15),
	('HungryH', 1000, '2010-10-22', 10);
