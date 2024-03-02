import rospy
from hsr_gym.tiago.tiago_gym import HSRGym

rospy.init_node('hsr_teleop')
from telemoma.input_interface.teleop_policy import TeleopPolicy
from telemoma.configs.only_human_kpts import teleop_config

env = HSRGym(
        frequency=10,
        head_policy=None,
        base_enabled=True,
        torso_enabled=False,
        arm_enabled=True,
    )
obs = env.reset(reset_arms=True)

teleop = TeleopPolicy(teleop_config)
teleop.start()


def shutdown_helper():
    teleop.stop()

rospy.on_shutdown(shutdown_helper)

count = 0
while not rospy.is_shutdown():
    action = teleop.get_action(obs)

    if action.right is not None and action.right[-1] == 0:
        break
    obs, _, _, _ = env.step(action)

shutdown_helper()