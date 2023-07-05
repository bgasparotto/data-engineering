# SQL

Structured Query Language (SQL) notes.

## Query order of execution

SQL query statements are executed in the following order:

1. `FROM/JOIN` determines the data of interest.
2. `WHERE` filters out records that do not meet the constraints.
3. `GROUP BY` groups records based one of several columns.
4. `HAVING` filters out the grouped records that do not meet the constraints.
5. `SELECT` derives desired columns and expressions.
6. `ORDER BY` sorts derived values.
7. `LIMIT/OFFSET` keeps and/or skips the specified number of records.

## Query execution plan

Databases estimate query execution plans then choose the least costly plan to execute the query.

**Analyse** the performance of a query by inspecting the execution plan graph with `EXPLAIN`:

- `EXPLAIN <query>` displays the query execution plan.
- `EXPLAIN ANALYSE <query>` executes the query and displays both the plan and the actual execution.
- `BEGIN; EXPLAIN ANALYSE <query>; ROLLBACK;` safely analyses `INSERT`, `UPDATE`, `DELETE` and `EXECUTE`.

**Watch out** for the following whilst inspecting the results:

- `Seq Scan` (sequential scan): scans the full table until the filters are satisfied. Can be mitigated by an `INDEX`
  creation resulting in an `Index Scan` instead. However, if approximately 5-10% of the records are to be returned,
  a `Seq Scan` can still take place as many index look-ups could be costlier than just scanning the table.
- `cost=0.00..150.10` (initial cost...total cost) in units of disk page fetches: should be relatively low in comparison
  to other steps, where:
    - initial cost: the start-up time before returning the first row.
    - total cost: total time to return all rows.
- `Nested Loop` when joining tables, where the database queries the one table for each record in the other table. Ensure
  the enclosed `* Scan` operations can be optimised with an `INDEX`.
