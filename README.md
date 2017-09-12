# ROS Packages Downloader


## Description

Clone all official packages (core and 3rd party) available for certain ROS distribution (eg. Indigo, Groovy, Jade, etc.).
It extracts all git urls from repositories listed on the rosdistro url

## How to use

### Initialization
Git urls are gathered from the [`ros/rosdistro`](https://github.com/ros/rosdistro) repository which maintains a list of the available repositories for each ROS distribution.
[Download a copy](https://github.com/ros/rosdistro/archive/master.zip) of it and unzip it into the `ros-pkgs-downloader/` directory.

### Executing it
```
$ python download-them-all.py <distribution>

```
where `<distribution>` can be: `groovy`, `hydro`, `indigo`, `jade`, `kinetic` or `lunar`.


## Next steps
