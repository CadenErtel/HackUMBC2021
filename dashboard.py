import streamlit as st
from streamlit_player import st_player
import sqlite3
from PIL import Image
from datetime import datetime
import pandas as pd
import numpy as np

############################# CONSTANTS/GLOBALS ##############################

workouts = ('General Fitness', 'Push, Pull, Legs', 'HIIT', 'Marathon Prep', 'Weight Loss')
weights = tuple(range(21, 401))
height_ft = tuple(range(0,8))
height_in = tuple(range(0,12))
ages = tuple(range(0,111))

conn = sqlite3.connect('exercises.db')
cursor = conn.cursor()

exercises = []
legs = []
push = []
pull = []

############################ CLASSES #######################################

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

############################ PAGES #########################################

def home_page():
    
    st.set_page_config(layout="wide")
    create_objects()

    pages = {
        "Weekly Fitness Plan": current_goals,
        "Calendar": calendar,
        "Friends": friends,
        "Health and Safety": hands,
        "Nutrition":nutrition
    }

    st.sidebar.title("Select a Page")
    page = st.sidebar.selectbox("Select your page", tuple(pages.keys()))
    if page == 'Calendar' or page == 'Weekly Fitness Plan':
        st.session_state.workout = st.sidebar.selectbox("Choose your Fitness Plan", workouts)

    # Display the selected page
    pages[page]()

def current_goals():
    st.markdown("<h1 style='text-align: center; color: white; font-size: 72px; font-family: Andale Mono,AndaleMono,monospace;'>Weekly Fitness Plan</h1>", unsafe_allow_html=True)
    sun, mon, tues, wed, thur, fri, sat = st.columns(7)
    daily_workouts = generate_workouts(st.session_state.workout, False)

    with sun:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Sunday</h1>", unsafe_allow_html=True)
        st.markdown(string_to_p(daily_workouts['sun']), unsafe_allow_html=True)
    with mon:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Monday</h1>", unsafe_allow_html=True)
        st.markdown(string_to_p(daily_workouts['mon']), unsafe_allow_html=True)
    with tues:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Tuesday</h1>", unsafe_allow_html=True)
        st.markdown(string_to_p(daily_workouts['tue']), unsafe_allow_html=True)
    with wed:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Wednesday</h1>", unsafe_allow_html=True)
        st.markdown(string_to_p(daily_workouts['wed']), unsafe_allow_html=True)
    with thur:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Thursday</h1>", unsafe_allow_html=True)
        st.markdown(string_to_p(daily_workouts['thur']), unsafe_allow_html=True)
    with fri:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Friday</h1>", unsafe_allow_html=True)
        st.markdown(string_to_p(daily_workouts['fri']), unsafe_allow_html=True)
    with sat:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 24px; font-family: Andale Mono,AndaleMono,monospace;'>Saturday</h1>", unsafe_allow_html=True)
        st.markdown(string_to_p(daily_workouts['sat']), unsafe_allow_html=True)

def friends():
    st.markdown("<h1 style='text-align: center; color: white; font-size: 72px; font-family: Andale Mono,AndaleMono,monospace;'>Friends</h1>", unsafe_allow_html=True)
    st.image('simu-liu.png')
    st.image('Dancing-Simu-Liu.jpg')
    st.image('serious.png')
    st.image('shrek.jpg')
    st.image('yoda.jpg')
    st.image('yoga.png')

