from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper



data = load(open("/Users/pestefo/Sync/projects/ros-pkgs-downloader/rosdistro/indigo/distribution.yaml"), Loader=Loader)

git_urls = open("/Users/pestefo/Sync/projects/ros-pkgs-downloader/rosdistro/indigo/urls.txt", "w")
repos_without_source = open("/Users/pestefo/Sync/projects/ros-pkgs-downloader/rosdistro/indigo/repos_no_git_url.txt", "w")

for r in data["repositories"].keys():
    try:
            # print data["repositories"][r]["source"]["url"]
            git_urls.write(data["repositories"][r]["source"]["url"]+"\n")
    except Exception as e:
            # print "\t"+r
            repos_without_source.write(r+"\n")

git_urls.close()
repos_without_source.close()
