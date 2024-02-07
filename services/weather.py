from datetime import date
from gql.entities import WheaterForecastResponse, WheaterObservedResponse, PointsForecast, PointsObserved, Location, DataForecast, DataObserved, Meta, Units
from repositories.file import WeatherForecastRepository, WeatherObservedRepository

def weather_forecast_by_dates(
        from_date: date,
        to_date: date,
        repository: WeatherForecastRepository      
    ) -> WheaterForecastResponse:

    weather_data = repository.get_weather_data_by_dates(
        from_date=from_date,
        to_date=to_date
    )

    return WheaterForecastResponse(
        periods = weather_data.periods,
        points = PointsForecast(
            location = Location(
                latitude = repository.latitude,
                longitude = repository.longitude,
                elevation = 0,
                sunset = "",
                sunrise = "",
                timezone = 0,
                reference = ""
            ),
            data = DataForecast(
                precipitation = weather_data.precipitation, 
                temperature = weather_data.temperature,
                max_temperature = weather_data.max_temperature,
                min_temperature = weather_data.min_temperature,
                rel_humidity = weather_data.rel_humidity,
                wind_speed = weather_data.wind_speed,
                wind_direction = weather_data.wind_direction,
                pressure = weather_data.pressure            
            )
        ),
        meta = Meta(
            updated_at = "",
            units = Units(
                precipitacion = "mm",
                temperature = "C",
                humidity = "%",
                wind_speed = "m/s",
                wind_direction = "deg",
                pressure = "hpa"                
            )
        )            
    )

def weather_observed_by_dates(
        from_date: date,
        to_date: date,
        repository: WeatherObservedRepository      
    ) -> WheaterObservedResponse:

    weather_data = repository.get_weather_data_by_dates(
        from_date=from_date,
        to_date=to_date
    )

    return WheaterObservedResponse(
        periods = weather_data.periods,
        points = PointsObserved(
            location = Location(
                latitude = repository.latitude,
                longitude = repository.longitude,
                elevation = 0,
                sunset = "",
                sunrise = "",
                timezone = 0,
                reference = ""
            ),
            data = DataObserved(
                precipitation = weather_data.precipitation,
                temperature = weather_data.temperature,
                max_temperature = weather_data.max_temperature,
                min_temperature = weather_data.min_temperature,
                max_rel_humidity = weather_data.max_rel_humidity,
                min_rel_humidity = weather_data.min_rel_humidity,
                max_pressure = weather_data.max_pressure,
                min_pressure = weather_data.min_pressure,
                wind_gust = weather_data.wind_gust,
                frost_alert = weather_data.frost_alert,
                etp = weather_data.etp,
                radiation = weather_data.radiation,
                wetting = weather_data.wetting 
            )
        ),
        meta = Meta(
            updated_at = "",
            units = Units(
                precipitacion = "mm",
                temperature = "C",
                humidity = "%",
                wind_speed = "m/s",
                wind_direction = "deg",
                pressure = "hpa"                
            )
        )            
    )
