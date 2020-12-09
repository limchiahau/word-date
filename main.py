from datetime import datetime, timedelta
from num2words import num2words
import sys

def period(start_date, year):
    '''
    returns a tuple with the start date and the end date.
    
    retuns (start:datetime, duration:datetime)
    
    start_date: datetime object from the datetime module
    duration: int <- unit = years
    
    '''
    # the end date if the start date + 1 year
    # deduct 1 day
    end_date = datetime(start_date.year + year,
                        start_date.month,
                        start_date.day)
    end_date = end_date - timedelta(days=1)
    
        
    return start_date, end_date


def year_delta(year):
    '''
    returns a timedelta that represents the given years
    
    return timedelta from the datetime module
    year: int
    '''
    return timedelta(days=365) * year

def tenancy_period(start_date, year, fmt='{@term}\n\t\t(i.e {@start_date} to {@end_date})'):
    '''
    return a string that represent the tenancy period
    
    You can change the format of the returned string by setting the fmt
    variable.
    
    There are 3 variables used in the format string:
    1. @term -> "One (1) Year"
    2. @start_date -> "1 July 2019" //commencement date
    3. @end_date -> "30 June 2020" //end date
    
    start_date: datetime object from the datetime module
    year: int <- unit = years
    '''
    
    period_tuple = period(start_date, year) 
    
    term = f'{num2words(year).upper()} ({str(year)}) {year_str(year).upper()}'
    
    commencement_date = period_tuple[0].strftime("%-d %B %Y")
    end_date = period_tuple[1].strftime("%d %B %Y")
    
    return fmt.format_map({
        '@term' : term,
        '@start_date' : commencement_date,
        '@end_date' : end_date
    })
    
def year_str(year):
    '''
    determine if there should be a 's' at the end of the year.
    Than returns a 'Year' with or without the 's'.
    
    output -> 'year' | 'years'
    
    year: int  // unit year
    '''
    end = ''
    if year > 1:
        end = 's'
    
    return 'year' + end


def get_commencement_date():
    day = int(sys.argv[1])
    month = int(sys.argv[2])
    year = int(sys.argv[3])

    return datetime(year, month, day)

def get_tenure():
    period = int(sys.argv[4])
    return period


#MAIN
commencement_date = get_commencement_date()
tenure = get_tenure()

print(tenancy_period(commencement_date, tenure))
