from datetime import datetime
from datetime import time
from datetime import timedelta
import random

import cauldron as cd
import pandas as pd


def create_entry() -> dict:
    start_time = datetime(
        2016,
        1,
        1,
        random.randint(0, 8),  
        random.randint(0, 59),
        random.randint(0, 59)
    )
    
    elapsed = timedelta(seconds=random.randint(0, 3600))
    
    return dict(
        start_time=start_time.time(),
        end_time=(start_time + elapsed).time(),
        elapsed_seconds=elapsed.total_seconds()
    )

df = pd.DataFrame([create_entry() for _ in range(10)])

cd.display.markdown(
    """
    # Time conversion in Pandas
    
    We start by creating a data frame with three columns, _start_time_,
    _end_time_ and _elapses_seconds_. The time columns are populated with 
    datetime.time objects. The _elapsed_seconds_ contains the number of
    seconds between the start and end times
    
    The resulting data frame looks like:
    """
)

cd.display.table(df)

cd.shared.df = df