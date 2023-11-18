from util.helper import logAndPrint
import python_weather as pw

async def execute(self, msg, args):
    try:
        client = pw.Client(unit=pw.IMPERIAL)
        print(args)
        for arg in args:
            print(arg)
            weather = await client.get(arg)
            country = weather.nearest_area.country 
            region = weather.nearest_area.region
            resp = f"The current temperature in {arg}, {region}, {country} is {weather.current.temperature}!"
            await logAndPrint(self, msg, resp, True)
        await client.close()
    except BaseException as err:
        await logAndPrint(self, msg, err, False)