# Backend API(Task1)

Replace 'postgresql://username:password@localhost/assignment_db' with your PostgreSQL credentials.
Run the API with python backend/app.py to test the endpoints

## Description
This task involves creating a Flask-based API for managing app details with endpoints for adding, retrieving, and deleting apps.

## Prerequisites
- Python 3.12.5 OR 3.8 Above 
- PostgreSQL
- Python packages: flask, flask-sqlalchemy, psycopg2-binary

## Installation
1. Navigate to the `backend` directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Configure the PostgreSQL database connection in `app.py`.

## Running the Code
- Start the API: `python app.py`

## Testing
- Use Postman or curl to test endpoints.
- Example:
  - Add app: `curl -X POST -H "Content-Type: application/json" -d '{"name": "TestApp", "version": "1.0", "description": "Test Description"}' http://localhost:5000/add-app`
- Write unit tests with pytest for automated testing.

## Additional Notes
Ensure the database is running and credentials are correct.


# Database Management(Task2)

## Description
This task involves setting up the PostgreSQL database schema and inserting sample data.

## Prerequisites
- PostgreSQL

## Installation
1. Create the database: `createdb assignment_db`
2. Run the schema: `psql -d assignment_db -f schema.sql`
3. Insert sample data: `psql -d assignment_db -f sample_data.sql`

## Testing
- Use pgAdmin or psql to verify tables and data.
- Check for apps like "App1" and "App2" in the database.

## Additional Notes
Ensure PostgreSQL is installed and accessible.

Steps to Fix and Create the Database
1. Verify PostgreSQL Service is Running
F:\PostgreSQL\17\bin\pg_ctl status -D "F:\PostgreSQL\17\data"

If it says “pg_ctl: server is running,” great! If not, start it:
F:\PostgreSQL\17\bin\pg_ctl start -D "F:\PostgreSQL\17\data"

Create the Database with the postgres User
F:\PostgreSQL\17\bin\createdb -U postgres assignment_db

verify creation
psql -U postgres -l

connect to database
psql -U postgres -d assignment_db

--------------------------
1.CHECK POSTGRES SERVICE STATUS
F:\PostgreSQL\17\bin\pg_ctl status -D "F:\PostgreSQL\17\data"

2.START THE POSTGRES SERVER
F:\PostgreSQL\17\bin\pg_ctl start -D "F:\PostgreSQL\17\data"

3.CREATE THE DATABASE
F:\PostgreSQL\17\bin\createdb -U postgres assignment_db

4.VERIFY THE DATABASE

F:\PostgreSQL\17\bin\psql -U postgres -l

5.STOP THE SERVER


F:\PostgreSQL\17\bin\pg_ctl stop -D "F:\PostgreSQL\17\data"

6.INITIALISE NEW DATA DIRECTORY
F:\PostgreSQL\17\bin\initdb -D "F:\PostgreSQL\17\data" -U postgres --pwfile=<(echo "newpassword123")