def calendar():
    st.markdown("<h1 style='text-align: center; color: white; font-size: 72px; font-family: Andale Mono,AndaleMono,monospace;'>Calendar</h1>", unsafe_allow_html=True)
    dateInput = st.date_input("Which date would you like to view your fitness plan?")
    day = dateInput.weekday()
    daily_workouts = generate_workouts(st.session_state.workout, True)
    if(day == 0):
        st.title("Monday Fitness Plan")
        daily_workouts['mon']
        if daily_workouts['mon'] == 'Run':
            st.image('officer-police.gif')
    elif(day == 1):
        st.title("Tuesday Fitness Plan")
        daily_workouts['tue']
        if daily_workouts['tue'] == 'Run':
            st.image('officer-police.gif')
    elif(day == 2):
        st.title("Wedesday Fitness Plan")
        daily_workouts['wed']
        if daily_workouts['wed'] == 'Run':
            st.image('officer-police.gif')
    elif(day == 3):
        st.title("Thursday Fitness Plan")
        daily_workouts['thur']
        if daily_workouts['thur'] == 'Run':
            st.image('officer-police.gif')
    elif(day == 4):
        st.title("Friday Fitness Plan")
        daily_workouts['fri']
        if daily_workouts['fri'] == 'Run':
            st.image('officer-police.gif')
    elif(day == 5):
        st.title("Saturday Fitness Plan")
        daily_workouts['sat']
        if daily_workouts['sat'] == 'Run':
            st.image('officer-police.gif')
    elif(day == 6):
        st.title("Sunday Fitness Plan")
        daily_workouts['sun']
        if daily_workouts['sun'] == 'Run':
            st.image('officer-police.gif')
    
def hands():
    st.markdown("<h1 style='text-align: center; color: white; font-size: 34px; font-family: Andale Mono,AndaleMono,monospace;'>Health and Safety</h1>", unsafe_allow_html=True)
    option = st.selectbox( 'Which exercice are you interested in?', ('Bench Press', 'Burpees', 'Deadlifts', 'Planks', 'Push ups', 'Pull ups', 'Squats', 'Lunges'))
    main_container = st.container()
    
    if (option == 'Burpees'):
        st_player("https://www.youtube.com/watch?v=tJrdJBWBu08", key='youtube_player')
        main_container.markdown("<ul style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>\
        <li>This exercise targets the muscles in your legs, hips, buttocks, abdomen, arms, chest, and shoulders.</li><li> Don't do a full push up</li>\
        <li>Land on your heels</li> <li>Don't forget to breathe</li> <li>Stay in form</li>", unsafe_allow_html=True)
    elif (option == 'Push ups'):
        st_player("https://www.youtube.com/watch?v=IODxDxX7oi4")
        main_container.markdown("<ul style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>\
        <li>This exercise targets the chest, shoulders, and triceps and work your core, back, and legs</li>\
        <li>Make sure your neck and spine are aligned</li>\
        <li>Bring your hands towards your toes</li>\
        <li>Don’t let gravity do the work for you</li>\
        <li>Have a strong grip on the floor</h1>", unsafe_allow_html=True)
    elif (option == 'Pull ups'):
        st_player("https://www.youtube.com/watch?v=eGo4IYlbE5g")
        main_container.markdown("<ul style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>\
        <li>This exercise targets the back muscles. </li>\
        <li> Move slowly upward until your chin is above the bar, then equally slowly downward until your arms are extended again.</l1>\
        <li>Keep your shoulders back and your core engaged throughout. Then pull up. Focus on enlisting every upper body muscle to aid your upward endeavours.</l1>\
        <li>Have a strong grip on the floor</li>", unsafe_allow_html=True)
    elif (option =='Squats'):
        st_player("https://www.youtube.com/watch?v=YaXPRqUwItQ")
        main_container.markdown("<ul style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>\
        <li>This exercise targets quadriceps, hamstrings, glutes, abdominals, calves</li>\
        <li>Move slowly upward until your chin is above the bar, then equally slowly downward until your arms are extended again.</li>\
            <li>Take A Pause When You Get Parallel</li>\
        <li>Keep The Spine Neutral: Avoid rounding your back or shoulders</li>\
        <li>Only Squat What You Can Handle and with good form</li> ", unsafe_allow_html=True)
    elif (option == 'Planks'):
        st_player("https://www.youtube.com/watch?v=B296mZDhrP4")
        main_container.markdown("<ul style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;' >\
        <li>This exercise targets the core, reduces back pain, improve stability and builds endurance</li>\
        <li>Get into pushup position. For a high plank, your arms should be fully extended. If you’re a beginner, you can start by doing a plank on your knees. If you’re more advanced, you can try one on your forearms for more of a challenge.</li>\
        <li> Keep your palms and toes firmly planted on the ground, your back straight, and your core tight.</li>\
        <li>Make sure your body is in a straight line while you’re in plank position. Don’t let your back or head sag</li>\
        <li>Hold your plank for the predetermined time. If your form begins to go at any point, drop to your knees or stop until you’re ready to return to plank position.</li>", unsafe_allow_html=True)
    elif (option == 'Lunges'):
        st_player('https://www.youtube.com/watch?v=QOVaHwm-Q6U')
        main_container.markdown("<ul style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;' >\
        <li>This exercise strengthen the leg muscles as well as the core, hips, and glutes</li>\
        <li>Walking lunges can help increase your range of motion by helping to increase flexibility, and loosen up your hips and hamstring</li>\
        <li>Lunges mimic movements you do every day like standing up, sitting, and stepping forward to pick something up off the floor. Practicing walking lunges regularly can help make these everyday movements easier in real life.</li>\
        <li>Keep your body upright through the movement. Try to avoid leaning forward too much</li>\
        <li>Don’t overextend your leg when you lunge forward, which can cause your back to arch.</li>", unsafe_allow_html=True)
    elif (option == 'Bench Press'):
        st_player('https://www.youtube.com/watch?v=vthMCtgVtFw')
        main_container.markdown("<ul style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;' >\
        <li>Bench press is a exercise that mainly works your pecs – a.k.a. chest muscle – and your triceps, but it also utilises a range of other muscles on your upper body too, including the delts (shoulders), forearms, core and more</li>\
        <li>Keep a tight grip on the bar at all times, a tighter grip equates to more tension in the lower arms, upper back and chest.</li>\
        <li>Keep your chest up (thoracic extension) throughout the movement.</li>\
        <li>Elbows should be tucked and end up at approximately 45 degrees from your side</li>\
        <li>When you touch your chest, drive your feet downward and reverse the movement.</li>", unsafe_allow_html=True)
    elif (option == 'Deadlifts'):
        st_player('https://www.youtube.com/watch?v=hCDzSR6bW10')
        main_container.markdown("<ul style='text-align: left; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;' >\
        <li>This exercise targets glutes, hamstrings, lower back muscles, upper back muscles, quads, and most importantly the core.</li>\
        <li>Keep the bar as close to your body as possible.</li>\
        <li>Check your form before you start the lift: neutral spine, chest up, knees out.</li>\
        <li>Do not hyperextend at top of the movement.</li>\
        <li>Complete the lift with a hinging movement — it’s not a squat. tand up from your strong starting position and lower the bar back down </li>", unsafe_allow_html=True)

