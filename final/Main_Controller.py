from Ultrasonic import *
from time import sleep
#from LED_Controller import *
from Camera_Logic import *
from Image_Classification import *
#from Motor_Controller import *

COMPOST = '0'
LANDFILL = '1'
RECYCLE = '2'

num = 0
# Due to dynamic ip address on server, need to get current ip
# SERVER_IP = input('Enter IP Address of Server (Format: XX.XXX.XX.XXX): ')

while True:
   # if isMotionDetected():
    print("Motion Detected!")
    sleep(0.5)
    #lightCompartment()

    isObjectPresent, stream = confirmObjectPresence()
    print("Confirm Object Presence:", str(isObjectPresent))

    if True:
        classification = classifyImage(stream).decode('utf-8')
        print("Object Classification: ", str(classification))
        stream.close()

        # COMPOST: Center
        # RECYCLE: Left
        # LANDFILL: Right

        if classification == COMPOST:
            print("Compost")
            #flapMotion()

        elif classification == LANDFILL:
            print("Landfill")
            #moveReceptacleRight()
            #sleep(1.5)
            #right_DS_waitInRange()        # Wait for distance sensor
            #flapMotion()
            #moveReceptacleLeft()
            #sleep(1.5)
            #stopReceptacle()

        elif classification == RECYCLE:
            print("Recycle")
            #moveReceptacleLeft()
            #sleep(1.5)
            #left_DS_waitInRange()       # Wait for distance sensor
            #flapMotion()
            #moveReceptacleRight()
            #sleep(1.5)
            #stopReceptacle()
        #print("Here!")

        sleep(2)

    print("---------- Round", str(num), "----------\n")
    num = num + 1


