import pytest
from gql.resolvers import schema
from graphene.test import Client

@pytest.fixture
def client():
    return Client(schema)

def test_query_weather_forecast_by_dates_with_data(client):
    query = '''
        query {
            weatherForecastByDates(
                dates: {
                    fromDate: "2019-09-19",
                    toDate: "2019-09-20"
                },
                location: {
                    latitude: -11.56,
                    longitude: -37.52,
                    city: "Abadia-BA"
                }
            ) {
                periods ,
                points {
                    location {
                        latitude,
                        longitude
                    },
                    data {
                        temperature
                    }
                },
                meta {
                    updatedAt
                }
            }
        }
    '''

    result = client.execute(query)

    assert result['data']['weatherForecastByDates'] == {
        "periods": [
            "2019-09-19 06:00"
        ],
        "points": {
            "location": {
                "latitude": -11.56,
                "longitude": -37.52
            },
            "data": {
                "temperature": [
                    24.30055046081543
                ]
            }
        },
        "meta": {
            "updatedAt": ""
        }
    }

def test_query_weather_forecast_by_dates_without_data(client):
    query = '''
        query {
            weatherForecastByDates(
                dates: {
                    fromDate: "2024-09-19",
                    toDate: "2024-09-20"
                },
                location: {
                    latitude: -11.56,
                    longitude: -37.52,
                    city: "Abadia-BA"
                }
            ) {
                periods ,
                points {
                    location {
                        latitude,
                        longitude
                    },
                    data {
                        temperature
                    }
                },
                meta {
                    updatedAt
                }
            }
        }
    '''

    result = client.execute(query)

    assert result['data']['weatherForecastByDates'] == {
        "periods": [],
        "points": {
            "location": {
                "latitude": -11.56,
                "longitude": -37.52
            },
            "data": {
                "temperature": []
            }
        },
        "meta": {
            "updatedAt": ""
        }
    }

def test_query_weather_forecast_by_days_with_data(client):
    query = '''
        query {
            weatherForecastByDates(
                dates: {
                    fromDate: "2019-09-19",
                    toDate: "2019-09-20"
                },
                location: {
                    latitude: -11.56,
                    longitude: -37.52,
                    city: "Abadia-BA"
                }
            ) {
                periods ,
                points {
                    location {
                        latitude,
                        longitude
                    },
                    data {
                        temperature
                    }
                },
                meta {
                    updatedAt
                }
            }
        }
    '''

    result = client.execute(query)

    assert result['data']['weatherForecastByDates'] == {
        "periods": [
            "2019-09-19 06:00"
        ],
        "points": {
            "location": {
                "latitude": -11.56,
                "longitude": -37.52
            },
            "data": {
                "temperature": [
                    24.30055046081543
                ]
            }
        },
        "meta": {
            "updatedAt": ""
        }
    }

def test_query_weather_forecast_by_days_without_data(client):
    query = '''
        query {
            weatherForecastByDays(
                days: 10,
                location: {
                    latitude: -11.56,
                    longitude: -37.52,
                    city: "Abadia-BA"
                }
            ) {
                periods ,
                points {
                    location {
                        latitude,
                        longitude
                    },
                    data {
                        temperature
                    }
                },
                meta {
                    updatedAt
                }
            }
        }
    '''

    result = client.execute(query)

    assert result['data']['weatherForecastByDays'] == {
        "periods": [],
        "points": {
            "location": {
                "latitude": -11.56,
                "longitude": -37.52
            },
            "data": {
                "temperature": []
            }
        },
        "meta": {
            "updatedAt": ""
        }
    }












