import os
import yaml
import config
import asyncio

from loguru import logger
from dotenv import load_dotenv
from aiohttp import ClientSession
from pyuseragents import random as random_useragent
from tenacity import retry, retry_if_exception, stop_after_attempt, wait_fixed

load_dotenv()

HEADERS = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'content-type': 'application/json',
    'origin': 'https://discord.com',
    'authorization': os.environ["TOKEN"],
    'user-agent': random_useragent()
}


@retry(retry=retry_if_exception(Exception), stop=stop_after_attempt(1), wait=wait_fixed(5), reraise=True)
async def send_message(client: ClientSession):
    try:
        response = await client.post(f'https://discord.com/api/v9/channels/{CHANNEL}/messages',
                                     json={
                                         "content": MESSAGE,
                                         "tts": False,
                                         "flags": 0
                                     })
        data = await response.json()
        response.raise_for_status()
    except Exception:
        raise Exception(data['message'])


async def main():
    async with ClientSession(headers=HEADERS) as client:
        while True:
            try:
                await send_message(client)
                logger.success("Message sent successfully")

            except Exception as error:
                logger.error(error)

            finally:
                await asyncio.sleep(DELAY)


if __name__ == '__main__':
    print('Discord Message Sender @flamingoat\n')
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    CHANNEL = config["CHANNEL_ID"]
    MESSAGE = config["MESSAGE"]
    DELAY = config["DELAY"]

    asyncio.run(main())
