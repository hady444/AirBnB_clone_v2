#!/usr/bin/python3
# Full deployment


from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy


def deploy():
    """ Full deployment """
    archive_file = do_pack()
    if not archive_file:
        return False
    return (do_deploy(archive_path))
