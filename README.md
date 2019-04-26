# RexROV 2

[![Build Status](https://travis-ci.org/uuvsimulator/rexrov2.svg?branch=master)](https://travis-ci.org/uuvsimulator/rexrov2)
[![GitHub issues](https://img.shields.io/github/issues/uuvsimulator/rexrov2.svg)](https://github.com/uuvsimulator/rexrov2/issues)
![License](https://img.shields.io/badge/license-Apache%202-blue.svg)

> Link to the `rexrov2` repository [here](https://github.com/uuvsimulator/rexrov2)

> Link to the [documentation page](https://uuvsimulator.github.io/packages/rexrov2/intro/)

> Chat on [Discord](https://discord.gg/zNauF2F)

This repository contains the robot description and necessary launch files to
simulate the RexROV 2 unmanned underwater vehicle. This repository is complementary
to the [Unmanned Underwater Vehicle Simulator (UUV Simulator)](https://github.com/uuvsimulator/uuv_simulator),
an open-source project extending the simulation capabilities of the robotics
simulator Gazebo to underwater vehicles and environments. For installation and
usage instructions, please refer to the [documentation pages](https://uuvsimulator.github.io/).

The dimensions and parameters for the RexROV 2 are derived from the published
model parameters for the SF 30k ROV [1].

[[1] Berg, Viktor. Development and Commissioning of a DP system for ROV SF 30k. MS thesis. Institutt for marin teknikk, 2012.](https://brage.bibsys.no/xmlui/handle/11250/238170)

![RexROV 2](images/rexrov2.png)

## Purpose of the project

This software is a research prototype, originally developed for the EU ECSEL
Project 662107 [SWARMs](http://swarms.eu/).

The software is not ready for production use. However, the license conditions of the
applicable Open Source licenses allow you to adapt the software to your needs.
Before using it in a safety relevant setting, make sure that the software
fulfills your requirements and adjust it according to any applicable safety
standards (e.g. ISO 26262).

## Requirements

To simulate the RexROV 2 vehicle, please refer to the [UUV Simulator](https://github.com/uuvsimulator/uuv_simulator)
repository and follow the installation instructions of the package. Then you can clone
this package in the `src` folder of you catkin workspace

```
cd ~/catkin_ws/src
git clone https://github.com/uuvsimulator/rexrov2.git
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
roslaunch rexrov2_gazebo start_demo_pid_controller.launch teleop_on:=true joy_id:=0
```

The teleoperation nodes are pre-configured per default for the XBox 360
controller.

## License

RexROV 2 package is open-sourced under the Apache-2.0 license. See the
[LICENSE](https://github.com/uuvsimulator/rexrov2/blob/master/LICENSE) file for details.
