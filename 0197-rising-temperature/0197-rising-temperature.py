import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])

    # Sort by date to ensure comparison order
    weather.sort_values('recordDate', inplace=True)

       # Shift temperature and date for yesterday's values
    weather['prevDate'] = weather['recordDate'].shift(1)
    weather['prevTemp'] = weather['temperature'].shift(1)

    # Compare today's date with yesterday and filter
    mask = (weather['recordDate'] - weather['prevDate'] == pd.Timedelta(days=1)) & \
           (weather['temperature'] > weather['prevTemp'])

    return weather.loc[mask, ['id']]