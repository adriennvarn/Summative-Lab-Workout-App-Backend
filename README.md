# Workout App Backend Demo
#### By Adrienn Varn
Backend for a hypothetical Workout App - Summative Lab for Flatiron School SE-FND2-FT Module 24

This backend app demonstrates knowledge of Flask API creation, SQLAlchemy mastery, and Marshmallow serialization and deserialization.

### Features:
* GET, POST, and DELETE endpoints
* Table and column management
* Relationships and association proxies
* Validation at both the SQLAlchemy and schema levels
* Seeder to generate useful demonstration data
* Marshmallow serialization of database entries
* Marshmallow deserialization of JSON data received from API

## Installation
- Fork and clone the GitHub repository.
- From a terminal in the repo folder, run `pipenv install` and `pipenv shell`
- `cd` to the server folder, and run `flask db upgrade` to generate a database file. Then run `python3 seed.py` to fill it with seed data.
- To test database directly: run `flask shell` to enter commands as if operating from within the Flask app.
- To test full API: run `flask run` and use your preferred API testing tool to send GET, POST, and DELETE commands. Routes and data formats below.

## Routes
**GET**
* `/` Returns a simple welcome message
* `/api/health` Confirms API is running
* `/workouts` Lists all workouts
* `/workouts/<id>` Shows specified workout
* `/exercises` Lists all exercises
* `/exercises/<id>` Shows specified exercise

**POST**
* `/workouts` Posts a new workout. Fields:
  * `duration_minutes`: Integer; number of minutes of full workout
  * `notes`: String, optional
* `/exercises` Posts a new exercise. Format:
  * `name`: String
  * `category`: String
  * `equipment_needed`: Boolean, optional
* `/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` Adds an exercise to a workout. Format:
  * `reps`: Integer
  * `sets`: Integer
  * `duration_seconds`: Integer; duration of individual exercise within larger workout
 
**DELETE**
* `/workouts/<id>` Deletes specified workout
* `/exercises/<id>` Deletes specified exercise
