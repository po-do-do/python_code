from wlkata_mirobot import WlkataMirobot
import time
import paho.mqtt.client as mqtt
import math

# 로봇 팔 객체 생성
arm = WlkataMirobot(portname='/dev/tty.usbserial-1110', debug=False)

forward_initial_angle = {1: -90.0, 2: -25.0, 3: 60.0, 4: 0.0, 5: 0.0, 6: 0.0}
reverse_initial_angle = {1: 90.0, 2: -20.0, 3: 60.0, 4: 0.0, 5: 0.0, 6: 0.0}
forward_store_angle = {1: -90.0, 2: 30.0, 3: 0.0, 4: 0.0, 5: -40.0, 6: 0.0}
reverse_store_angle = {1: 130.0, 2: 30.0, 3: 10.0, 4: 0.0, 5: -40.0, 6: 0.0}
before_store_angle_forward = {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0}
before_store_angle_reverse = {1: 130.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0}
after_store_angle_forward = {1: 0.0, 2: -20.0, 3: 60.0, 4: 0.0, 5: -20.0, 6: 0.0}
after_store_angle_reverse = {1: 130.0, 2: -20.0, 3: 60.0, 4: 0.0, 5: -20.0, 6: 0.0}
step_before_forward_target = {1: -90.0, 2: -30.0, 3: 10.0, 4: 10.0, 5: -90.0, 6: 0.0}
step_before_reverse_target = {1: 90.0, 2: -30.0, 3: 10.0, 4: 10.0, 5: -90.0, 6: 0.0}
a_11cm_600px = {1: -90.0, 2: 0.0, 3: -10.0, 4: 5.0, 5: -90.0, 6: 0.0}
a_9cm_500px = {1: -90.0, 2: 5.0, 3: -20.0, 4: 5.0, 5: -85.0, 6: 0.0}
a_7cm_400px = {1: -90.0, 2: 8.0, 3: -30.0, 4: 5.0, 5: -80.0, 6: 0.0}
a_30cm_300px = {1: -90.0, 2: 12.0, 3: -40.0, 4: 5.0, 5: -75.0, 6: 0.0}
a_28cm_200px = {1: -90.0, 2: 33.0, 3: -77.0, 4: 5.0, 5: -57.0, 6: 0.0}
a_26cm_100px = {1: -90.0, 2: 48.0, 3: -100.0, 4: 5.0, 5: -67.0, 6: 0.0}


a_11cm_600px_R = {1: 90.0, 2: 0.0, 3: -10.0, 4: 5.0, 5: -90.0, 6: 0.0}
a_9cm_500px_R = {1: 90.0, 2: 5.0, 3: -20.0, 4: 5.0, 5: -85.0, 6: 0.0}
a_7cm_400px_R = {1: 90.0, 2: 8.0, 3: -30.0, 4: 5.0, 5: -80.0, 6: 0.0}
a_30cm_300px_R = {1: 90.0, 2: 12.0, 3: -40.0, 4: 5.0, 5: -75.0, 6: 0.0}
a_28cm_200px_R = {1: 90.0, 2: 33.0, 3: -77.0, 4: 5.0, 5: -57.0, 6: 0.0}
a_26cm_100px_R = {1: 90.0, 2: 48.0, 3: -100.0, 4: 5.0, 5: -67.0, 6: 0.0}
#arm.set_joint_angle(step_before_forward_target)
#arm.set_joint_angle(a_26cm_100px)
#arm.set_joint_angle(a_28cm_200px)
#arm.set_joint_angle(a_30cm_300px)
#arm.set_joint_angle(a_7cm_400px)
#arm.set_joint_angle(a_9cm_500px)
#arm.set_joint_angle(a_11cm_600px)

# time.sleep(3)
#arm.gripper_open()
# arm.set_joint_angle(a_11cm_600px_after)

# arm.gripper_open()
# 160
#arm.set_slider_posi(150)
#arm.home() 
#arm.home_slider()
#arm.gripper_open()
#arm.gripper_close()

#arm.home_slider()
#a=calculate_gripper_x_position(arm, 593,400)
#print(a)
arm.set_slider_posi(485)
#arm.set_joint_angle(a_7cm_400px)
#arm.set_joint_angle(a_13cm_700px)
#arm.gripper_close()
#arm.gripper_open()
