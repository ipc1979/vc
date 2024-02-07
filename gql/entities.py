from graphene import InputObjectType, ObjectType, String, Int, Field, Float, List, Date

class LocationInput(InputObjectType):
    latitude = Float()
    longitude = Float()
    city = String()

class DatesInput(InputObjectType):
    from_date = Date()
    to_date = Date()

class Units(ObjectType):
    precipitacion = String()
    temperature = String()
    humidity = String()
    wind_speed = String()
    wind_direction = String()
    pressure = String()

class Meta(ObjectType):
    updated_at = String()
    units = Field(Units)

class Location(ObjectType):
    latitude = Float()
    longitude = Float()
    elevation = Int()
    sunrise = String()
    sunset = String()
    timezone = Int()
    reference = String()

class DataObserved(ObjectType):
    periods = List(Float)
    precipitation = List(Float)
    temperature = List(Float)
    max_temperature = List(Float)
    min_temperature = List(Float)
    max_rel_humidity = List(Float)
    min_rel_humidity = List(Float)
    max_pressure = List(Float)
    min_pressure = List(Float)
    wind_gust = List(Float)
    frost_alert = List(Float)
    etp = List(Float)
    radiation = List(Float)
    wetting = List(Float)

class DataForecast(ObjectType):
    precipitation = List(Float)	
    temperature = List(Float)
    max_temperature = List(Float)	
    min_temperature = List(Float)	
    rel_humidity = List(Float)
    wind_speed = List(Float)	
    wind_direction = List(Int)	
    pressure = List(Float)  
    weather_conditions = List(Float)
    atmospheric_conditions = List(Float)
    thunderstorm_alerts = List(Float)
    thermal_sensation = List(Float)
    max_sensation = List(Float)
    min_sensation = List(Float)
    frost_alert = List(Float)
    etp = List(Float)

class PointsForecast(ObjectType):
    location=Field(Location)
    data=Field(DataForecast)

class PointsObserved(ObjectType):
    location=Field(Location)
    data=Field(DataObserved)

class WheaterForecastResponse(ObjectType):
    periods=List(String)
    points=Field(PointsForecast)
    meta=Field(Meta)

class WheaterObservedResponse(ObjectType):
    periods=List(String)
    points=Field(PointsObserved)
    meta=Field(Meta)
 