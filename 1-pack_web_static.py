#!/usr/bin/python3
"""This script compresses a folder before sending"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        - Archive path if generated successfully.
        - None if the archive generation fails.
    """
    local('mkdir -p versions')

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_filename = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}.tgz".format(archive_filename)

    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.failed:
        return None
    return archive_path
