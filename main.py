import asyncio


class TrafficLight:
    def __init__(self):
        self.colors = ['red', 'yellow', 'green']

    async def run(self):
        while True:
            for color in self.colors:
                await self.switch(color)

    async def switch(self, color):
        if color == 'red':
            print("Red light")
            await asyncio.sleep(4)
        elif color == 'yellow':
            print("Yellow light")
            await asyncio.sleep(6)
        elif color == 'green':
            print("Green light")
            await asyncio.sleep(8)


async def main():
    traffic_light = TrafficLight()
    await traffic_light.run()


asyncio.run(main())
