import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    available_cities = ['chicago','new york city','washington']

    while True:
        city =input('write a city you want to analyse from new york city, chicago and washington\n').lower()
        if city in available_cities:
            break
        else:
            print("You entered an invalid city")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['jan','feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    month_decision = input('Will you like to analyse a specific month or all the months\nPlease write yes for specific month').lower()
    if month_decision == 'yes':
        month = 'specific'
    
    while True:
        month =input('What month do you which to analyse\nPlease enter the abb. form\n').lower()
        if month in month_list:
            break
        else:
            print('Please enter a valid month') 
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_decision = input('Will you like to analyse all the days of the week or specific days\nPlease write yes for all days').lower()  
    if day_decision == 'yes':
        day = 'all'
    else:
         while True:
            try:
                day = int( input('Please write the day you want to analyse. Write 0= sunday, 1= monday,... 6= saturday\n'))
                if 0 < day < 6:
                    break
                else:
                    print('out of range')
            except:
                    print('You entered an invalid day ')
    

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    def load_data(city, month, day):
        """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['Week Day'] = df['Start Time'].dt.dayofweek
    df['Hour'] = df['Start Time'].dt.hour
    month_index = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
    if month != 'all':
        df = df.loc[df['month'] == month_index[month]]
    df.head()
    if day != 'all':
        df = df.loc[df['Week Day'] == day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()
    print(most_common_month)

    # TO DO: display the most common day of week
    most_common_weekday = df['Week Day'].mode()
    print(most_common_weekday)

    # TO DO: display the most common start hour
    most_common_hour =df['Hour'].mode()
    print(most_common_hour)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_station = df['Start Station'].mode()
    print(most_used_start_station)

    # TO DO: display most commonly used end station
    most_used_end_station = df['End Station'].mode()
    print(most_used_end_station)    

    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Combination'] = df['Start Station'] + "..." + df['End Station']
    most_start_end_combination  = df['Start-End Combination'].mode()
    print(most_start_end_combination)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print(total_trip_duration)

    # TO DO: display mean travel time
    total_trip_duration = df['Trip Duration'].mean()
    print(total_trip_duration)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print(user_count)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print('Data not available')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Gender' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print(earliest_birth_year)
        most_recent_birth_year = df['Birth Year'].max()
        print(most_recent_birth_year)
        most_common_birth_year = df['Birth Year'].mode()
        print(most_common_birth_year)
    else:
        print('Data not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def view_data(df):     
        display_data = input("Do you wish to view the the first 5 rows?").lower()
        if display_data == 'yes':
            i = 0
            while True:
                print(df.loc[i:i + 5])
                i+=5
                display_data = input("Do you wish to view the the next 5 rows?").lower()
                if display_data != 'yes':
                    break
          
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)  
          

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
