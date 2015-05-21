#!/usr/bin/python

from apogeemanager import ApogeeManager
import datetime

from astropy.io import fits
import time
import os

now = datetime.datetime.now()

manager = ApogeeManager() #"/tmp/python_image_test_" + now.strftime("%Y%m%d%H%M%S") + ".xxx" )
print manager.setUp()
print manager.stopCooling()
print manager.getTemperature()
print 'Doing a light frame...'
t0 = time.time()
print manager.expose('%s/test_light.fits' % os.path.realpath(os.path.curdir), .1, 1)
print 'took %3.2f' % (time.time() - t0)
t0 = time.time()
print 'Doing a dark frame...'
print manager.expose('%s/test_dark.fits' % os.path.realpath(os.path.curdir), 0, 0)
print 'took %3.2f' % (time.time() - t0)
t0 = time.time()
print 'Doing a bias frame...'
print manager.expose('%s/test_dark.fits' % os.path.realpath(os.path.curdir), .1, 0)
print 'took %3.2f' % (time.time() - t0)
t0 = time.time()
#print manager.getImageData()
#print fits.writeto('test.fits', manager.getImageData())
#manager.run()
print manager.getTemperature()
print manager.stop()
