SQL Fundamentals
Overview

This lab documents SQL skills practiced while completing the Google Cybersecurity Professional Certificate. The exercises focused on retrieving, sorting, filtering, and combining data from relational databases.

Skills Practiced
Selecting specific columns from database tables
Retrieving complete table records
Inspecting table structure
Sorting query results
Filtering records with WHERE
Matching string patterns with LIKE and %
Filtering numeric ranges with BETWEEN
Combining multiple conditions
Excluding records using NOT
Joining related tables using INNER JOIN
SQL Queries
Select Specific Columns

Retrieve selected columns from a table.

SELECT name, city, state
FROM employee;
Sort Query Results

Return records and sort them according to a specified column.

SELECT *
FROM log_in_attempts
ORDER BY login_date;
Inspect a Table

View information about the structure of a table.

DESCRIBE title;
Filter Records

Return records matching a specific value.

SELECT *
FROM entry_door
WHERE badge_number = '342432';
Pattern Matching

Use LIKE and the % wildcard to find values matching a pattern.

SELECT *
FROM employees
WHERE room LIKE 'Basement%';
Filter a Range

Use BETWEEN to return values within a specified range.

SELECT *
FROM entry_door
WHERE badge_number BETWEEN 30000 AND 40000;
Combine Conditions

Use logical operators to apply multiple filtering conditions.

SELECT *
FROM keyboards
WHERE install_date = 2026 OR install_date = 2025;
Exclude Records

Use NOT to exclude records that meet a specified condition.

SELECT *
FROM taxfiles
WHERE NOT state LIKE 'North%';
Join Related Tables

Use an INNER JOIN to combine records from related tables using a shared identifier.

SELECT state, income, household_number
FROM clients
INNER JOIN accountant_name
ON clients.client_id = accountant_name.client_id;
Key Takeaways

These exercises provided hands-on practice querying relational databases and demonstrated how SQL can be used to locate and analyze specific records efficiently. Filtering, pattern matching, logical operators, and joins provide increasingly precise ways to retrieve information from larger datasets.
