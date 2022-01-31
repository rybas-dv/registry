import core
import aiohttp

# 1 получить все images
# 2 получить все теги имеджа
# 3 получить манифест, в манифесте есть слои в виде sha


async def count_weight(host, un, pwd):
    tag_counter = 0
    layer_size = 0

    session = await core.session_obj(username=un, pwd=pwd)
    json_repo = await core.get_data(session, f'{host}/v2/_catalog')
    for image in json_repo["repositories"]:
        json_tag = await core.get_data(session, f'{host}/v2/{image}/tags/list')
        core.struct[tag_counter] = json_tag
        tag_counter += 1

    for m in core.struct:
        url = f'{host}/v2/{core.struct[m]["name"]}/manifests/{core.struct[m]["tags"][-1]}'
        async with session.get(url, headers={"Accept": "application/vnd.docker.distribution.manifest.v2+json"}) as resp:
            ma = await resp.json()
            for i in range(len(ma["layers"])):
                layer_size += ma["layers"][i]["size"]
                final = {core.struct[m]["name"]: layer_size / 1000000}
                final_str = [final, core.struct[m]["tags"][-1]]
                # layer_size = 0
                print(final_str)

    await session.close()
