#!/usr/bin/python3
"""Deploy an archive to my web servers"""

from fabric import api
from fabric.contrib import files
import os

api.env.hosts = ['54.144.142.186', '100.27.14.169']
api.env.user = 'ubuntu'


def do_deploy(archive_path):
    """Deploy `archive_path` to web servers.
    """
    if not os.path.isfile(archive_path):
        return False
    with api.cd('/tmp'):
        basename = os.path.basename(archive_path)
        root, ext = os.path.splitext(basename)
        outpath = '/data/web_static/releases/{}'.format(root)
        try:
            putpath = api.put(archive_path)
            if files.exists(outpath):
                api.run('rm -rdf {}'.format(outpath))
            api.run('mkdir -p {}'.format(outpath))
            api.run('tar -xzf {} -C {}'.format(putpath[0], outpath))
            api.run('rm -f {}'.format(putpath[0]))
            api.run('mv -u {}/web_static/* {}'.format(outpath, outpath))
            api.run('rm -rf {}/web_static'.format(outpath))
            api.run('rm -rf /data/web_static/current')
            api.run('ln -sf {} /data/web_static/current'.format(outpath))
            print('New version deployed!')
        except Exception as e:
            return False
        else:
            return True