def nutrition():
    st.title("Select Your Nutrition Goal")
    activity_levels = {
        "Sedentary (little or no exercise)":"sedentary",
        "Lightly active (lightly exercise/sports 1-3 days/week)":"light",
        "Moderately active (moderate exercise/sports 3-5 days/week)":"moderate",
        "Very active (hard exercise/sports 6-7 days a week)":"very",
        "extra active (very hard exercise/sports & physical job or 2x training)":"extra"
    }
    col1, col2 , _ = st.columns(3)
    with col1:
        goal = st.selectbox('Select Your Nutrition Goal', ('Maintain', 'Cut', 'Bulk'))
        gender = st.selectbox('Select a gender',('Male','Female'))
        weight = st.selectbox('Select Weight', weights)
        feet = st.selectbox('Select Height in Feet',height_ft)
        inches = st.selectbox('Select Height in Inches',height_in)
        age = st.selectbox('Select Age',ages)
        activity = st.selectbox('Select Your Level of activity', tuple(activity_levels.keys()))
    
    height = feet*12+inches

    if(gender == 'Male'):
        bmr = 66 + 6.3*weight + 12.9*height - 6.8*age
    else:
        bmr = 655 + 4.3*weight + 4.7*height - 4.7*age
    
    if(activity_levels[activity]=="sedentary"):
        calories = 1.2*bmr
    elif(activity_levels[activity]=="light"):
        calories = 1.375*bmr
    elif(activity_levels[activity]=="moderate"):
        calories = 1.55*bmr
    elif(activity_levels[activity]=="very"):
        calories = 1.725*bmr
    elif(activity_levels[activity]=="extra"):
        calories = 1.9*bmr
    
    carbs = (calories/2)/4
    max_protein =weight
    fat = 0.3*calories/9

    if(goal == 'Bulk'):
        calories = 1.1*calories
        carbs = .4*calories/4
        max_protein = 1.1*max_protein
        fat = calories*.3/4
    elif(goal == 'Cut'):
        maintain_calories = calories
        calories = 0.8*calories
        max_protein = 1.2*weight
        fat = calories*.3/9
        carbs = (maintain_calories-max_protein*4-fat*9)/4

    with col2:
        st.markdown("""<table>
                        <tr> 
                            <th>Macro</th>
                            <th>Grams needed</th>
                        </tr>
                        <tr>
                            <th>Calories</th>
                            <th>""" + str(calories) + """</th>
                        </tr>
                        <tr>
                            <th>Carbs</th>
                            <th>""" + str(carbs) + """</th>
                        </tr>
                        <tr>
                            <th>Protein</th>
                            <th>""" + str(max_protein) + """</th>
                        </tr>
                        <tr>
                            <th>Fat</th>
                            <th>""" + str(fat) + """</th>
                        </tr>
                        </table>
                        """, unsafe_allow_html=True)

