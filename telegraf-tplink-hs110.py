import sys
import asyncio
from datetime import datetime
from kasa import SmartPlug

async def get_power_data(plugs):
    output = []
    for plug_name, ip_address in plugs:
        plug = SmartPlug(ip_address)
        await plug.update()
        plug_data = await plug.get_emeter_realtime()
        plug_monthly_data = await plug.get_emeter_daily()
        plug_total_monthly_data = await plug.get_emeter_monthly()

        # Add realtime data
        realtime_data = ",".join([f"{k}={v}" for k, v in plug_data.items()])
        output.append(f"power,plugname={plug_name} {realtime_data}")

        # Add daily data
        for day, total in plug_monthly_data.items():
            if day == datetime.today().day:
                day_str = "0"
            else:
                days_difference = (datetime.today() - datetime(datetime.today().year, datetime.today().month, day)).days
                day_str = f"-{days_difference}"

            output.append(f"power,plugname={plug_name},day={day_str} total={total}")

        # Add total monthly data
        current_month = datetime.today().month
        output.append(f"power,plugname={plug_name},month=0 total={plug_total_monthly_data[current_month]}")

    print("\n".join(output))

# Get the list of plugs from the command line arguments
plugs = []
for i in range(1, len(sys.argv), 2):
    plugs.append((sys.argv[i], sys.argv[i+1]))

# Call the get_power_data function using asyncio
asyncio.run(get_power_data(plugs))
