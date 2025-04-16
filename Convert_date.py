import datetime
import jdatetime

def convert_gregorian_to_shamsi():
    try:
        input_date = input("Enter Gregorian date (YYYY-MM-DD): ")
        year, month, day = map(int, input_date.split('-'))
        gregorian_date = datetime.date(year, month, day)
        jalali_date = jdatetime.date.fromgregorian(date=gregorian_date)
        print("Shamsi date is:", jalali_date.strftime("%Y/%m/%d"))
    except Exception as e:
        print("Invalid input. Please enter date in correct format.")

def convert_shamsi_to_gregorian():
    try:
        input_date = input("Enter Shamsi date (YYYY-MM-DD): ")
        year, month, day = map(int, input_date.split('-'))
        jalali_date = jdatetime.date(year, month, day)
        gregorian_date = jalali_date.togregorian()
        print("Gregorian date is:", gregorian_date.strftime("%Y/%m/%d"))
    except Exception as e:
        print("Invalid input. Please enter date in correct format.")

# حلقه اصلی برنامه
while True:
    print("\nChoose conversion type:")
    print("1. Gregorian to Shamsi (میلادی به شمسی)")
    print("2. Shamsi to Gregorian (شمسی به میلادی)")
    
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        convert_gregorian_to_shamsi()
    elif choice == "2":
        convert_shamsi_to_gregorian()
    else:
        print("Invalid choice. Please enter 1 or 2.")

    again = input("\nDo you want to convert another date? (y/n): ")
    if again.lower() != 'y':
        print("Goodbye!")
        break
