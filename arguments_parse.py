import argparse


class Variables(object):
    """class with variables"""

    def __init__(self, tf_source_host, tf_dest_host, repo_name,
                 un_source, pwd_source, un_dest, pwd_dest):
        """Constructor"""
        self.tf_source_host = tf_source_host
        self.tf_dest_host = tf_dest_host
        self.repo_name = repo_name
        self.un_source = un_source
        self.pwd_source = pwd_source
        self.un_dest = un_dest
        self.pwd_dest = pwd_dest


parser = argparse.ArgumentParser(
    description="script for transfer tf assets between two Nexus 3 repository")
parser.add_argument("tf_source_host",
                    help="Root URL source Nexus 3 server; e.g., https://nexus.test.com")
parser.add_argument("tf_dest_host",
                    help="Root URL destination Nexus 3 server; e.g., https://nexus.test.com")
parser.add_argument("repo_name",
                    help="Name of repository whose assets will be transfer; e.g., dev-terraform-state")
parser.add_argument("un_source",
                    help="username source Nexus 3")
parser.add_argument("pwd_source",
                    help="password source Nexus 3")
parser.add_argument("un_dest",
                    help="username destination Nexus 3")
parser.add_argument("pwd_dest",
                    help="password destination Nexus 3")

args = parser.parse_args()

arg_init = Variables(tf_source_host=args.tf_source_host,
                     tf_dest_host=args.tf_dest_host,
                     repo_name=args.repo_name,
                     un_source=args.un_source,
                     pwd_source=args.pwd_source,
                     un_dest=args.un_dest,
                     pwd_dest=args.pwd_dest)
