import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago','new york city','washington']
MONTHS = ['january','february','march','april','may','june','all']
DAYS = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']


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
    while True:
        city = input('enter city name:(Chicago, New York, Washington)').format(city.title())).lower()
    if city in CITIES:
             break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input ('\n\nTo filter {}\'s data by a particular month, please type the month name or all for not filtering by month:\n-January\n-February\n-March\n-April\n-May\n-June\n All\n\n:'.format(city.title())).lower()

    while month not in MONTHS:
        print("That's an invalid choice, please type a valid month name or all.")
        month = input ('\n-January\n-February\n-March\n-April\n-May\n-June\n All\n\n:'.format(city.title())).lower()
         
         
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\n\nTo filter {}\'s data by a particular day, please type the day name or all for not filtering by weekday:\n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-Saturday\n-Sunday\n All\n\n:'.format(city.title())).lower()
    while day not in DAYS:
        print("That's an invalid choice, please type a valid day name or all.")
        day = input('\n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-Saturday\n-Sunday\n All\n\n:'.format(city.title())).lower()
        
        
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
#first load data
    df = pd.read_csv(CITY_DATA[city])
#second to convert the start time to datetime
    df['Start Time']= pd.to_datetime(df['Start Time'])
#extracting month and day from Start Time into new columns
    df['month']=df ['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
#also to filter by month
    if month !='all':
        month = MONTHS.index(month) + 1
        df = df[df['month'] ==month ]
#filter by day
    if day != 'all':
        df=df[df['day_of_week'] ==day.title()]
    return df
   


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print ("The most common month is:", most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is:", most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station =df['Start Station'].value_counts().idxmax()
    print("The most common start station is:", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station =df['End Station'].value_counts().idxmax()
    print("The most common end station is:", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station =df[['Start Station','End Station']].mode().loc[0]
    print("The most frequent combination of start and end station is: {},{}".format(most_common_start_end_station[0], most_common_start_end_station[1]))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print ("Total travel time is :", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print ("The mean of travel time is:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

   
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        user_stats_gender(df)

    if 'Birth Year' in df.columns:
        user_stats_birth(df)

    
def user_stats_gender(df):
    user_gender = df['Gender'].value_counts()
    print(user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
def user_stats_birth(df):
    birth_year=df['Birth Year']
    most_common_birth_year=birth_year.value_counts().idxmax()
    print("The most common birth year is:", most_common_birth_year)
    most_recent_year=birth_year.max()
    print ("The most recent birth year is:", most_recent_year)
    earliest_year=birth_year.min()
    print("The earliest birth year is:", earliest_year)

   
    
import json
def display_raw_data(df):
    row_length=df.shape[0]
    for i in range(0, row_length,5):
        yes=input ('\nDo you want to display a sample of the data? type \'yes\' or \'no\'\n>')
        if yes.lower() !='yes':
            break
        
        row_data= df.iloc[i: i+5].to_json(orient='records', lines=True).split('\n')
        for row in row_data:
            parsed_row=json.loads(row)
            json_row=json.dumps(parsed_row,indent=2)
            print(json_row)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
