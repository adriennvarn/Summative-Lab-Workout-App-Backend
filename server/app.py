from flask import Flask, make_response, request
from flask_migrate import Migrate
from marshmallow import ValidationError
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route("/api/health")
def health_check():
    return make_response({"status": "ok"}, 200)


@app.route("/")
def index():
    return "<h1>Welcome to Workout API Lab</h1>"


@app.get("/workouts")
def get_all_workouts():
    workouts = Workout.query.all()
    if workouts:
        body = WorkoutSchema(many=True).dump(workouts)
        status = 200
    else:
        body = {"error": "No workouts found."}
        status = 404

    return make_response(body, status)


@app.get("/workouts/<int:id>")
def get_workout_by_id(id):
    workout = Workout.query.filter_by(id=id).first()
    if workout:
        body = WorkoutSchema().dump(workout)
        status = 200
    else:
        body = {"error": f"No workout ID {id} found."}
        status = 404

    return make_response(body, status)


@app.post("/workouts")
def add_workout():
    data = request.get_json()
    try:
        workout = WorkoutSchema().load(data)
        db.session.add(workout)
        db.session.commit()
        body = {"message": "success"}
        status = 201
    except ValidationError as err:
        body = {"validation error": f"{err}"}
        status = 400

    return make_response(body, status)


@app.delete("/workouts/<int:id>")
def delete_workout(id):
    workout = Workout.query.filter_by(id=id).first()
    if workout:
        db.session.delete(workout)
        db.session.commit()
        body = {}
        status = 204
    else:
        body = {"error": f"No workout ID {id} found."}
        status = 404

    return make_response(body, status)


@app.get("/exercises")
def get_all_exercises():
    exercises = Exercise.query.all()
    if exercises:
        body = ExerciseSchema(many=True).dump(exercises)
        status = 200
    else:
        body = {"error": "No exercises found."}
        status = 404

    return make_response(body, status)


@app.get("/exercises/<int:id>")
def get_exercise_by_id(id):
    exercise = Exercise.query.filter_by(id=id).first()
    if exercise:
        body = ExerciseSchema().dump(exercise)
        status = 200
    else:
        body = {"error": f"No exercise ID {id} found."}
        status = 404

    return make_response(body, status)


@app.post("/exercises")
def add_exercise():
    data = request.get_json()
    try:
        exercise = ExerciseSchema().load(data)
        db.session.add(exercise)
        db.session.commit()
        body = {"message": "success"}
        status = 201
    except ValidationError as err:
        body = {"validation error": f"{err}"}
        status = 400

    return make_response(body, status)


@app.delete("/exercises/<int:id>")
def delete_exercise(id):
    exercise = Exercise.query.filter_by(id=id).first()
    if exercise:
        db.session.delete(exercise)
        db.session.commit()
        body = {}
        status = 204
    else:
        body = {"error": f"No exercise ID {id} found."}
        status = 404

    return make_response(body, status)


@app.post("/workouts/<int:wo_id>/exercises/<int:ex_id>/workout_exercises")
def add_exercise_to_workout(wo_id, ex_id):
    workout = Workout.query.filter_by(id=wo_id).first()
    exercise = Exercise.query.filter_by(id=ex_id).first()
    if not workout:
        body = {"error": f"No workout ID {wo_id} found."}
        status = 404
    elif not exercise:
        body = {"error": f"No exercise ID {ex_id} found."}
        status = 404
    else:
        data = request.get_json()
        try:
            workout_exercise = WorkoutExerciseSchema().load(data)
            workout_exercise.workout = workout
            workout_exercise.exercise = exercise
            db.session.add(workout_exercise)
            db.session.commit()
            body = {"message": "success"}
            status = 201
        except ValidationError as err:
            body = {"validation error": f"{err}"}
            status = 400
    
    return make_response(body, status)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
