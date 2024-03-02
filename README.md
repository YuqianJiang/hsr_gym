# HSR Gym

A modular gym environment for controlling the HSR with teleoperation. It has been used with [TeleMoma]().

## Installation

Install [tracikpy](https://github.com/mjd3/tracikpy)
```
git clone https://github.com/mjd3/tracikpy.git
pip install tracikpy/
```

Install HSR Gym
```
git clone https://github.com/YuqianJiang/hsr_gym.git
cd hsr_gym
pip install -r requirements.txt
pip install -e .
```

## HSR Dependencies

This package controls the HSR by function calls in ```hsrb_interface```.

If you would like to run TeleMoMa on the real HSR, please follow the documentation from Toyota to install the dependencies.

Alternatively, you want to use an open source HSR simulator like [this one](https://github.com/hsr-project/tmc_wrs_docker), you can get ```hsrb_interface``` [here](https://github.com/hsr-project/hsrb_interfaces/tree/master/hsrb_interface_py).