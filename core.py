import aiohttp

struct = {}
manifest = []


async def get_data(session, url):
    async with session.get(url, headers={'accept': 'application/json'}) as resp:
        data = await resp.json()
        return data


async def session_obj(username, pwd):
    session = aiohttp.ClientSession(auth=aiohttp.BasicAuth(login=username, password=pwd))
    return session
