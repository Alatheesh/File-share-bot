import aiohttp
import logging


logger = logging.getLogger(__name__)

async def get_shortlink(link):
    url = f'{SHORT_URL}/api'
    params = {
        'api': SHORT_API,
        'url': link,
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
                data = await response.json()
                if data["status"] == "success":
                    return data['shortenedUrl']
                else:
                    logger.error(f"Error: {data['message']}")
                    return link
    except Exception as e:
        logger.error(e)
        return link
