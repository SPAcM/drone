#!/usr/bin/python

#AUTHOR Kevin Thao
#VERSION 1.0.0



#sixaxis library for taking input from the controller
import sixaxis 
#libardrone for controlling the drone
import libardrone

#initialize the controller, default device is /dev/input/js0
sixaxis.init("/dev/input/js0")

#make new drone object
#NOTE: networking must have already been configured and the pi must already be connected over wifi to the drone
drone = libardrone.ARDrone()

loop = True

while loop:
    #Declare/Initialize/Reset Variables
    select = 0
    start = 0
    ps = 0
    #Not being used
    b_up = 0
    #Not being used
    b_right = 0
    #Not Being used
    b_down = 0
    #Not being used
    b_left = 0
    triangle = 0
    circle = 0
    #Not being used
    cross = 0
    #Not being used
    square = 0
    trig0 = 0
    trig1 = 0
    trig2 = 0
    trig3 = 0
    leftx_move_left = 0
    leftx_move_right = 0
    lefty_move_fwd = 0
    lefty_move_bwd = 0
    rightx_turn_left = 0
    rightx_turn_right = 0
    righty_move_up = 0
    righty_move_down = 0
    hover = 1
    #Gets the state of controller
    state = sixaxis.get_state()

    #Buttons
    if state['select'] == True:
        print ("select")
	select = 1
    elif state['start'] == True:
        print ("start")
	start = 1
    elif state['ps'] == True:
        print ("ps")
	ps = 1
    #Not being used
    elif state['buttonup'] == True:
        print ("buttonup")
	b_up = 1
    #Not being used
    elif state['buttonright'] == True:
        print ("buttonright")
	b_right = 1
    #Not being used
    elif state['buttondown'] == True:
        print ("buttondown")
	b_down = 1
    #Not being used
    elif state['buttonleft'] == True:
        print ("buttonleft")
	b_left = 1
    elif state['triangle'] == True:
        print ("triangle")
	triangle = 1
    elif state['circle'] == True:
        print ("circle")
	circle = 1
    #Not being used
    elif state['cross'] == True:
        print ("cross")
	cross = 1
    #Not being used
    elif state['square'] == True:
        print ("square")
	square = 1
    elif state['trig0'] == True:
        print ("trig0")
	trig0 = 1
    elif state['trig1'] == True:
        print ("trig ")
	trig1 = 1
    elif state['trig2'] == True:
        print ("trig2")
	trig2 = 1
    elif state['trig3'] == True:
        print ("trig3")
	trig3 = 1
    #Joystick 
    elif state['leftx'] < 0:
        print ( "left <---")
 	leftx_move_left = 1
	hover = 0
    elif state['leftx'] > 0:
        print ("left --->")
	leftx_move_right = 1
	hover = 0
    elif state['lefty'] < 0:
        print ("leftstickup")
	lefty_move_fwd = 1
	hover = 0
    elif state['lefty'] > 0:
        print ("leftstickdown")
	lefty_move_bwd = 1
	hover = 0
    elif state['rightx'] < 0:
        print ("right <---")
	rightx_turn_left = 1
	hover = 0
    elif state['rightx'] > 0:
        print ("right --->")
	rightx_turn_right = 1
	hover = 0
#right y axis disabled, mapped to the d-pad instead
    elif state['righty'] < 0:
        print ("rightstickup")
	righty_move_up = 1
	hover = 0
    elif state['righty'] > 0:
        print ("rightstickdown")
	righty_move_down = 1
	hover = 0
    #Logic for moving the drone
    #Button Logic
    if select == 1:
	drone.land()
	print ("Landing")
    if start == 1:
	drone.takeoff()
	print ("Taking off")
    if ps == 1:
	drone.reset()
	print ("Reset")
    if triangle == 1:
	drone.halt()
	print ("Closing drone pipeline")
    if circle == 1:
	print ("Exiting Program")
	loop = False
    if trig0 == 1:
	drone.speed = 0.1
	print ("Speed set to 0.1")
    if trig1 == 1:
	drone.speed = 0.3
	print ("Speed set to 0.3")
    if trig2 == 1:
	drone.speed = 0.7
	print ("Speed set to 0.7")
    if trig3 == 1:
	drone.speed = 1.0
	print ("Speed set to 1.0")

    #Drone movement
    #Drone hovers in place
    if hover == 1:
	drone.hover()
    #Left joystick drone movement
    if leftx_move_left == 1:
	drone.move_left()
    elif leftx_move_right == 1:
	drone.move_right()
    if lefty_move_fwd == 1:
	drone.move_forward()
    elif lefty_move_bwd == 1:
	drone.move_backward()
    #Right joystick drone movement
    if rightx_turn_left == 1:
	drone.turn_left()
    elif rightx_turn_right == 1:
	drone.turn_right()
    #changed from right stick to d-pad for vertical movement
    if b_up == 1:
	drone.move_up()
    elif b_down == 1:
	drone.move_down()

#Close all pipelines
drone.halt()
sixaxis.shutdown()
