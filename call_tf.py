import aiohttp
from arguments_pars import arg_init
from core import session_obj, get_data


async def transfer_tf(un, pwd, source_host, repo_name):
    session = await session_obj(username=un, pwd=pwd)
    json_repo = await get_data(session, f'{source_host}/service/rest/v1/assets?repository={repo_name}')

    for k in json_repo['items']:
        mod_path = str(k['path']).split('/')
        async with session.get(url=k['downloadUrl']) as resp:
            if resp.status == 200:
                print(resp.status)
                res = await resp.text()
                await upload_tf(un_dest=arg_init.un_dest,
                                pwd_dest=arg_init.pwd_dest,
                                tf_dest_host=arg_init.tf_dest_host,
                                repo_name=arg_init.repo_name,
                                path=mod_path[1], data=res, filename=mod_path[2])
    await session.close()


async def upload_tf(un_dest, pwd_dest, tf_dest_host, repo_name, path, data, filename):
    session = await session_obj(username=un_dest, pwd=pwd_dest)
    formdata = aiohttp.FormData()
    formdata.add_field('raw.directory', f'{path}', content_type='Content-Type: multipart/form-data')
    formdata.add_field('raw.asset1', f'{data}', content_type='Content-Type: multipart/form-data')
    formdata.add_field('raw.asset1.filename', f'{filename}', content_type='Content-Type: multipart/form-data')
    async with session.post(f'{tf_dest_host}/service/rest/v1/components?repository={repo_name}',
                            data=formdata) as resp:
        if resp.status == 204:
            print(f' state {filename} upload in {path}')
        else:
            print('Error')

    await session.close()
