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
        if not exercise: # Put the IF NOT statement first so that we can catch empty input early
            print("Please enter a valid exercise ")
            continue # the loop continues - it skips everything below this 'continue' statement as it will re-prompt the user to enter something
        elif exercise: # so if they do enter an exercise. always put th
            workout_session.append(exercise)

        while True:
            try:
                set_number = int(input(f"Enter set number for {exercise}: "))
                if set_number <= 0:
                    print("Set number must be a valid number e.g. 1")
                    continue
                elif set_number > 0:
                    workout_session.append(set_number)
            except ValueError:
                print("You must enter a number e.g. 1")

            # while True:
            #     try:
            #         weight_lifted_kg = float(input(f"Enter the weight lifted for {exercise}"))
            #         if weight_lifted_kg < 0.0:
            #             print("Weight lifted must be at least 0kg")
            #         elif weight_lifted_kg >=0.0:
            #             workout_session.append(weight_lifted_kg)
            #     except ValueError:
            #             print("You must enter a number e.g. 10 or 10.5")
                        
            #     break # break out of the initial outer loop 

            # break


def main():
    tracker()
    print("You completed the following", [workout_session])

main()

# this does a basic append to the function 

# long term functionality - add multiple exercises, sets;  - error handling e.g. if the user inputs an incorrect value 