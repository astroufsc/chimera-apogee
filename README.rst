chimera_apogee plugin
=====================

This is a plugin for Apogee Alta cameras on the chimera observatory control system https://github.com/astroufsc/chimera.


Installation
------------

    sudo apt-get install libapogee-dev cfitsio-dev wcs-dev libwcstools-dev libusb-dev tcl-dev libcurl4-openssl-dev wcslib-dev


Tested cameras
--------------

* Apogee Alta U47

Configuration Example
---------------------

    camera:
        name: alta_u47
        type: Apogee

