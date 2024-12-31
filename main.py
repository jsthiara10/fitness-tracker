# Python Fitness Tracker

# The Python Fitness Tracker allows the user to record their exercise, set number, weight lifted, reps and rest time.

workout_session = [] # global list to store variable data e.g. sets, reps

def tracker(): # User inputs exercise 
    global workout_session # functions can access the global list so long as you call it at the beginning of the function
    while True:
        exercise = input("Enter an exercise: ")
        if not exercise: # Put the IF NOT statement first so that we can catch empty input early
            print("Please enter a valid exercise ")
            continue # the loop continues - it skips everything below this 'continue' statement as it will re-prompt the user to enter something
        elif exercise: # so if they do enter an exercise. always put th
            workout_session.append(exercise)
            break
    set_number(exercise)

def set_number(exercise): # User inputs set number 
    global workout_session
    while True:
        try:
            set_number = int(input(f"Enter set number for {exercise}: "))
            if set_number <= 0:
                print("Set number must be a valid number e.g. 1")
                continue
            elif set_number > 0:
                workout_session.append(set_number)
                break
        except ValueError:
            print("You must enter a number e.g. 1")

    weight_lifted_kg(exercise, set_number) # position function call OUTSIDE of the while loop

    
def weight_lifted_kg(exercise, set_number): # User inputs weight lifted 
    global workout_session
    while True:
        try:
            weight_lifted_kg = float(input(f"Enter weight lifted (kg) for Set {set_number} of {exercise}: "))
            if weight_lifted_kg < 0:
                print("Weight lifted must be greater than 0")
                continue
            elif weight_lifted_kg >=0:
                workout_session.append(weight_lifted_kg)
                break
        except ValueError:
            print("You must enter a number e.g. 1")

    repetitions(exercise, set_number, weight_lifted_kg)

def repetitions(exercise, set_number, weight_lifted_kg): # User inputs reps performed for input exercise and respective set number 
    global workout_session
    while True:
        try:
            repetitions = float(input(f"Enter the number of repetitions performed at {weight_lifted_kg} kg for Set {set_number} of {exercise}: "))
            if repetitions < 0:
                print("Repetitions performed must be greater than or equal to 0")
                continue
            elif repetitions >=0:
                workout_session.append(repetitions)
                break
        except ValueError:
            print("You must enter number of repetitions e.g. 10 or 10.5")

    rest_time(exercise, set_number) # no need to pass through weight lifted or repetitions, as we are not accessing those in the rest_time function

def rest_time(exercise, set_number): # user inputs rest time taken after their set 
    global workout_session
    while True:
        try:
            rest_time = float(input(f"Enter the rest time for Set {set_number} of {exercise} in seconds (s): "))
            if rest_time < 0:
                print("Rest time must be greater than or equal to 0")
                continue
            elif rest_time >= 0:
                workout_session.append(rest_time)
                break
        except ValueError:
            print("You must enter the rest time in seconds (s): ")
    new_record()

def new_record(): # if the user wants to input a new record i.e. new exercise or another set(s) of the same exercise 
    while True:
        try:
            new_record = input(f"Enter another exercise? Y/N: ").upper()
            if new_record == "N":
                break # if they don't want to enter a new exercise, break out of the while loop and return to the main function
            elif new_record == "Y":
                tracker() # if they do enter a new exercise, return to the tracker function
        except ValueError:
            print("You must enter Y or N: ")

        break # break out of the while loop 


def main():
    print("Welcome to JST's Fitness App")
    tracker()
    print("You completed the following", [workout_session])

main() # start of the program


# long term functionality - add multiple exercises, sets;  - error handling e.g. if the user inputs an incorrect value 