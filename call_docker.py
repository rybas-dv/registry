import core


async def count_weight():
    tag_counter = 0
    layer_size = 0
    async with aiohttp.ClientSession(auth=aiohttp.BasicAuth(login=un, password=pwd)) as session:

        json_repo = await get_data(session, f'{host}/v2/_catalog')
        print(json_repo)
        for image in json_repo["repositories"]:
            json_tag = await get_data(session, f'{host}/v2/{image}/tags/list')
            print(image)
            print(json_tag)
            core.struct[tag_counter] = json_tag
            tag_counter += 1

        for m in range(tag_counter):
            url = f'{host}/v2/{core.struct[m]["name"]}/manifests/{core.struct[m]["tags"][m]}'
            async with session.get(url, headers={"Accept": "application/vnd.docker.distribution.manifest.v2+json"}) as resp:
                ma = await resp.json()
                for i in range(len(ma["layers"])):
                    layer_size += ma["layers"][i]["size"]
                final = {core.struct[m]["name"]: layer_size / 1000000}
                final_str = [final, core.struct[m]["tags"][m]]
            print(final_str)
    await session.close()