workout_session = []

def tracker():
    global workout_session
    while True:
        exercise = input("Enter an exercise: ")
        if not exercise: # Put the IF NOT statement first so that we can catch empty input early
            print("Please enter a valid exercise ")
            continue # the loop continues - it skips everything below this 'continue' statement as it will re-prompt the user to enter something
        elif exercise: # so if they do enter an exercise. always put th
            workout_session.append(exercise)
            break
    reps(exercise)

def reps(exercise):
    global workout_session
    print(f"Enter reps for {exercise}")
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




#  def reps(exercise):
#     global workout_session
#     while True:
#         try:
#             set_number = int(input(f"Enter set number for {exercise}: "))
#             if set_number <= 0:
#                 print("Set number must be a valid number e.g. 1")
#                 continue
#             elif set_number > 0:
#                 workout_session.append(set_number)
#                 break
#         except ValueError:
#             print("You must enter a number e.g. 1")


def main():
    tracker()
    print("You completed the following", [workout_session])

main()
                    