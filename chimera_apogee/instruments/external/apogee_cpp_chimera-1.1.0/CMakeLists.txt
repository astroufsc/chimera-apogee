cmake_minimum_required(VERSION 2.8)

project(APOGEE_CHIMERA)

ADD_DEFINITIONS(-c -g -fPIC )

#TODO : fazer funcionar com boost_python

include_directories(
	/opt/apogee/include/libapogee-2.1/apogee/
	/opt/apogee/include/
)

link_directories (
    /opt/apogee/lib/
)

add_library (
	apogee_chimera SHARED
	src/ApogeeAltaManager.cpp
	src/apgSampleCmn.cpp
)

target_link_libraries(
	apogee_chimera 
	ccd
	cfitsio
	apogee
	wcs
	usb
	curl
	tcl
)

SET_TARGET_PROPERTIES(apogee_chimera
                      PROPERTIES
                      VERSION 1.1.0
                      SOVERSION 1)

file(COPY src/ApogeeWrapper.py DESTINATION .)
file(COPY test/ApogeeWrapperTest.py DESTINATION .)

#install(TARGETS apogee_chimera DESTINATION /usr/bin)

