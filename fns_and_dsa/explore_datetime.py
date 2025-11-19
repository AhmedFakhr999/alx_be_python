import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print('Current date and time: ')
    print(current_date.strftime('%Y-%m-%d %H:%M:%S'))

def calculate_future_date(): 
    days = int(input('Enter the number of days to add to the current date: '))
    

    today = datetime.date.today()
    

    future_date = today + datetime.timedelta(days=days)
    
    
    print(future_date.strftime('%Y-%m-%d'))

if __name__ == '__main__':
    display_current_datetime()
    calculate_future_date()