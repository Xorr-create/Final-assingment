import sys
from datetime import timedelta

def analyze_cat_shelter_log(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        cat_visits = 0
        total_time_in_house = 0
        visit_lengths = []

        for line in lines:
            if line.startswith("OURS"):
                cat_visits += 1
                entry_time, exit_time = map(int, line.split(",")[1:])
                visit_duration = exit_time - entry_time
                total_time_in_house += visit_duration
                visit_lengths.append(visit_duration)

        other_cats = len(lines) - cat_visits

        average_visit_length = timedelta(minutes=sum(visit_lengths) // len(visit_lengths))
        longest_visit = timedelta(minutes=max(visit_lengths))
        shortest_visit = timedelta(minutes=min(visit_lengths))

        print("Log File Analysis")
        print("==================")
        print(f"Cat Visits: {cat_visits}")
        print(f"Other Cats: {other_cats}")
        print(f"Total Time in House: {str(timedelta(minutes=total_time_in_house))}")

        print("\nFor the correct cat:")
        print(f"Average Visit Length: {str(average_visit_length)}")
        print(f"Longest Visit: {str(longest_visit)}")
        print(f"Shortest Visit: {str(shortest_visit)}")

    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        log_file_path = sys.argv[1]
        analyze_cat_shelter_log(log_file_path)
import sys
from datetime import timedelta

def analyze_cat_shelter_log(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        cat_visits = [line.split(",")[1:] for line in lines if line.startswith("OURS")]
        other_cats = len(lines) - len(cat_visits)

        visit_lengths = [exit_time - entry_time for entry_time, exit_time in cat_visits]
        total_time_in_house = sum(visit_lengths)

        average_visit_length = timedelta(minutes=sum(visit_lengths) // len(visit_lengths))
        longest_visit = timedelta(minutes=max(visit_lengths))
        shortest_visit = timedelta(minutes=min(visit_lengths))

        print("Log File Analysis")
        print("==================")
        print(f"Cat Visits: {len(cat_visits)}")
        print(f"Other Cats: {other_cats}")
        print(f"Total Time in House: {str(timedelta(minutes=total_time_in_house))}")

        print("\nFor the correct cat:")
        print(f"Average Visit Length: {str(average_visit_length)}")
        print(f"Longest Visit: {str(longest_visit)}")
        print(f"Shortest Visit: {str(shortest_visit)}")

    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        log_file_path = sys.argv[1]
        analyze_cat_shelter_log(log_file_path)
