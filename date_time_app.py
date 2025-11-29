from datetime import datetime, timedelta

def show_date():
    today = datetime.now().strftime("%d-%m-%Y")
    print("Today's Date:", today)

def show_time():
    now = datetime.now().strftime("%H:%M:%S")
    print("Current Time:", now)

def add_days():
    days = int(input("Enter number of days to add: "))
    future = datetime.now() + timedelta(days=days)
    print("Date After", days, "Days :", future.strftime("%d-%m-%Y"))

def main():
    while True:
        print("\n--- Date & Time Application ---")
        print("1. Show Today's Date")
        print("2. Show Current Time")
        print("3. Add Days to Today's Date")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_date()
        elif choice == '2':
            show_time()
        elif choice == '3':
            add_days()
        elif choice == '4':
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice! Try again.")

main()