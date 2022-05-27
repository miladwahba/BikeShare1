import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ["chicago", "new york city", "washington"]

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
    city = input('enter the city (chicago, new york city, washington):').lower()
    while city not in cities :
        city = input('enter the city (chicago, new york city, washington):').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    months= ['all','january','february','march','april','may','june']
    month = input('enter month form list (all,january,february,march,april,may,june) :').lower()
    while month not in months :
        month = input('enter month form list (all,january,february,march,april,may,june) :').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all' , 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('enter day of week (all , monday, tuesday, wednesday, thursday, friday, saturday, sunday :').lower()
    while day not in days :
        day = input('enter day of week (all , monday, tuesday, wednesday, thursday, friday, saturday, sunday :').lower()

    print('-'*40)
    return city,month,day


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]


    # TO DO: display the most common day of week

    popular_day_of_week = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start month:', popular_month)
    print('Most Popular Start day of week:', popular_day_of_week)
    print('Most Popular Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]


    # TO DO: display most frequent combination of start station and end station trip
    df['start_station_and_end_station'] = df['Start Station']+ " and "+ df['End Station']
    popular_start_station_and_end_station = df['start_station_and_end_station'].mode()[0]
    

    print('Most Popular Start Station:', popular_start_station)
    print('Most Popular end Station:', popular_end_station)
    print('Most Popular of start station and end station:', popular_start_station_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()


    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()


    print('total travel time in seconds :',total_travel_time)
    print('average travel time in seconds :',average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print("counts of user types :\n",counts_of_user_types)
    # TO DO: Display counts of gender
    try :
        counts_of_gender = df['Gender'].value_counts()
        print("counts of gender :\n",counts_of_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        print ('birth year Descripe')
        earliest_year = df['Birth Year'].min()
        print ('earliest year :', earliest_year)
        most_recent_year = df['Birth Year'].max()
        print('most recent year:', most_recent_year)
        most_common_year = df['Birth Year'].mode()[0]
        print ('most common year :', most_common_year)
    except : 
        print('no data for gender & year of birth')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    print('\nRaw data is available to check... \n')
    display_raw = input('To View the availbale raw data in chuncks of 5 rows type: Yes or No if you don\'t want \n').lower()
    while display_raw not in ('yes', 'no'):
        print('That\'s invalid input, please enter your selection again')
        display_raw = input('To View the availbale raw data in chuncks of 5 rows type: Yes or No if you don\'t want \n').lower()
   # The second while loop is on the same level and doesn't belong to the first.
    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city], index_col = 0 ,chunksize=5):
                print(chunk)
                display_raw = input('To View the availbale raw in chuncks of 5 rows type: Yes\n').lower()
                if display_raw != 'yes':
                    print('Thank You')
                    break
            break

        except KeyboardInterrupt:
            print('Thank you.')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
