import asyncio
import aiohttp
from typing import List


async def fetch_url(session: aiohttp.ClientSession, url: str, fetch_timeout: int) -> str:
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=fetch_timeout)) as response:
            return await response.text()
    except Exception:
        return ''


async def fetch_all_sources(urls: List[str], fetch_timeout: int) -> str:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url, fetch_timeout) for url in urls]
        results = await asyncio.gather(*tasks)
        return '\n'.join(results)
