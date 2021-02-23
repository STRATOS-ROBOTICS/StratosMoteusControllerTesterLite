
import asyncio
import math
import moteus

async def main():
    c = moteus.Controller()
    await c.set_stop()  # in case there was a fault

    while True:
        print(await c.set_position(position=math.nan, velocity=0.5, maximum_torque=0.5, stop_position=0.9, query=True))
        await asyncio.sleep(0.02)

asyncio.run(main())
