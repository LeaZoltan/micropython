from util.drivecontrol import Controller

mycontroller = Controller()
mycontroller.start()

state = 0
turns_made = 0

while True:
    #Forwards state
    if state == 0:
        mycontroller.drive_forwards()

        #odometry based transition condition
        if mycontroller.left_odom.get_count() >= 1234 and mycontroller.right_odom.get_count() >= 1234:
            state = 1
            #reset the odometry counts
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()
        
    #turning state
    elif state == 1:
        mycontroller.raft.led_on()

        mycontroller.left_turn()
        #increase turns made counter
        turns_made += 1

        #two transition conditions
        if turns_made > 3:
            state = 2
        else:
            state = 0

    #stopping state
    elif state == 2:
        mycontroller.stop()