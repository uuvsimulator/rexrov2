# BlueROV 2

This repository contains the robot description and necessary launch files to
simulate the BlueROV 2 unmanned underwater vehicle. This repository is complementary
to the [Unmanned Underwater Vehicle Simulator (UUV Simulator)](https://github.com/uuvsimulator/uuv_simulator),
an open-source project extending the simulation capabilities of the robotics
simulator Gazebo to underwater vehicles and environments. For installation and
usage instructions, please refer to the [documentation pages](https://uuvsimulator.github.io/).


## Requirements

To simulate the BlueROV 2 vehicle, please refer to the [UUV Simulator](https://github.com/uuvsimulator/uuv_simulator)
repository and follow the installation instructions of the package. Then you can clone
this package in the `src` folder of you catkin workspace

```
cd ~/catkin_ws/src
git clone https://github.com/fredvaz/bluerov2.git
```

and then build your catkin workspace

```bash
cd ~/catkin_ws
catkin_make # or <catkin build>, if you are using catkin_tools
```

## Example of usage

To run a demonstration with the vehicle with teleoperation, you can run a UUV
simulator Gazebo scenario, such as

```bash
roslaunch uuv_descriptions ocean_waves.launch
```

and then

```bash
roslaunch bluerov2_gazebo upload.launch
```

## License

RexROV 2 package is open-sourced under the Apache-2.0 license. See the
[LICENSE](LICENSE) file for details.
