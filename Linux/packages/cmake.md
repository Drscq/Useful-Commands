# How to Fix CMake Version Issues on Ubuntu

## Problem:
CMake version too old, or apt errors due to malformed Kitware repository entry.

## Solution Steps:

1. Remove malformed Kitware repo file (if present):
```
sudo rm /etc/apt/sources.list.d/archive_uri-https_apt_kitware_com_ubuntu_jammy-jammy.list
```

2. Add the correct Kitware repository:

```
echo "deb https://apt.kitware.com/ubuntu/ jammy main" | sudo tee /etc/apt/sources.list.d/kitware.list
sudo apt update
```

3. Install or upgrade CMake:
```
sudo apt install cmake
cmake --version
```
