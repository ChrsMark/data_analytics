#!/bin/sh

wget http://downloads.sourceforge.net/project/gnuplot-py/Gnuplot-py/1.8/gnuplot-py-1.8.tar.gz
tar xzf gnuplot-py-1.8.tar.gz
cd gnuplot-py-1.8/ && python setup.py install