def generate_workouts(workout_type, return_obj):
    days = {'sun':'', 'mon':'', 'tue':'', 'wed':'', 'thur':'', 'fri':'', 'sat':'',}

    if not return_obj:
        new_legs = ' '.join([str(data) for data in legs])
        new_pull = ' '.join([str(data) for data in pull])
        new_push = ' '.join([str(data) for data in push])
    else:
        new_legs = legs
        new_pull = pull
        new_push = push

    if workout_type == workouts[0]: # General Fitness
        days['sun'] = new_legs
        days['mon'] = 'Rest Day, You Deserve This!'
        days['tue'] = new_pull
        days['wed'] = 'Run'
        days['thur'] = new_pull
        days['fri'] = 'Rest Day, You Deserve This!'
        days['sat'] = new_push
    elif workout_type == workouts[1]: # Push Pull Legs
        days['sun'] = 'Rest Day, You Deserve This!'
        days['mon'] = new_push
        days['tue'] = new_pull
        days['wed'] = new_legs
        days['thur'] = new_push
        days['fri'] = new_pull
        days['sat'] = new_legs
    elif workout_type == workouts[2]: # HIIT
        days['sun'] = 'Sprints'
        days['mon'] = 'Rest Day, You Deserve This!'
        days['tue'] = new_push
        days['wed'] = new_legs
        days['thur'] = new_legs
        days['fri'] = 'Sprints'
        days['sat'] = new_push
    elif workout_type == workouts[3]: # Marathon Prep
        days['sun'] = 'Run'
        days['mon'] = 'Run'
        days['tue'] = 'Run'
        days['wed'] = 'Rest Day, You Deserve This!'
        days['thur'] = 'Run'
        days['fri'] = 'Run'
        days['sat'] = 'Run'
    elif workout_type == workouts[4]: # Weight Loss
        days['sun'] = 'Sprints'
        days['mon'] = new_push
        days['tue'] = new_push
        days['wed'] = new_legs
        days['thur'] = new_legs
        days['fri'] = 'Sprints'
        days['sat'] = 'Rest Day, You Deserve This!'

    return days

def create_objects():
    cursor.execute('SELECT * FROM exercises')
    all_rows = cursor.fetchall()

    for row in all_rows:
        insert_exercise = Exercise(row[0], row[1], row[2], row[3])
        exercises.append(insert_exercise)

        if row[3] == 'leg':
            legs.append(insert_exercise)
        elif row[3] == 'push':
            push.append(insert_exercise)
        elif row[3] == 'pull':
            pull.append(insert_exercise)

def string_to_p(string):
    return "<h1 style='text-align: center; color: white; font-size: 18px; font-family: Andale Mono,AndaleMono,monospace;'>" + string + "</h1>"

if __name__ == "__main__":
    home_page()