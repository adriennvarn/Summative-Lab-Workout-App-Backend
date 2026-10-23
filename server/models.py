from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean, default=False)

    #  Relationships
    workout_exercises = db.relationship("WorkoutExercise", back_populates="exercise")
    workouts = association_proxy(
        "workout_exercises",
        "workout",
        creator=lambda workout_obj: WorkoutExercise(workout=workout_obj),
    )
    
    #  Validators
    @validates("name")
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name required.")
        if len(name) not in range(6, 26):
            raise ValueError("Name must be between 6 and 25 characters.")
        return name
    
    @validates("category")
    def validate_category(self, key, category):
        if not category:
            raise ValueError("Category required.")
        if not isinstance(category, str):
            raise ValueError("Category must be a valid string.")
        return category


class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, server_default=db.func.now())
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.Text)

    #  Relationships
    workout_exercises = db.relationship(
        "WorkoutExercise", back_populates="workout", cascade="all, delete-orphan"
    )
    exercises = association_proxy(
        "workout_exercises",
        "exercise",
        creator=lambda exercise_obj: WorkoutExercise(exercise=exercise_obj),
    )
    
    #  Validators
    @validates("duration_minutes")
    def validate_duration(self, key, duration):
        if not duration:
            raise ValueError("Duration required.")
        if not isinstance(duration, int):
            raise ValueError("Duration must be a valid integer.")
        if not duration > 0:
            raise ValueError("Duration must be greater than 0 minutes.")
        return duration


class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    #  Foreign keys
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"))
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"))

    #  Relationships
    workout = db.relationship("Workout", back_populates="workout_exercises")
    exercise = db.relationship("Exercise", back_populates="workout_exercises")

    #  Validators
    @validates("reps")
    def validate_reps(self, key, reps):
        if not reps:
            raise ValueError("Number of reps is required.")
        if not isinstance(reps, int):
            raise ValueError("Number of reps must be a valid integer.")
        if not reps > 0:
            raise ValueError("Number of reps must be greater than 0.")
        return reps
    
    @validates("sets")
    def validate_reps(self, key, sets):
        if not sets:
            raise ValueError("Number of sets is required.")
        if not isinstance(sets, int):
            raise ValueError("Number of sets must be a valid integer.")
        if not sets > 0:
            raise ValueError("Number of sets must be greater than 0.")
        return sets

    @validates("duration_seconds")
    def validate_duration(self, key, duration):
        if not duration:
            raise ValueError("Duration required.")
        if not isinstance(duration, int):
            raise ValueError("Duration must be a valid integer.")
        if not duration > 0:
            raise ValueError("Duration must be greater than 0 seconds.")
        return duration