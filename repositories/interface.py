from abc import ABC, abstractmethod

from domain.entities import WeatherData

class IWeatherRepository(ABC):
    
    @abstractmethod
    def get_weather_data_by_dates() -> WeatherData:
        ...
    
    @abstractmethod
    def get_weather_data_by_dates() -> WeatherData:
        ...