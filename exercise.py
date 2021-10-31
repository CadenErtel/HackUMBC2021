import sqlite3

conn = sqlite3.connect('exercises.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS exercises (name text PRIMARY KEY, sets integer NOT NULL, reps integer NOT NULL, working_group text NOT NULL)')

class Exercise():
    
    def __init__(self, name, set, reps, group):
        self.name = name
        self.set = set
        self.reps = reps
        self.group = group

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

exercises = [data.strip() for data in """
    Squats, leg,
    Leg Press, leg,
    Romaninian Deadlift, leg,
    Leg Curl, leg,
    Hip Thrusts, leg,
    Calf Raises, leg,
    Front Squat, leg,
    Hack Squat, leg,
    Single Leg Extension, leg,
    Goblet Squat, leg,
    Bulgarian Split Squat, leg,
    Bench Press, push,
    Incline DB Press, push,
    Cable Fly, push,
    Tricep Extension, push,
    Skullcrushers, push,
    DB Lateral Raise, push,
    Machine Lateral Raise, push,
    Incline Barbell Bench, push,
    Flat DB Press, push,
    DB Shoulder press, push,
    Cable Lateral Raise, push,
    Dips, push,
    Overhead Tricep Extension, push,
    Deadlift, pull,
    Pullups, pull,
    Barbell Row, pull,
    Lateral Pulldown, pull,
    Chest Assisted Row, pull,
    DB Bicep Curl, pull,
    Incline DB Curl, pull,
    DB Preacher Curl, pull,
    Rear Delt Flys, pull,
    DB Rear Delt Fly, pull,
    Face Pulls, pull
""".split(',')]

groups = exercises[1::2]
exercises_2 = exercises[::2]

def fill_tables():
    for i in range(len(exercises_2)):
        cursor.execute('INSERT INTO exercises VALUES (?,?,?,?)', (exercises_2[i], 0, 0, groups[i]))
        conn.commit()

def main():
    fill_tables()

if __name__ == '__main__':
    main()