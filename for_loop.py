import random

print("----- Dice Rolling Program -----")

rolls = 20
count_6 = 0
count_1 = 0
two_sixes_in_row = 0
previous_roll = None

for i in range(rolls):
    current_roll = random.randint(1, 6)
    print(f"Roll {i+1}: {current_roll}")

    if current_roll == 6:
        count_6 += 1

    if current_roll == 1:
        count_1 += 1

    if current_roll == 6 and previous_roll == 6:
        two_sixes_in_row += 1

    previous_roll = current_roll

print("\nStatistics:")
print("Number of times rolled 6:", count_6)
print("Number of times rolled 1:", count_1)
print("Number of times two 6s in a row:", two_sixes_in_row)

print("\n----- Jumping Jack Program -----")

total_jumps = 100
done_jumps = 0

for i in range(10):
    done_jumps += 10
    print(f"You completed {done_jumps} jumping jacks.")

    if done_jumps >= total_jumps:
        print("Congratulations! You completed the workout 🎉")
        break

    tired = input("Are you tired? (yes/y or no/n): ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()

        if skip == "yes" or skip == "y":
            print(f"You completed a total of {done_jumps} jumping jacks.")
            break
        else:
            remaining = total_jumps - done_jumps
            print(f"{remaining} jumping jacks remaining.\n")
