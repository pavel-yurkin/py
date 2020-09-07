import pprint
import requsts

class YahooWeatherForecast:

    def get(self, city)
        url = ""
        data = requests.get(url).json()
        forecast_data = data['query']['results']['channel']['item']['forecast']
        forecast = []
        for day_data in forecast_data:
            forecast.append({
                "date": day_data["date"],
                "high_temp": day_data["high"]
                })
class CityInfo:
    
    def __init__(self, city, weather_forecast = None):
        self.city = city
        self._weather_forecast = weather_forecast

    def wearther_forecast(self):
        get(

def _main():
    city_info = CityInfo("Moscow")
    forecast = city_info.weather_forecast()
    pprint.pprint(forecast)

if __name__ == "__main__":
    _main()
