# Python Object-Relational Mapping (ORM)

This directory contains Python exercises for working with MySQL databases using both `MySQLdb` and SQLAlchemy. The exercises cover querying, filtering, inserting, deleting, joining tables, and defining relationships between Python classes and database tables.

## Requirements

- Python 3
- MySQL Server running locally on port `3306`
- `MySQLdb` (`mysqlclient` / `python3-mysqldb`)
- SQLAlchemy
- A MySQL user with permission to access the exercise databases

## Installation

On Ubuntu or WSL, install the system packages:

```bash
sudo apt update
sudo apt install python3-mysqldb python3-sqlalchemy
```

Alternatively, in an environment where pip packages are appropriate:

```bash
python3 -m pip install SQLAlchemy mysqlclient
```

Check that the modules can be imported:

```bash
python3 -c "import MySQLdb; import sqlalchemy; print('Dependencies are ready')"
```

## Database setup

Open the MySQL client as an administrator:

```bash
sudo mysql
```

Create the exercise databases as needed:

```sql
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
CREATE DATABASE IF NOT EXISTS hbtn_0e_14_usa;
CREATE DATABASE IF NOT EXISTS hbtn_0e_101_usa;
```

Create or configure a MySQL user for the scripts. Replace the example password with your own secure password:

```sql
CREATE USER IF NOT EXISTS 'pythonuser'@'localhost' IDENTIFIED BY 'replace_with_your_password';
GRANT ALL PRIVILEGES ON hbtn_0e_6_usa.* TO 'pythonuser'@'localhost';
GRANT ALL PRIVILEGES ON hbtn_0e_14_usa.* TO 'pythonuser'@'localhost';
GRANT ALL PRIVILEGES ON hbtn_0e_101_usa.* TO 'pythonuser'@'localhost';
FLUSH PRIVILEGES;
```

If the user already exists, use `ALTER USER` to update its password rather than creating it again.

### Example table data

For the state exercises, the `states` table can be created and populated with sample rows. Run these commands in the `hbtn_0e_6_usa` database if your assignment environment does not already provide the table/data:

```sql
USE hbtn_0e_6_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO states (name) VALUES
('California'),
('Arizona'),
('Texas'),
('New York'),
('Nevada');
```

Do not insert the sample rows again if the table is already populated; otherwise, duplicate rows may appear.

For the city and relationship exercises, use the supplied assignment SQL files where applicable. In particular, `101-relationship_states_cities_list.sql` is associated with the relationship-based state/city exercise.

## Files and exercises

### Basic MySQLdb exercises

These scripts use command-line arguments for the MySQL username, password, and database. Scripts that filter by a supplied value take that value as an additional argument.

| File | Purpose |
|---|---|
| `0-select_states.py` | List all states from the `states` table. |
| `1-filter_states.py` | List states whose names begin with an uppercase `N`. |
| `2-my_filter_states.py` | Filter states using a name supplied on the command line. |
| `3-my_safe_filter_states.py` | Filter states using a parameterized query to reduce SQL-injection risk. |
| `4-cities_by_state.py` | List cities together with their state names using a join. |
| `5-filter_cities.py` | List cities belonging to a state supplied on the command line. |

### SQLAlchemy state exercises

These exercises use `model_state.py` and the `State` model. The typical database for this group is `hbtn_0e_6_usa`.

| File | Purpose |
|---|---|
| `model_state.py` | Defines the SQLAlchemy `Base` and `State` model mapped to the `states` table. |
| `6-model_state.py` | Creates the mapped table(s) in the database. |
| `7-model_state_fetch_all.py` | Retrieves all states, ordered by ascending ID. |
| `8-model_state_fetch_first.py` | Retrieves the first state by ascending ID; prints `Nothing` if no state exists. |
| `9-model_state_filter_a.py` | Lists states whose names contain the letter `a`, ordered by ascending ID. |
| `13-model_state_delete_a.py` | Deletes states whose names contain the letter `a`. |

### SQLAlchemy city exercises

These exercises use the `State` and `City` models. The city model refers to the related state through the state's ID.

| File | Purpose |
|---|---|
| `model_city.py` | Defines the SQLAlchemy `City` model mapped to the `cities` table, with a state foreign key. |
| `14-model_city_fetch_by_state.py` | Lists cities grouped/displayed with their state information, ordered by city ID. |
| `14-model_city_fetch_by_state.sql` | SQL setup/query file associated with the city-by-state exercise. |

### SQLAlchemy relationship exercises

These exercises use the `hbtn_0e_101_usa` database and SQLAlchemy relationships between states and cities.

| File | Purpose |
|---|---|
| `relationship_state.py` | Defines the `State` model and its relationship to cities. |
| `relationship_city.py` | Defines the `City` model and its relationship back to a state. |
| `101-relationship_states_cities_list.sql` | SQL setup file for the relationship-based states/cities exercise. |
| `102-relationship_cities_states_list.py` | Lists states and their related cities using SQLAlchemy relationships; uses one database query and orders cities by ascending ID. |

> File names and exercise descriptions above reflect the files discussed for this project. If a listed file is not present in your working directory, create or copy it from the corresponding exercise before running it.

## Running the scripts

Move to the project directory:

```bash
cd /mnt/c/Users/pc/OneDrive/Desktop/set-high_level_programming/python-object_relational_mapping
```

Make a script executable if needed:

```bash
chmod +x 9-model_state_filter_a.py
```

Run a script with the required MySQL credentials and database name:

```bash
./9-model_state_filter_a.py MYSQL_USERNAME MYSQL_PASSWORD hbtn_0e_6_usa
```

For example, if your configured account is named `pythonuser`:

```bash
./9-model_state_filter_a.py pythonuser 'YOUR_PASSWORD' hbtn_0e_6_usa
```

Keep passwords in quotes when they contain shell-special characters such as `!`. Avoid putting real passwords into shared files or committing them to Git.

For the relationship exercise:

```bash
./102-relationship_cities_states_list.py MYSQL_USERNAME MYSQL_PASSWORD hbtn_0e_101_usa
```

## Expected behavior and troubleshooting

- **`ModuleNotFoundError: No module named 'sqlalchemy'`**: install SQLAlchemy in the same Python environment used to run the script.
- **`ModuleNotFoundError: No module named 'MySQLdb'`**: install `python3-mysqldb` or `mysqlclient`.
- **`Access denied for user`**: check the username/password and confirm that the user has privileges on the target database. On Ubuntu, `sudo mysql` may be required for administrator access.
- **`Nothing` from `8-model_state_fetch_first.py`**: the query did not find any rows. Confirm that the `states` table exists and contains data.
- **No output from a list script**: confirm that the target table has rows and that you are using the correct database.
- **Connection errors**: verify that MySQL is running and listening on `localhost:3306`.
- **Importing a script runs database code unexpectedly**: executable scripts should put their main logic under `if __name__ == "__main__":`.

## General implementation notes

- Use command-line arguments for database credentials and database name when required by the assignment.
- Connect to MySQL on `localhost`, port `3306`.
- Order results explicitly when the exercise requires a particular order.
- Use parameterized SQL queries for user-provided values in `MySQLdb` scripts.
- In SQLAlchemy scripts, use the required models and sessions, and avoid executing the main program when a module is imported.
- Do not commit database passwords or other credentials to version control.
