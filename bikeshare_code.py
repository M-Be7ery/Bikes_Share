import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
print('Hello! Let\'s explore some US bikeshare data!')
   
    
#get the city as input from the user and check that the user's input is one of the available cities list
#get the filtering by time as an input from the user and check that the user's input is one of the available o

def user_input():
    cities=['chicago','new york city','washington']
    while True:
        city=input('\nPlease, select the city to be analyzed from chicago, new york city or washington:\n').lower()
        if city in cities:
            break
            
    print('you choosed city of {}'.format(city))
    

    
    filter_opts=['month', 'day', 'both', 'none']
    
    while True:
        filter_opt = input("\nDo you want to filter the data by month, day, both or none? (Hint: choose none\nif you wanna display the data for all the available period):\n").lower()  
        if filter_opt in filter_opts:
        
            if filter_opt == 'month':
                months = ['january', 'feburary', 'march', 'april', 'may', 'june']
                while True:
                    month = input("\nWhich month? january, feburary, march, april, may or june?:\n").lower()
                    if month in months:
                       break
                day = 'all'
                break
            elif filter_opt == 'day':
                days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
                while True:
                    day = input("\nWhich day? monday, tuesday, wednesday, thursday, friday, saturday or sunday?:\n").lower()
                    if day in days:
                        break
                month = 'all'
                break
                
            elif filter_opt == 'both':
                months = ['january', 'feburary', 'march', 'april', 'may', 'june']
                while True:
                    month = input("\nWhich month? january, feburary, march, april, may or june?:\n").lower()
                    if month in months:
                        break
                days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
                while True:
                    day = input("\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?:\n").lower()
                    if day in days:
                        break
                break       
            else :
                month = 'all'
                day = 'all'      
                break       
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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

    # display the most common month
    popular_month = df['month'].mode()[0]
    
    print('The most common month is: {}.'.format(popular_month))

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    print('The most common day of week is: {}.'.format(popular_day))
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    
    print('The most common hour of day is: {}.'.format(popular_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
        
def station_stats(df):
    
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start=df['Start Station'].value_counts().index[0]
    print('The most common start station is: {}.'.format(popular_start))

    # display most commonly used end station
    popular_end=df['End Station'].value_counts().index[0]
    print('The most common end station is: {}.'.format(popular_end))

    # display most frequent combination of start station and end station trip
    df['start_end']=df['Start Station'] +'--'+ df['End Station']
    popular_start_end=df['start_end'].value_counts().index[0]
    print('The most frequent combination of start and end station trip is: {}.'.format(popular_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tot_travel_time=df['Trip Duration'].sum()
    print('The total travel time is {} seconds'.format(tot_travel_time))

    # display mean travel time
    avg_travel_time=df['Trip Duration'].mean()
    print('The average travel time is {} seconds'.format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of user types are:\n\n{}'.format(user_types))

    # Display counts of gender if avalable in the data of the chosen city
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('The counts of users gender are:\n\n{}'.format(gender_count))
    else:
        print("This city data file has no information about the gender of the users")
    
    #Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        print('The earliest year of birth is {}'.format(earliest))
        most_recent = df['Birth Year'].max()
        print('The most recent year of birth is {}'.format(most_recent))
        most_common = df['Birth Year'].mode()[0]
        print('The most common year of birth is {}'.format(most_common))
    else:
        print("This city data file has no information about the year of birth of the users")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
       
    responce= input('\nSample of data is available to check!, would you like to view a sample of data? yes or no:\n').lower()
    responces = ['yes', 'no']
    while responce not in responces:
            responce= input('\nwould you like to view a sample of data? yes or no:\n').lower()
        
    while True:
            
        while responce == 'yes':

            print(df.sample(n=5))
            responce = input('\nWould you like to view another sample of data? yes or no:\n').lower()
            while responce not in responces:
                responce= input('\nwould you like to view a sample of data? yes or no:\n').lower()
            
            if responce == 'no':
                
                print('Thank You')
                break
        break
               

def main():
    while True:
        city, month, day = user_input()
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