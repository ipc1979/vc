from dataclasses import dataclass

@dataclass
class WeatherObservedData:
    periods: list
    precipitation: list
    temperature: list
    max_temperature: list
    min_temperature: list
    max_rel_humidity: list
    min_rel_humidity: list
    max_pressure: list
    min_pressure: list
    wind_gust: list
    frost_alert: list
    etp: list
    radiation: list
    wetting: list

@dataclass
class WeatherForecastData:
    periods: list
    precipitation: list
    temperature: list
    max_temperature: list
    min_temperature: list
    rel_humidity: list
    wind_speed: list
    wind_direction: list
    pressure: list
    weather_conditions: list
    atmospheric_conditions: list
    thunderstorm_alerts: list
    thermal_sensation: list
    max_sensation: list
    min_sensation: list
    frost_alert: list
    etp: list 