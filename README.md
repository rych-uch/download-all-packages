# ROS Packages Downloader


## Description

Clone all official packages (core and 3rd party) available for certain ROS distribution (eg. Indigo, Groovy, Jade, etc.).
It extracts all git urls from repositories listed on the rosdistro url

## How to use

### Dependencies

- PyYAML - [website](http://pyyaml.org/)

### Repositories cache
Each ROS distribution directory has two files inside:

- `urls.txt`: list of urls of official repositories for a certain ROS distribution.
- `no_url.txt`: list of repositories that not specified an url for their source.

To update it, a fresh copy of the repository [ros/rosdistro](https://github.com/ros/rosdistro) needs to be downloaded to run `repositories_cache_generator.py`. 

### Executing it

For downloading a zip file of each repository:
```
$ python download-them-all.py -d=<distribution>
```
where `<distribution>` can be: `groovy`, `hydro`, `indigo`, `jade`, `kinetic` or `lunar`.

Use `-c`or `--clone` to clone each repository instead of

## Next steps

- Have a cached list of git repositories per distribution that would be updated on demand. This way the *Initialization* step it won't be needed.
