import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_LIST=['january','february','march','april','may','june','all']
DAY_LIST=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello Sir/Madam! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    try:
        city = input("Would you like to see the data for Chicago, New York, or Washington?")
        while city not in CITY_DATA:
            print('You entered a mistake in the city')
            city = input("Would you like to see the data for Chicago, New York, or Washington?")
        print("Your city choice was {}".format(city))
    # get user input for month (all, january, february, ... , june)
        month = input("For which month do you want to filter? all, January, February, March, April, May, or June?").lower()
        while month not in MONTH_LIST:
            print('Seems like you entered the wrong month')
            month=input("For which month do you want to filter? all, January, February, March, April, May, or June?")
        print('your choice was:{}'.format(month))
    # get user input for day of week (all, monday, tuesday, ... sunday)
        day=input("Which day? all, monday, tuesday, wedsnesday, thursday, friday, saturday, sunday?").lower()
        while day not in DAY_LIST:
            print('Seems like you entered the wrong day')
            day=input("Which day? all, monday, tuesday, wedsnesday, thursday, friday, saturday, sunday?").lower()
        print('your choice was:{}'.format(day))
        return city, month, day
    except Exception as e:
        print('An error with inputs occured: {}'.format(e))
    print('-'*40)
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
    # load data file into a dataframe
    try:
        df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
        if month != 'all':
        # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) +1
        # filter by month to create the new dataframe
            df = df[df['month'] == month]
    # filter by day of week if applicable
        if day != 'all':
        # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]
        return df
    except Exception as e:
        print('Could not load the file, as an Error occurred: {}'.format(e))
def time_stats(df, city):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start = time.time()
    try:

    # display the most common month
        most_common_month_num = df['Start Time'].dt.month.mode()[0]
        popular_month = df['month'].mode()[0]
        print('The most popular month is {}'.format(popular_month))
    except Exception as e:
        print('Could not calculate the most popular month, as an error occured:{}'.format(e))
    # display the most common day of week
    try:
        most_common_day_of_week = df['day_of_week'].mode()[0]
        print('The most popular day is {}'.format(most_common_day_of_week))
    except Exception as e:
        print('Could not calculate the most common day of the week, as an error occured:{}'.format(e))
    # display the most common start hour
    try:
        most_common_hour = df['hour'].mode()[0]
        print('The most popular starting hour is {}.format(most_common_hour)')
    except Exception as e:
        print('Could not calculate the most common start hour, as an error occured:{}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start))
    print('-'*40)
def station_stats(df, city):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    try:
        most_common_start_station = df['Start Station'].mode()[0]
        print('The most popular start station is {}'.format(most_common_start_station))
    except Exception as e:
        print('Could not calculate the most used start station because an error occurred:{}'.format(e))
    # display most commonly used end station
        most_common_end_station = df['End Station'].mode()[0]
        print('The most popular end station is {}'.format(most_common_end_station))
    except Exception as e:
        print('Could not calculate the most used end station because an error occurred:{}'.format(e))
    # display most frequent combination of start station and end station trip
    try:
        popular_start_end = df.loc[:, 'Start Station':'End Station'].mode()[0:]
        print('The most populat trip is {}'.format(popular_start_end))
    except Exception as e:
        print('Could not caculate most popular trip because of error {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df,city):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    try:
        df['Time Delta']=df['End Time'] - df['Start Time']
        total_time_delta=df['Time Delta'].sum()
        print('The total travel time was:{}'.format(total_time_delta))
    except Exception as e:
        print('Could not calculate the total travel time of users, an error occurred:{}'.format(e))
    # display mean travel time
    try:
        total_mean=df['Time Delta'].mean()
        print('The mean distance travelled was {}'.format(total_mean))
    except Exception as e:
        print('Could not print the mean distance travelled because of the error {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    try:
        print('The amount and type of users in {} are as followed {}'.format(city, df['User Type'].value_counts()))
    except Exception as e:
        print('Could not calculate the type of users, as an error occurred: {}'.format(e))
    # Display counts of gender
    try:
        print('The amount and gender of users in', city, 'are as followed:\n',df['Gender'].value_counts())
    except Exception as e:
        print('Couldn\'t calculate the amount and gender of users, as an Error occurred: {}'.format(e))
    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()
        print('The oldest costumer is {} years old, the youngest costumer is {} years old, the most common age is {} year'.format(earliest_year, most_recent_year, most_common_year))
    except Exception as e:
        print('Could not calculate the age sructure of the costomers, as an error eccurred: {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    POSSIBLE_RESPONSE:['yes','no']
    rawdata=''
    while rawdata not in POSSIBLE_RESPONSE:
        print('Madam,Sir, Do you want to see the raw data?')
        print('Accepted answers: yes or no')
        rawdata=input().lower()
        if rawdata =='yes':
            print(df.head())
        elif rwadata not in POSSIBLE_RESPONSE:
            print('Please, verify your input')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df, city)
        station_stats(df, city)
        trip_duration_stats(df, city)
        user_stats(df, city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
