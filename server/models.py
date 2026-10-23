from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean, default=False)

    # relationships: 
    # has many workout exercises
    # has many workouts through workout exercises

class Workout(db.Model):
    __tablename__ = "workouts"
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, server_default=db.func.now())
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.Text)
    
    # relationships:
    # has many workout exercises
    # has many exercises through workout exercises
    
class WorkoutExercises(db.Model):
    __tablename__ = "workout_exercises"
    
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"))
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"))
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)
    
    # relationships
    # belongs to a workout
    # belongs to an exercise
    # association table between the two