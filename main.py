import asyncio
import call_tf
from arguments_parse import arg_init


async def main():
    # await count_weight()
    await call_tf.transfer_tf(un=arg_init.un_source,
                              pwd=arg_init.pwd_source,
                              source_host=arg_init.tf_source_host,
                              repo_name=arg_init.repo_name)

asyncio.run(main())
