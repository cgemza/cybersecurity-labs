# SQL Fundamentals

## Overview

This lab documents SQL skills practiced while completing the **Google Cybersecurity Professional Certificate**. The exercises focused on retrieving, sorting, filtering, and combining data from relational databases.

## Skills Practiced

- Selecting specific columns from database tables
- Retrieving complete table records
- Inspecting table structure
- Sorting query results
- Filtering records with `WHERE`
- Matching string patterns with `LIKE` and `%`
- Filtering numeric ranges with `BETWEEN`
- Combining multiple conditions
- Excluding records using `NOT`
- Joining related tables using `INNER JOIN`

## SQL Queries

### Select Specific Columns

Retrieve selected columns from a table.

```sql
SELECT name, city, state
FROM employee;
```

### Sort Query Results

Return records and sort them according to a specified column.

```sql
SELECT *
FROM log_in_attempts
ORDER BY login_date;
```

### Inspect a Table

View information about the structure of a table.

```sql
DESCRIBE title;
```

### Filter Records

Return records matching a specific value.

```sql
SELECT *
FROM entry_door
WHERE badge_number = '342432';
```

### Pattern Matching

Use `LIKE` and the `%` wildcard to find values matching a specified pattern.

```sql
SELECT *
FROM employees
WHERE room LIKE 'Basement%';
```

Another example uses a wildcard to locate records ending in a specified value.

```sql
SELECT employee_badge_date, employee_name
FROM directory
WHERE employee_badge_date LIKE '%2026';
```

### Filter a Range

Use `BETWEEN` to return values within a specified range.

```sql
SELECT *
FROM entry_door
WHERE badge_number BETWEEN 30000 AND 40000;
```

### Combine Conditions

Use logical operators to apply multiple filtering conditions.

```sql
SELECT *
FROM keyboards
WHERE install_date = 2026 OR install_date = 2025;
```

### Exclude Records

Use `NOT` to exclude records that meet a specified condition.

```sql
SELECT *
FROM taxfiles
WHERE NOT state LIKE 'North%';
```

### Join Related Tables

Use an `INNER JOIN` to combine records from related tables using a shared identifier.

```sql
SELECT state, income, household_number
FROM clients
INNER JOIN accountant_name
ON clients.client_id = accountant_name.client_id;
```

## Key Takeaways

These exercises provided hands-on practice querying relational databases and demonstrated how SQL can be used to locate and analyze specific records efficiently. Filtering, pattern matching, logical operators, and joins provide increasingly precise ways to retrieve information from larger datasets.

---

*These examples document my own notes and technical practice while completing coursework for the Google Cybersecurity Professional Certificate. They are intended to demonstrate skills practiced rather than reproduce course assessments or proprietary lab materials.*
