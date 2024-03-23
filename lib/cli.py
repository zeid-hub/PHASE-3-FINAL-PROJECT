from functions import (
    list_doctors,
    find_doctor_by_name,
    find_doctor_by_id,
    add_new_doctor,
    dismiss_doctor,
    list_patients,
    find_patient_by_name,
    find_patient_by_id,
    admit_new_patient,
    discharge_patient,
    exit_program
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            list_doctors()
            input("Press ENTER to Continue")
        elif choice == "2":
            find_doctor_by_name()
            input("Press ENTER to Continue")
        elif choice == "3":
            find_doctor_by_id()
            input("Press ENTER to Continue")
        elif choice == "4":
            add_new_doctor()
            input("Press ENTER to Continue")
        elif choice == "5":
            dismiss_doctor()
            input("Press ENTER to Continue")
        elif choice == "6":
            list_patients()
            input("Press ENTER to Continue")
        elif choice == "7":
            find_patient_by_name()
            input("Press ENTER to Continue")
        elif choice == "8":
            find_patient_by_id()
            input("Press ENTER to Continue")
        elif choice == "9":
            admit_new_patient()
            input("Press ENTER to Continue")
        elif choice == "10":
            discharge_patient()
            input("Press ENTER to Continue")
        elif choice == "11":
            exit_program()    
        else:
            print("Invalid choice")


def menu():
    print("1. List all doctors")
    print("2. Find doctor by name")
    print("3. Find doctor by id")
    print("4: Enroll new doctor")
    print("5: Dismiss doctor")
    print("6. List all patients")
    print("7. Find patient by name")
    print("8. Find patient by id")
    print("9: Admit new patient")
    print("10: Discharge patient")
    print("11. Exit the program")
    print("Please select an option:")


if __name__ == "__main__":
    main()    