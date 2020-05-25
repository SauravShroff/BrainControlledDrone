### This file is created to read data from the drone controller via USB.
### Due to the fact that only a single application can read rom an application,
### this file will then pass along its inputs to the autoquad1 drone sim made by UAVS@Berkeley (thanks guys!)
### make sure to pip install pyusb :)
### Author: Saurav Shroff

import usb.core