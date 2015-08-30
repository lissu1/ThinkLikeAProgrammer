__author__ = 'lissu1'

# Print

#####
####
###
##
#

i_range = range(5)
for i in i_range:
    hashtags = len(i_range)-i
    print('#' * hashtags)

print()
#Print

#
##
###
####
###
##
#


i_range = range(30)
half_i_range = len(i_range)/2
for i in i_range:
    if i < round(half_i_range):
        hashtags = i+1
        print('#' * hashtags)
    else:
        hashtags = len(i_range) - i
        print('#' * hashtags)

