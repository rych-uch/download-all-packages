#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Pablo Estefo"
__license__ = "MIT"
__maintainer__ = "Pablo Estefo"
__email__ = "pestefo@gmail.com"
__status__ = "Development"

"""
I just generate a list of repositories for each ROS distribution from the distribution.yaml file specified in ros/rosdistro
"""
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


# verify distribution is a valid ros distribution name
ros_distributions = ['groovy', 'hydro', 'indigo', 'jade', 'kinetic', 'lunar']

for distro in ros_distributions:
    urls = []
    repos_without_url = []
    urls_file = open("./"+distro+"/urls.txt", "w")
    repos_without_url_file = open("./"+distro+"/no_url.txt", "w")

    # path to distribution.yaml file
    path_to_distribution_yaml = "./rosdistro/"+distro+"/distribution.yaml"
    data = load(open(path_to_distribution_yaml), Loader=Loader)

    for r in data["repositories"].keys():
        try:
            urls.append(data["repositories"][r]["source"]["url"])
        except Exception as e:
            repos_without_url.append(r)

    # writing
    urls_file.write('# List of urls of official repositories for ROS '+distro+'\n')
    urls_file.write('\n'.join(urls))

    repos_without_url_file.write('# List of repositories that not specified an url for their source in the distribution.yaml file\n')
    repos_without_url_file.write('\n'.join(repos_without_url))

    # closing files
    urls_file.close()
    repos_without_url_file.close()
