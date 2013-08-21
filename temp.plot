  GNU nano 2.2.6                          File: temp.plot                                                          


set size ratio 0.71
set terminal postscript enhanced landscape color solid
set output 'exemple.eps'

# set data syle line
# set style data l
set style fill transparent solid 0.50 noborder
set key out horiz
set key left top
set key bottom center

# limits horitzontals lines

set title "1308013-s1" font "Helvetica,12"
set xlabel "temps" font "Helvetica,8"
set ylabel "temperatura i humitat" font "Helvetica,10"



# Paper: max. temp. 21 C humitat min.30% max 50%
t_max = 21.00
t_min = 14.00
h_max = 50.00
h_min = 30.00



# Setting xdata to time precludes the use of histograms.
set xdata time
set timefmt "%H:%M:%S"
set format x "%H:%M:%S"
set xtics nomirror rotate font "Helvetica,8"
set ytic 0, 5

# set format x controls the way that gnuplot displays the dates on the x axis.

set size ratio -2
set grid


plot "/var/tmp/lectures.txt" using 3:1 with filledcurve y1=50 title "humitat", "/var/tmp/lectures.txt" using 3:2 w$



