__author__ = 'lissu1'


i_range = range(4)



########
 ######
  ####
   ##

for i in i_range:
    hashtags = 2 * len(i_range)-2 * i
    print(' ' * i, '#' * hashtags)


print()


#####
####
###
##
#


for i in i_range:
    hashtags = len(i_range)-i
    print('#' * hashtags)

print()




#
##
###
####
###
##
#

half_i_range = len(i_range)/2
for i in i_range:
    if i < round(half_i_range):
        hashtags = i+1
        print('#' * hashtags)
    else:
        hashtags = len(i_range) - i
        print('#' * hashtags)


