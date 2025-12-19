import asyncio
import aiohttp
from aiohttp_socks import ProxyConnector
from typing import Tuple, Optional
from config import TEST_URLS, TIMEOUT

async def check_proxy(proxy: str, protocol: str, semaphore: asyncio.Semaphore) -> Tuple[str, bool]:
    """
    Checks if a proxy is alive.
    For HTTP/HTTPS: uses aiohttp with proxy parameter.
    For SOCKS4/5: uses aiohttp_socks ProxyConnector.
    """
    async with semaphore:
        for test_url in TEST_URLS:
            try:
                # Prepare arguments for request
                session_kwargs = {}
                request_kwargs = {
                    'timeout': aiohttp.ClientTimeout(total=TIMEOUT),
                }

                if protocol in ('http', 'https'):
                    request_kwargs['proxy'] = f'http://{proxy}'
                    request_kwargs['ssl'] = False if protocol == 'https' else None
                elif protocol in ('socks4', 'socks5'):
                    connector = ProxyConnector.from_url(f'{protocol}://{proxy}')
                    session_kwargs['connector'] = connector
                else:
                    return proxy, False

                async with aiohttp.ClientSession(**session_kwargs) as session:
                    async with session.get(test_url, **request_kwargs) as response:
                        if response.status == 200:
                            return proxy, True

            except (
                aiohttp.ClientError,
                asyncio.TimeoutError,
                OSError,
                Exception
            ):
                continue
        
        return proxy, False
