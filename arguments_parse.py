import argparse


class Variables(object):
    """class with variables"""

    def __init__(self, source_host, dest_host, repo_name,
                 un_source, pwd_source, un_dest, pwd_dest):
        """Constructor"""
        self.source_host = source_host
        self.dest_host = dest_host
        self.repo_name = repo_name
        self.un_source = un_source
        self.pwd_source = pwd_source
        self.un_dest = un_dest
        self.pwd_dest = pwd_dest


class VariablesDocker(object):
    """class with variables for docker"""

    def __init__(self, source_host, un_source, pwd_source):
        """Constructor"""
        self.source_host = source_host
        self.un_source = un_source
        self.pwd_source = pwd_source


master_parser = argparse.ArgumentParser(
    description="Utility for interacting with the nexus api")
subparse = master_parser.add_subparsers(dest='command')
docker_p = subparse.add_parser("docker-count",
                               help="Docker-registry api")
docker_p.add_argument("source_host",
                      help="Root URL source Nexus 3 server; e.g., https://nexus.test.com")
docker_p.add_argument("un_source",
                      help="username source Nexus 3")
docker_p.add_argument("pwd_source",
                      help="password source Nexus 3")

raw_p = subparse.add_parser("raw",
                            help="Raw repository api, script for transfer tf assets between two Nexus 3 repository")
raw_p.add_argument("source_host",
                   help="Root URL source Nexus 3 server; e.g., https://nexus.test.com")
raw_p.add_argument("dest_host",
                   help="Root URL destination Nexus 3 server; e.g., https://nexus.test.com")
raw_p.add_argument("repo_name",
                   help="Name of repository whose assets will be transfer; e.g., dev-terraform-state")
raw_p.add_argument("un_source",
                   help="username source Nexus 3")
raw_p.add_argument("pwd_source",
                   help="password source Nexus 3")
raw_p.add_argument("un_dest",
                   help="username destination Nexus 3")
raw_p.add_argument("pwd_dest",
                   help="password destination Nexus 3")

first_args = master_parser.parse_args()


async def arg_init():
    arg_init = Variables(source_host=first_args.source_host,
                         dest_host=first_args.dest_host,
                         repo_name=first_args.repo_name,
                         un_source=first_args.un_source,
                         pwd_source=first_args.pwd_source,
                         un_dest=first_args.un_dest,
                         pwd_dest=first_args.pwd_dest)
    return arg_init


async def arg_init_docker():
    arg_init = VariablesDocker(source_host=first_args.source_host,
                               un_source=first_args.un_source,
                               pwd_source=first_args.pwd_source)
    return arg_init
