import asyncio
import call_tf
from arguments_parse import arg_init
from arguments_parse import first_args
from arguments_parse import arg_init_docker
from call_docker import count_weight


async def main():
    if first_args.command == "docker-count":
        arg = await arg_init_docker()
        await count_weight(host=arg.source_host,
                           un=arg.un_source,
                           pwd=arg.pwd_source)
    elif first_args.command == "raw":
        arg = await arg_init()
        await call_tf.transfer_tf(un=arg.un_source,
                                  pwd=arg.pwd_source,
                                  source_host=arg.source_host,
                                  repo_name=arg.repo_name)
    else:
        print("invalid argument")

asyncio.run(main())
