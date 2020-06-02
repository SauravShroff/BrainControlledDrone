import airsim

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)


f1 = client.takeoffAsync()
f1.join()

state1 = client.getMultirotorState()
s = print(state1)

airsim.wait_key('Press any key to move vehicles')
f1 = client.moveToPositionAsync(-5, 5, -10, 5)
f1.join()
