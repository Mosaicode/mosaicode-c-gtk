#!/bin/sh
python setup.py install --record files.txt
cat files.txt | xargs rm -rf
rm -rf files.txt
rm -rf build
rm -rf dist
rm -rf mosaicode_c_gtk.egg-info
rm -rf usr/local/lib/python2.7/dist-packages/mosaicode_c_gtk-1.0-py2.7.egg
