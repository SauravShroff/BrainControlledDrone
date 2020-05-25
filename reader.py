### This file is created to read data from the drone controller via USB.
### Due to the fact that only a single application can read rom an application,
### this file will then pass along its inputs to the autoquad1 drone sim made by UAVS@Berkeley. (thanks guys!)
### Make sure to pip install pyusb :)
### Run with sudo https://www.urbandictionary.com/define.php?term=sudo
### Author: Saurav Shroff

import usb.core

ID_VENDOR = 0x0000 # Find id_vendor and id_prodcut by using lsusb on the command line
ID_PRODUCT = 0xFFFF
NUM_BYTES = 1024

dev = usb.core.find(idVendor = ID_VENDOR, idProduct = ID_PRODUCT)
endpoint = dev[0].interfaces()[0].endpoints()[0]
i = dev[0].interfaces()[0].bInterfaceNumber
dev.reset()

if dev.is_kernel_driver_active(i):
    dev.detach_kernel_driver(i)

dev.set_configuration()
endpointadr = endpoint.bEndpointAddress

ret = dev.read(endpointadr, NUM_BYTES)

print(len(ret))
print(ret)