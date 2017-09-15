#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Pablo Estefo"
__license__ = "MIT"
__maintainer__ = "Pablo Estefo"
__email__ = "pestefo@gmail.com"
__status__ = "Development"

import os

def download_action(url):
    url = url[:-5]
    FIX!
    url = url+'/archive/master.zip'
    print "downloading "+url

def clone_action(url):
    print "git clone "+url

def repositories_iterate(distro, command):
    """ Applies and action, download (default), clone or print to a repository git url

    Keyword arguments:
    distro -- the name of the distribution. Eg. 'indigo', 'hydro', etc.
    action -- a function to apply to a repository git url.
    """
    global do_we_print

    urls_file = open("./"+distro+"/urls.txt","r")
    urls = urls_file.readlines()[1:]
    for url in urls:

    	#print command+'     '
    	#os.system(command)

        command(url)



# This program downloads all available packages for a ROS distribution
# It can also clone them instead of download.
from sys import argv, exit
import argparse # It works for Python 2.7

# Parsing arguments
parser = argparse.ArgumentParser(description='I download or clone all available packages for a ROS distribution.')

# Argument: ROS Distribution
parser.add_argument('-d','--distribution',help='Name of the distribution: groovy, hydro, indigo, jade, kinetic or lunar.', required=True)

# Option: Clone option is False by default
parser.add_argument('-c','--clone', help='Clone repositories instead of downloading them. You get the files plus the history of changes',required=False, action="store_true")


# Getting arguments and options
args = parser.parse_args()

distribution    = vars(args)['distribution']
do_we_clone     = args.clone

# defining the action to perform
action = 'download'
if do_we_clone: action = 'clone'


ros_distributions = ['groovy', 'hydro', 'indigo', 'jade', 'kinetic', 'lunar']
if distribution not in ros_distributions:
    err_msg = "\""+distribution+"\" is not a valid ROS distribution name.\nPlease, choose between: "+", ".join(ros_distributions)
    exit(err_msg)

#verify action is a valid action
actions = ['download', 'clone']
actions_map = {'download': download_action, "clone": clone_action}
if action not in actions:
    err_msg = "\""+action+"\" is not a valid action.\nPlease, choose between: "+", ".join(actions)
    exit(err_msg)


# apply the function
repositories_iterate(distribution,actions_map[action])
