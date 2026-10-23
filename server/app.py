from flask import Flask, make_response
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# migrate = Migrate(app, db)

# db.init_app(app)

@app.route("/api/health")
def health_check():
    return make_response({"status": "ok"}, 200)

@app.get("/workouts")
def get_all_workouts():
    pass

@app.get("/workouts/<int:id>")
def get_workout_by_id(id):
    pass

@app.post("/workouts")
def add_workout():
    pass

@app.delete("/workouts/<int:id>")
def delete_workout(id):
    """OPTIONAL"""
    pass

@app.get("/exercises")
def get_all_exercises():
    pass

@app.get("/exercises/<int:id>")
def get_exercise_by_id(id):
    pass

@app.post("/exercises")
def add_exercise():
    pass

@app.delete("/exercises/<int:id>")
def delete_exercise(id):
    """OPTIONAL"""
    pass

@app.post("/workouts/<int:wo_id>/exercises/<int:ex_id>/workout_exercises")
def add_exercise_to_workout(wo_id, ex_id):
    pass

if __name__ == '__main__':
    app.run(port=5555, debug=True)