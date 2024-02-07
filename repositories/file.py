import pandas as pd
from constants import CSV_SEPARATOR, DATE_FORMAT
from datetime import date
from domain.entities import WeatherForecastData, WeatherObservedData

class WeatherForecastRepository():

    def __init__(
        self,
        latitude: float,
        longitude: float,         
        city: str,
        base_path: str
    ):
        self.latitude = latitude
        self.longitude = longitude        
        self.city = city
        self.base_data_path = f'{base_path}/forecast/'

    def get_weather_data_by_dates(self, from_date: date, to_date: date) -> WeatherForecastData:

        try:
            df_wheater_data = pd.read_csv(
                filepath_or_buffer=self.base_data_path+f'{self.city}_{self.latitude}_{self.longitude}.csv',
                sep=CSV_SEPARATOR
            )
        except Exception as e:
            raise e

        index_datetime = df_wheater_data[
            (from_date.strftime(DATE_FORMAT) <= df_wheater_data['periods']) & 
            (df_wheater_data['periods'] <= to_date.strftime(DATE_FORMAT) )   
        ].index

        df_wheater_data = df_wheater_data.iloc[index_datetime]

        return WeatherForecastData(
            periods = list(df_wheater_data['periods']),
            precipitation = list(df_wheater_data['precipitation']),
            temperature = list(df_wheater_data['temperature']),
            max_temperature = list(df_wheater_data['max_temperature']),
            min_temperature = list(df_wheater_data['min_temperature']),
            rel_humidity = list(df_wheater_data['rel_humidity']),
            wind_speed = list(df_wheater_data['wind_speed']),
            wind_direction = list(df_wheater_data['wind_direction']),
            pressure = list(df_wheater_data['pressure']),
            weather_conditions = list(df_wheater_data['weather_conditions']),
            atmospheric_conditions = list(df_wheater_data['atmospheric_conditions']),
            thunderstorm_alerts = list(df_wheater_data['thunderstorm_alerts']),
            thermal_sensation = list(df_wheater_data['thermal_sensation']),
            max_sensation = list(df_wheater_data['max_sensation']),
            min_sensation = list(df_wheater_data['min_sensation']),
            frost_alert = list(df_wheater_data['frost_alert']),
            etp = list(df_wheater_data['etp']),     
        )    
    
class WeatherObservedRepository():

    def __init__(
        self,
        latitude: float,
        longitude: float,         
        city: str,
        base_path: str
    ):
        self.latitude = latitude
        self.longitude = longitude        
        self.city = city
        self.base_data_path = f'{base_path}/observed/'

    def get_weather_data_by_dates(self, from_date: date, to_date: date) -> WeatherObservedData:

        try:
            df_wheater_data = pd.read_csv(
                filepath_or_buffer=self.base_data_path+f'{self.city}_{self.latitude}_{self.longitude}.csv',
                sep=CSV_SEPARATOR
            )
        except Exception as e:
            raise e

        index_datetime = df_wheater_data[
            (from_date.strftime(DATE_FORMAT) <= df_wheater_data['periods']) & 
            (df_wheater_data['periods'] <= to_date.strftime(DATE_FORMAT) )   
        ].index

        df_wheater_data = df_wheater_data.iloc[index_datetime]

        return WeatherObservedData(
            periods = list(df_wheater_data['periods']),
            precipitation = list(df_wheater_data['precipitation']),
            temperature = list(df_wheater_data['temperature']),
            max_temperature = list(df_wheater_data['max_temperature']),
            min_temperature = list(df_wheater_data['min_temperature']),
            max_rel_humidity = list(df_wheater_data['max_rel_humidity']),
            min_rel_humidity = list(df_wheater_data['min_rel_humidity']),
            max_pressure = list(df_wheater_data['max_pressure']),
            min_pressure = list(df_wheater_data['min_pressure']),
            wind_gust = list(df_wheater_data['wind_gust']),
            frost_alert = list(df_wheater_data['frost_alert']),
            etp = list(df_wheater_data['etp']),
            radiation = list(df_wheater_data['radiation']),
            wetting = list(df_wheater_data['wetting'])        
        )
    
    