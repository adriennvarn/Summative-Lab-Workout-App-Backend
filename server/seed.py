from random import choice as rc, randint as ri

from app import app
from models import db, Workout, Exercise, WorkoutExercise

with app.app_context():
    Workout.query.delete()
    Exercise.query.delete()
    WorkoutExercise.query.delete()

    notes = [
        "worked up a serious sweat",
        "spend longer than usual today",
        "should have cut it off sooner",
        "i'm tired...",
    ]

    workouts = []
    for n in range(10):
        wo = Workout(duration_minutes=ri(5, 60), notes=rc(notes))
        workouts.append(wo)
        
    db.session.add_all(workouts)

    exercise_names = ["squats", "chin ups", "dumbell lifts", "leg raises"]
    categories = ["leg day", "arm day", "core day", "full body"]

    exercises = []
    for n in range(10):
        ex = Exercise(
            name=rc(exercise_names),
            category=rc(categories),
            equipment_needed=rc([True, False]),
        )
        exercises.append(ex)
    
    db.session.add_all(exercises)

    workout_exercises = []
    for n in range(10):
        we = WorkoutExercise(
            reps=ri(2, 6),
            sets=ri(2, 6),
            duration_seconds=ri(30, 120),
            workout_id=rc(workouts),
            exercise_id=rc(exercises),
        )
        workout_exercises.append(we)
    
    db.session.add_all(workout_exercises)
    
    db.session.commit()

