import aiohttp
import asyncio
import core

#1 получить все images
#2 получить все теги имеджа
#3 получить манифест, в манифесте есть слои в виде sha

async def get_data(session, url):
    async with session.get(url) as resp:
        data = await resp.json()
        return data

async def main():

    tag_counter = 0
    layer_size = 0

    async with aiohttp.ClientSession() as session:
        json_repo = await get_data(session, 'http://172.16.0.122:8081/repository/doc/v2/_catalog')

        for image in json_repo["repositories"]:
            json_tag = await get_data(session, f'http://172.16.0.122:8081/repository/doc/v2/{image}/tags/list')

            core.struct[tag_counter] = json_tag
            tag_counter += 1

        for m in range(tag_counter):
            url =f'http://172.16.0.122:8081/repository/doc/v2/{core.struct[m]["name"]}/manifests/{int(core.struct[m]["tags"][0])}'
            async with session.get(url, headers={"Accept": "application/vnd.docker.distribution.manifest.v2+json"}) as resp:
                ma = await resp.json()
                for i in range(len(ma["layers"])):
                    layer_size += ma["layers"][i]["size"]
                final = {core.struct[m]["name"]:layer_size / 1000000}
                final_str =[final, core.struct[m]["tags"][0]]
                print(final_str)


asyncio.run(main())