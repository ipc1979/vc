from graphene import Int, ObjectType, Schema, Field
from gql.entities import DatesInput, LocationInput, WheaterForecastResponse, WheaterObservedResponse
from repositories.file import WeatherForecastRepository, WeatherObservedRepository
from datetime import datetime, timedelta
from services.weather import weather_forecast_by_dates, weather_observed_by_dates
from config import config

class Query(ObjectType):

    weather_forecast_by_dates = Field(
        WheaterForecastResponse,
        dates=DatesInput(required=True),
        location=LocationInput(required=True)
    )

    weather_forecast_by_days = Field(
        WheaterForecastResponse,
        days=Int(required=True),
        location=LocationInput(required=True)
    )
    
    weather_observed_by_dates = Field(
        WheaterObservedResponse,
        dates=DatesInput(required=True),
        location=LocationInput(required=True)
    )

    weather_observed_by_days = Field(
        WheaterObservedResponse,
        days=Int(required=True),
        location=LocationInput(required=True)
    )
    
    def resolve_weather_forecast_by_dates(
            root, 
            info,
            dates: DatesInput,
            location: LocationInput
        ):

        repository = WeatherForecastRepository(
            latitude=location.latitude,
            longitude=location.longitude,          
            city=location.city,
            base_path=config.base_path
        )

        weather_forecast = weather_forecast_by_dates(
            from_date=dates.from_date,
            to_date=dates.to_date,
            repository=repository
        )

        return weather_forecast

    def resolve_weather_forecast_by_days(
            root, 
            info,
            days: Int,
            location: LocationInput
        ):

        repository = WeatherForecastRepository(
            latitude=location.latitude,
            longitude=location.longitude,          
            city=location.city,
            base_path=config.base_path
        )

        from_date = datetime.now()
        to_date = from_date + timedelta(days=days)

        weather_forecast = weather_forecast_by_dates(
            from_date=from_date,
            to_date=to_date,
            repository=repository
        )

        return weather_forecast
    
    def resolve_weather_observed_by_dates(
            root, 
            info,
            dates: DatesInput,
            location: LocationInput
        ):

        repository = WeatherObservedRepository(
            latitude=location.latitude,
            longitude=location.longitude,          
            city=location.city,
            base_path=config.base_path
        )

        weather_forecast = weather_observed_by_dates(
            from_date=dates.from_date,
            to_date=dates.to_date,
            repository=repository
        )

        return weather_forecast

    def resolve_weather_observed_by_days(
            root, 
            info,
            days: Int,
            location: LocationInput
        ):

        repository = WeatherObservedRepository(
            latitude=location.latitude,
            longitude=location.longitude,          
            city=location.city,
            base_path=config.base_path
        )

        from_date = datetime.now()
        to_date = from_date + timedelta(days=days)

        weather_forecast = weather_observed_by_dates(
            from_date=from_date,
            to_date=to_date,
            repository=repository
        )

        return weather_forecast

schema = Schema(query=Query)
