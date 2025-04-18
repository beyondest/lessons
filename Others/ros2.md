
# Install ROS2 on Ubuntu 18.04

## Update Locale
```bash
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
```

## Install Required Packages
```bash
sudo apt update && sudo apt install curl gnupg2 lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

```bash
sudo apt update && sudo apt install -y \
  build-essential \
  cmake \
  git \
  python3-colcon-common-extensions \
  python3-pip \
  python-rosdep \
  python3-vcstool \
  wget
```

## Install Python Packages for Testing
```bash
python3 -m pip install -U \
  argcomplete \
  flake8 \
  flake8-blind-except \
  flake8-builtins \
  flake8-class-newline \
  flake8-comprehensions \
  flake8-deprecated \
  flake8-docstrings \
  flake8-import-order \
  flake8-quotes \
  pytest-repeat \
  pytest-rerunfailures \
  pytest \
  pytest-cov \
  pytest-runner \
  setuptools
```

## Install Fast-RTPS Dependencies
```bash
sudo apt install --no-install-recommends -y \
  libasio-dev \
  libtinyxml2-dev
```

## Install Cyclone DDS Dependencies
```bash
sudo apt install --no-install-recommends -y \
  libcunit1-dev
```

## Setup ROS2 Workspace
```bash
mkdir -p ~/ros2_dashing/src
cd ~/ros2_dashing
wget https://raw.githubusercontent.com/ros2/ros2/dashing/ros2.repos
vcs import src < ros2.repos
```

## Initialize rosdep
```bash
sudo rosdep init --include-eol-distros
rosdep update --include-eol-distros
rosdep install --from-paths src --rosdistro dashing -y -i --ignore-src --skip-keys "console_bridge fastcdr fastrtps libopensplice67 libopensplice69 rti-connext-dds-5.3.1 urdfdom_headers"
```

## Build the Workspace
```bash
cd ~/ros2_dashing/
colcon build --symlink-install
```

## Source the Setup Script
```bash
. ~/ros2_dashing/install/setup.bash  # or you can add this to bashrc
```

## Create a ROS2 Package
```bash
ros2 pkg create --build-type ament_python learning_pkg_python
```

## Initialize and Update rosdep (Without sudo)
```bash
sudo rosdep init
rosdep update   # (no sudo!!!)
```

## Install Additional Packages
```bash
sudo apt install python3-colcon-ros
# Auto complete
sudo apt-get install python3-argcomplete
```

## Useful Commands
- `rqt-graph`  // Something cool
- `/opt/ros2/dashing/share msg|srv|actions definition`

## Service Commands
```bash
ros2 srv package XXX
ros2 srv show XXX
```

## Run ROS2 Node
```bash
ros2 run <node_name> <program_name>
ros2 topic pub /ggbond std(tap) --qos(tap) best_effort
ros2 topic echo /ggbond
ros2 param list
ros2 param set 
ros2 param get
```

## Visualize in RViz
```bash
ros2 run rviz2 rviz2
```

## Show URDF in More Visible Mode
```bash
urdf urdf_to_graphiz **.urdf
evince **.pdf
```

## Install rosbag for Dashing
```bash
sudo apt-get install ros-dashing-ros2bag \
ros-dashing-rosbag2-converter-default-plugins \
ros-dashing-rosbag2-storage-default-plugins
```

## Multicast Commands
```bash
ros2 multicast send
ros2 multicast receive
```
