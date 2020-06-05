import airsim

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

print("taking off for 3 seconds")
client.takeoffAsync(3).join()
print("taking off completed")

# client.moveByAngleZAsync(0.5, 0, -100, 0, 1).join()

#  def moveByAngleThrottleAsync(self, pitch, roll, throttle, yaw_rate, duration, vehicle_name = ''):

# client.moveByAngleThrottleAsync(0, 0, 1, 0.5, 10).join()

print("moving for 10 seconds")
client.moveByAngleThrottleAsync(1, 1, 1, 1, 10).join()
print("move complete")

# client.moveByVelocityAsync(0, 1, -1, 3).join()
