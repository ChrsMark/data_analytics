#!/usr/bin/env python
import sys, math
import Gnuplot, Gnuplot.funcutils

def generatePlot3D(filename):
    plot = Gnuplot.Gnuplot()
    plot("set terminal pngcairo size 640,480 enhanced font 'Verdana,10")
    plot("set output '{}'".format(filename))
    plot("set border 4095 front linetype 0 linewidth 1.000")
    plot("set view 60,30")
    plot("set xlabel 'r'")
    plot("set ylabel 'm'")
    plot("set zlabel 'time'")
    plot("set title 'Different x-y measurement'")
    plot("set ztics offset 1")
    plot("set zrange [0:20000]")
    plot("set palette defined (0.001 'green', 0.01 'yellow', 0.9 'red')")
    plot("set pm3d")
    plot.splot(Gnuplot.File('results_R_converted_time.txt', using=(1,2,3) ))#, with_="lines linecolor palette"))
    return

generatePlot3D("ex1_R_time.png")
