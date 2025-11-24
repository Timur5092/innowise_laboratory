students = []

def find_student(students, name):
    """Return student dictionary by name or None."""
    for s in students:
        if s["name"].strip().lower() == name.strip().lower():
            return s
    return None


def safe_average(grades):
    """Return average value or None if list is empty."""
    if not grades:
        return None
    return sum(grades) / len(grades)


def print_menu():
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")


def add_student(students):
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if find_student(students, name):
        print(f"Student '{name}' already exists.")
        return
    students.append({"name": name, "grades": []})
    print(f"Added student '{name}'.")


def add_grades(students):
    name = input("Enter student name: ").strip()
    student = find_student(students, name)
    if not student:
        print(f"Student '{name}' not found.")
        return

    print("Enter grades as integers (or 'done' to finish).")
    while True:
        raw = input("Enter a grade (or 'done'): ").strip().lower()
        if raw == "done":
            break
        try:
            grade = int(raw)
            if grade < 0:
                print("Grade cannot be negative.")
                continue
            student["grades"].append(grade)
            print(f"Added grade {grade} for {student['name']}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_report(students):
    print("\n--- Student Report ---")
    if not students:
        print("No students added yet.")
        return

    averages = []
    for s in students:
        avg = safe_average(s["grades"])
        averages.append((s["name"], avg))
        if avg is None:
            print(f"{s['name']}'s average grade is N/A.")
        else:
            print(f"{s['name']}'s average grade is {avg:.2f}.")

    print("-" * 26)
    valid_avgs = [avg for _, avg in averages if avg is not None]
    if not valid_avgs:
        print("No grades available to compute summary.")
        return

    max_avg = max(valid_avgs)
    min_avg = min(valid_avgs)
    overall_avg = sum(valid_avgs) / len(valid_avgs)
    print(f"Max Average: {max_avg:.2f}")
    print(f"Min Average: {min_avg:.2f}")
    print(f"Overall Average: {overall_avg:.2f}")


def find_top_student(students):
    if not students:
        print("No students added yet.")
        return

    students_with_avg = [
        (s, safe_average(s["grades"])) for s in students if safe_average(s["grades"]) is not None
    ]
    if not students_with_avg:
        print("No grades available to determine top student.")
        return

    top_student, top_avg = max(students_with_avg, key=lambda sa: sa[1])
    print(f"Top performer is {top_student['name']} with an average of {top_avg:.2f}.")


def main():
    students = []
    while True:
        print_menu()
        choice_raw = input("Enter your choice: ").strip()
        try:
            choice = int(choice_raw)
        except ValueError:
            print("Invalid choice. Please enter a number 1-5.")
            continue

        if choice == 1:
            add_student(students)
        elif choice == 2:
            add_grades(students)
        elif choice == 3:
            generate_report(students)
        elif choice == 4:
            find_top_student(students)
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Unknown choice. Please select 1-5.")


if __name__ == "__main__":
    main()
