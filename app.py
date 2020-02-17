import datetime
import pandas as pd
#comment

year = datetime.datetime.now().year
#change this
number_of_rooms = 40

# dict contructor to match room number with corresponding category
def selector(x):
    if x<11:
        return 0
    elif x<21:
        return 1
    elif x<31:
        return 2
    else:
        return 3

categories = {str(i): selector(i) for i in range(1, number_of_rooms+1)}
print(categories)
class Room:

    # read xlsx file with pandas
    prices_weekdays = pd.read_excel("room_prices.xlsx", sheet_name='weekdays')
    prices_weekend = pd.read_excel("room_prices.xlsx", sheet_name='weekend')
    
    # extract only the row with specified category to calculate prices
    def __init__(self, category):
        self.category = category
        self.prices_weekdays = Room.prices_weekdays.loc[self.category]
        self.prices_weekend = Room.prices_weekend.loc[self.category]

    # calculate total amount
    def calculate(self, start, end):
        total = 0
        current_day = start
        delta = datetime.timedelta(days=1)
        print(self.prices_weekdays)
        print(self.prices_weekend)
        print()
        # for each day calculate price
        while current_day < end:
            print(f'current month: {current_day.month}')
            print()
            if current_day.weekday() >= 4:
                day_price = self.prices_weekend.loc[current_day.month]
            else:
                day_price = self.prices_weekdays.loc[current_day.month]
            total += day_price
            print(f' current_day: {current_day}, {current_day.weekday()}, price: {day_price}')
            k = input('press for continue:')
            # increment current day by 1 day
            current_day += delta

        return f'Category: {self.category},  arrival date: {start}, departure date: {end}, total: {total} €'


while True:

    room_number = input('Input room number: ')
    print(f"Room: {room_number}")
    room = Room(categories[room_number])

    start_d, start_M = input('Input month and day of arrival in d-M format: ').split('-')
    end_d, end_M = input('Input month and day of departure in d-M format: ').split('-')
    start = datetime.datetime(year, int(start_M), int(start_d)).date()
    end = datetime.datetime(year, int(end_M), int(end_d)).date()

    print(room.calculate(start, end))
    print()
    c = input("Press 'q' to quit the program or continue: ")
    print()
    if (c=='q' or c=='Q'):
        break
