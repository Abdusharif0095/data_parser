import logging
import validators
from http import HTTPStatus
from aiohttp import ClientSession


logger = logging.getLogger(__name__)


class Spider:
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; "
                      "rv:109.0) Gecko/20100101 Firefox/111.0",
    }

    async def get_url(self, url: str, base_url: str) -> tuple:
        try:
            if not self.is_valid_url(url, base_url):
                raise Exception(f"Url {url} is not valid!")
            async with ClientSession() as session:
                async with session.get(url, headers=self.headers) as response:
                    if response.status != HTTPStatus.OK:
                        raise Exception(f"Response code: {response.status}")
                    return await response.read(), response.status

        except Exception as error:
            logger.error(f"This error was received while getting data from {url}: {error}")
            return False, 400

    @classmethod
    def is_valid_url(cls, url: str, base_url: str) -> bool:
        return base_url in url and validators.url(url)
