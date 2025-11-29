import datetime

def get_current_datetime():
    now = datetime.datetime.now()
    print("Current Date and Time:")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def get_custom_datetime():
    year = int(input("Enter year (YYYY): "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))
    hour = int(input("Enter hour (0-23): "))
    minute = int(input("Enter minute (0-59): "))
    second = int(input("Enter second (0-59): "))
    custom_date = datetime.datetime(year, month, day, hour, minute, second)
    print("Custom Date and Time:")
    print(custom_date.strftime("%Y-%m-%d %H:%M:%S"))

def main():
    while True:
        print("\nDate and Time Application")
        print("1. Get Current Date and Time")
        print("2. Enter a Custom Date and Time")
        print("3. Exit")
        choice = input("Select an option (1/2/3): ")
        if choice == '1':
            get_current_datetime()
        elif choice == '2':
            get_custom_datetime()
        elif choice == '3':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()