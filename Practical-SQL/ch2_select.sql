-- Chapter Two: Beginning Data Exploration With Select
/*
.teachers table
---------------------------------------------------------------------------
| id | first_name | last_name |        school       | hire_date  | salary |
|----+------------+-----------+---------------------+------------+--------|
| 1  | Janet      | Smith     | F.D. Roosevelt HS   | 2011-10-30 | 36200  |
|----+------------+-----------+---------------------+------------+--------|
| 2  | Lee        | Reynolds  | F.D. Roosevelt HS   | 1993-05-22 | 65000  |
|----+------------+-----------+---------------------+------------+--------|
| 3  | Samuel     | Cole      | Myers Middle School | 2005-08-01 | 43500  |
|----+------------+-----------+---------------------+------------+--------|
| 4  | Samantha   | Bush      | Myers Middle School | 2011-10-30 | 36200  |
|----+------------+-----------+---------------------+------------+--------|
| 5  | Betty      | Diaz      | Myers Middle School | 2005-08-01 | 43500  |
|----+------------+-----------+---------------------+------------+--------|
| 6  | Kathleen   | Roush     | F.D. Roosevelt HS   | 2010-10-22 | 38500  |
---------------------------------------------------------------------------
*/

SELECT * FROM teachers;

SELECT last_name, first_name, salary FROM teachers;

SELECT DISTINCT school FROM teachers;

SELECT DISTINCT school, salary FROM teachers;

-- Orders the output by salary from the teachers table in a descending order

SELECT first_name, last_name, salary FROM teachers ORDER BY salary DESC;

-- Orders the output by school, grouping school, and show most recent hires for each

SELECT last_name, school, hire_date FROM teachers ORDER BY school ASC, hire_date DESC;

-- Show those teachers  working at Myers Middle School

SELECT last_name, school, hire_date FROM teachers WHERE school = 'Myers Middle School';

-- Select those whose first name is Janet

SELECT first_name, last_name, school FROM teachers WHERE first_name = 'Janet';

-- List all schools but exclude F.D. Roosevelt HS

SELECT school FROM teachers WHERE school != 'F.D. Roosevelt HS';

-- List all teachers hired before January 1, 2000

SELECT first_name, last_name, hire_date FROm teachers where hire_date < '2000-01-01';

-- Teachers who earn $43,500 or more

SELECT first_name, last_name, salary FROM teachers WHERE salary >= 43500;

-- Inclusive search of teachers making between $40k and $65k

SELECT first_name, last_name, school, salary FROM teachers WHERE salary BETWEEN 40000 AND 65000;


