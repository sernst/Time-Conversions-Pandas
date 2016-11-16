from datetime import datetime
from datetime import time

import cauldron as cd
import pandas as pd

df = cd.shared.df

cd.display.markdown(
    """
    In this case we already have the _elapsed_seconds_ column, but what if we
    needed to claculate that ourselves from the start and end times?
    
    The first thought is to create our _elapsed_ column by subtracting the
    end time from the start time like this:
    
        df['elapsed'] = df['end_time'] - df['start_time']    
    
    but if you do that you will get a TypeError:
    
        unsupported operand type(s) for -: 'datetime.time' and 'datetime.time'
    
    What we need to do is convert the time columns into datetime columns first
    because datetime objects do support the subtraction operator.
    
    We will start by creating a function that converts a time object to a
    datetime object like this:
    
        def time_to_datetime(t: time) -> datetime:
            return datetime(
                2016,
                1,
                1,
                t.hour,
                t.minute,
                t.second
            )    
    
    We've set the date part of the datetime to 1/1/2016 here, but you can set
    it to anything that you want in this case as long as it is a constant 
    value throughout.
    
    Now we can use the Pandas apply() method on a time column to create a 
    datetime result like this:
    
        end_datetimes = df['end_time'].apply(time_to_datetime)
    
    Now we can subtract the datetimes columns to create our elapsed column:
    
        df['elapsed'] = (end_datetimes - start_datetimes )
    
    And when you inspect the resulting data frame, you can see that our 
    _elapsed_ column values match the _elapsed_seconds_ column values that
    were populated when the data frame was created.
    """
)

def time_to_datetime(t: time) -> datetime:
    return datetime(
        2016,
        1,
        1,
        t.hour,
        t.minute,
        t.second
    )

start_datetimes = df['start_time'].apply(time_to_datetime)
end_datetimes = df['end_time'].apply(time_to_datetime)
    
df['elapsed'] = (end_datetimes - start_datetimes )

cd.display.table(df)
