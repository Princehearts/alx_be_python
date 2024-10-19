import datetime

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.datetime.now()
    # Format and print the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
    # Get the current date
    current_date = datetime.datetime.now()
    # Calculate the future date by adding the specified number of days
    future_date = current_date + datetime.timedelta(days=days)
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    # Part 1: Display the current date and time
    display_current_datetime()

    # Part 2: Calculate a future date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Please enter a valid integer.")
