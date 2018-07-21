-- Shows the different character datatypes and how they handle padding
CREATE TABLE char_data_types (
	varchar_column varchar(10),
	char_column char(10),
	text_column text
);

-- Inserts the same content into each column in order of appearance
INSERT INTO char_data_types
VALUES
	('abc', 'abc', 'abc'),
	('defghi', 'defghi', 'defghi');

-- Send this information to a file, with pipe as a seperator 	
COPY char_data_types TO 'C:\Users\atwoo\Documents\SQL\typetest.txt'
WITH (FORMAT CSV, HEADER, DELIMITER '|');

/*
Numbers
*/

CREATE TABLE number_data_types (
	-- 20 digits, scale of 5 after decimal, adds padding
	numeric_column numeric(20,5),
	-- Shows the number rounds up if greater than 6 digits percision
	real_column real,
	-- Holds up to 15 digits
	double_column double precision
);

INSERT INTO number_data_types
VALUES
	(.7, .7, .7),
	(2.13579, 2.13579, 2.13579),
	(2.1357987654, 2.1357987654, 2.1357987654);

SELECT * FROM number_data_types;

-- floating point can lead to calculation errors
SELECT numeric_column * 10000000 AS "Fixed", real_column * 10000000 AS "Float" FROM number_data_types WHERE numeric_column = .7;


/*
Date and time
*/
CREATE TABLE date_time_types (
	timestamp_column timestamp with time zone,
	interval_column interval
);

INSERT INTO date_time_types
VALUES
	('2018-12-31 01:00 EST','2 days'),
	('2018-12-31 01:00 -8','1 month'),
	('2018-12-31 01:00 Australia/Melbourne','1 century'),
	(now(),'1 week');
	
SELECT * FROM date_time_types;

-- Interval math, creates new date from subtracting timestamp from interval.
SELECT timestamp_column, interval_column, timestamp_column - interval_column AS new_date FROM date_time_types;

/*
Transforming Values with CAST, letters cannot become integers
*/
SELECT timestamp_column, CAST(timestamp_column AS varchar(10))
FROM date_time_types;

SELECT numeric_column,
	CAST(numeric_column AS integer),
	CAST(numeric_column AS varchar(6))
FROM number_data_types;


-- In PostgreSQL you can use :: for a shortcut with CAST
-- Normal method
SELECT timestamp_column, CAST(timestamp_column AS varchar(10))
FROM date_time_types;
-- Shortcut method
SELECT timestamp_column::varchar(10)
FROM date_time_types;





