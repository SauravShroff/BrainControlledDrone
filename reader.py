### This file is created to read data from the drone controller via USB.
### Due to the fact that only a single application can read rom an application,
### this file will then pass along its inputs to the autoquad1 drone sim made by UAVS@Berkeley. (thanks guys!)
### Make sure to pip install pyusb :)
### Run with sudo https://www.urbandictionary.com/define.php?term=sudo
### Author: Saurav Shroff

import usb.core

ID_VENDOR = 0x045e # Find id_vendor and id_prodcut by using lsusb on the command line
ID_PRODUCT = 0x02d1
NUM_BYTES = 1024

dev = usb.core.find(idVendor = ID_VENDOR, idProduct = ID_PRODUCT)
print("dev:")
print(dev)
endpoint = dev[0].interfaces()[0].endpoints()[0]
print("endpoint:")
print(endpoint)
i = dev[0].interfaces()[0].bInterfaceNumber
print("i:")
print(i)
dev.reset()
print("successfully reset")

if dev.is_kernel_driver_active(i):
    dev.detach_kernel_driver(i)
print("detach confirmed")

dev.set_configuration()
endpoint_adr = endpoint.bEndpointAddress

ret = dev.read(endpoint_adr, NUM_BYTES)

print(len(ret))
print(ret)



# #debug test
# import os
# os.environ['PYUSB_DEBUG'] = 'debug'
# import usb.core
# usb.core.find()
