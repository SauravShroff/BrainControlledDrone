import airsim


def disconnect_drone():
    client = airsim.MultirotorClient()
    client.confirmConnection()
    client.enableApiControl(False)


disconnect_drone()
