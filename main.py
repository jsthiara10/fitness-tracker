def main():
    print("Welcome to JST's fitness app")
    tracker()

workout_session = []

# def tracker(): # OLD, WORKING
#     global workout_session
#     exercise = input(f"Enter an exercise: ")
#     workout_session.append(exercise)
#     set_number = input(f"Enter set number: ")
#     workout_session.append(set_number)
#     weight_lifted_kg = input(f"Enter weight lifted in kgs: ")
#     workout_session.append(weight_lifted_kg)
#     reps = input(f"Enter reps performed: ")
#     workout_session.append(reps)
#     rest_time = input(f"Enter rest time taken: ")
#     workout_session.append(rest_time)
#     print("Workout complete! You did the following in this workout" , workout_session )

def tracker():
    global workout_session
    while True:
        exercise = input("Enter an exercise: ")
        # workout_session.append(exercise)
        if not exercise:
            print("Please enter a valid exercise ")
            continue

        while True:
            try:
                set_number = int(input(f"Enter set number for {exercise}"))
                if set_number < 0:
                    print("Set number must be a valid number e.g. 1")
                else:
                    workout_session.append(set_number)
                    break # if they enter a valid set number, this particular while loop will be broken
            except ValueError: # if they enter a non-integer e.g. a string
                print ("You must enter a number e.g. 1")

print("You completed the following", [workout_session])


main()

# this does a basic append to the function 

# long term functionality - add multiple exercises, sets;  - error handling e.g. if the user inputs an incorrect value 