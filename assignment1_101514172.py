"""
Author: Nishi Bipin Mehta
Assignment: #1
"""

# Variables
gym_member = "Alex Alliton"  # str
preferred_weight_kg = 20.5  # float
highest_reps = 25  # int
membership_active = True  # bool

# Dictionary to store workout stats
# Data type: dict
# (yoga, running, weightlifting)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 40, 50),
    "Taylor": (20, 60, 30),
    "Arthur": (35, 30, 25),
    "Laila": (25, 30, 40)
}

# Create a separate dictionary to store total workout minutes
total_minutes_dict = {}

# Calculate total workout minutes for each friend and store in a separate dictionary
for friend, minutes in workout_stats.items():
    total_minutes = sum(minutes)
    total_minutes_dict[friend] = total_minutes

# Add total minutes to the original dictionary
for friend, total in total_minutes_dict.items():
    workout_stats[f"{friend}_Total"] = total

# Create a 2-dimensional (nested) list for workout minutes
# Data type: list of lists
workout_list = [list(minutes) for minutes in workout_stats.values() if isinstance(minutes, tuple)]

# Extract and print the minutes for yoga and running for all friends
yoga_running_minutes = [row[:2] for row in workout_list]  # Extracting yoga and running
print("\nYoga and Running Minutes for all friends:")
for friend, minutes in zip(workout_stats.keys(), yoga_running_minutes):
    print(f"{friend}: Yoga: {minutes[0]}, Running: {minutes[1]}")

# Extract and print the minutes for weightlifting for the last two friends
print("\nWeightlifting Minutes for the last two friends:")
# Get the last two friends from the original workout_stats keys (without _Total)
original_friends = [friend for friend in workout_stats.keys() if not friend.endswith('_Total')]
last_two_friends = original_friends[-2:]  # Get the last two original friends

for friend in last_two_friends:
    print(f"{friend}: Weightlifting: {workout_stats[friend][2]}")

# Check if any friend's total workout minutes are greater than or equal to 120
for friend in total_minutes_dict.keys():
    if total_minutes_dict[friend] >= 120:
        print(f"\n{friend}'s total workout minutes: {total_minutes_dict[friend]}")
        print(f"Great job staying active, {friend}!")

# User input for friend's name
friend_name = input("\nEnter a friend's name: ")
if friend_name in workout_stats:
    minutes = workout_stats[friend_name]
    total_minutes = total_minutes_dict[friend_name] if friend_name in total_minutes_dict else 0
    print(f"{friend_name}'s workout minutes: Yoga: {minutes[0]}, Running: {minutes[1]}, Weightlifting: {minutes[2] if isinstance(minutes, tuple) else 0}")
    print(f"Total workout minutes: {total_minutes}")
else:
    print(f"Friend {friend_name} not found in the records.")

# Print the friend with the highest and lowest total workout minutes
highest_friend = max(total_minutes_dict, key=total_minutes_dict.get)
lowest_friend = min(total_minutes_dict, key=total_minutes_dict.get)

print(f"\nFriend with the highest total workout minutes: {highest_friend} ({total_minutes_dict[highest_friend]} minutes)")
print(f"Friend with the lowest total workout minutes: {lowest_friend} ({total_minutes_dict[lowest_friend]} minutes)")
