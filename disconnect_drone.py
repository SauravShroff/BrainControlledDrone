import airsim

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(False)
