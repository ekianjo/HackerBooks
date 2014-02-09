#!/usr/bin/nawk -f
#
# A smattering of trigonometry...
#
# This AWK script plots the values from 0 to 360
# for the basic trigonometry functions
# but first - a review:
#
# (Note to the editor - the following diagram assumes
# a fixed width font, like Courier. 
# otherwise, the diagram  looks very stupid, instead of slightly stupid)
#
# Assume the following right triangle
#
#       Angle Y
#
#       |\
#       | \
#       |  \
#     a |   \  c
#       |    \
#       |     \
#       +-------   Angle X
#          b
#
# since the triangle is a right angle, then
#	X+Y=90
#
# Basic Trigonometric Functions. If you know the length
# of 2 sides, and the angles, you can find the length of the third side.
# Also - if you know the length of the sides, you can calculate 
# the angles.
#
# The formulas are
#
#	sine(X) = a/c
#	cosine(X) = b/c
#	tangent(X) = a/b
#
# reciprocal functions
#	cotangent(X) = b/a
#	secant(X) = c/b
#	cosecant(X) = c/a
#
# Example 1)
# if an angle is 30, and the hypotenuse (c) is 10, then
# 	a = sine(30) * 10 = 5
#	b = cosine(30) * 10 =  8.66
#
# The second example will be more realistic:
#
# 	Suppose you are looking for a Christmas tree, and
# while talking to your family, you smack into a tree
# because your head was turned, and your kids were arguing over who
# was going to put the first ornament on the tree.
#
# As you come to, you realize your feet are touching the trunk of the tree,
# and your eyes are 6 feet from the bottom of your frostbitten toes.
# While counting the stars that spin around your head, you also realize
# the top of the tree is located at a 65 degree angle, relative to your eyes.

# You suddenly realize the tree is 12.84 feet high! After all, 
# 	tangent(65 degrees) * 6 feet = 12.84 feet

# All right, it isn't realistic. Not many people memorize the
# tangent table, or can estimate angles that accurately. 
# I was telling the truth about the stars spinning around the head, however. 

#
BEGIN {
# assign a value for pi.
	PI=3.14159;
# select an "Ed Sullivan" number - really really big
	BIG=999999;	
# pick two formats
# Keep them close together, so when one column is made larger
# the other column can be adjusted to be the same width
	fmt1="%7s %8s %8s %8s %10s %10s %10s %10s\n";
# print out the title of each column
	fmt2="%7d %8.2f %8.2f %8.2f %10.2f %10.2f %10.2f %10.2f\n";
# old AWK wants a backslash at the end of the next line
# to continue the print statement
# new AWK allows you to break the line into two, after a comma
	printf(fmt1,"Degrees","Radians","Cosine","Sine", \
		"Tangent","Cotangent","Secant", "Cosecant");

	for (i=0;i<=360;i++) {
# convert degrees to radians
		r = i * (PI / 180 );
# in new AWK, the backslashes are optional
# in OLD AWK, they are required
		printf(fmt2, i, r, \
# cosine of r
		cos(r), \
# sine of r
		sin(r), \
#
# I ran into a problem when dividing by zero.
# So I had to test for this case.
#
# old AWK finds the next line too complicated
# I don't mind adding a backslash, but rewriting the
# next three lines seems pointless for a simple lesson.
# This script will only work with new AWK, now - sigh...
# On the plus side, 
#   I don't need to add those back slashes anymore
#
# tangent of r
		(cos(r) == 0) ? BIG : sin(r)/cos(r), 
# cotangent of r
		(sin(r) == 0) ? BIG : cos(r)/sin(r), 
# secant of r
		(cos(r) == 0) ? BIG : 1/cos(r), 
# cosecant of r
		(sin(r) == 0) ? BIG : 1/sin(r));
	}
# put an exit here, so that standard input isn't needed.
	exit;
}
