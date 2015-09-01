__author__ = 'lissu1'


i_range = range(8)

print('diamond')
   ##
  ####
 ######
########
 ######
  ####
   ##

half_i_range = int(len(i_range)/2)
for i in i_range:
    if i < half_i_range:
        hashtags = 2 * i + 2
        spaces = half_i_range - i - 1
        print(' ' * spaces, '#' * hashtags)
    else:
        hashtags = len(i_range)
        print(' ' * (i - (half_i_range - 1)), '#' * hashtags)

print()
print('diamond bottom')


########
 ######
  ####
   ##

for i in range(half_i_range):
    hashtags = len(i_range)-2 * i
    print(' ' * i, '#' * hashtags)

print()
print('rectangle bottom to top')


#####
####
###
##
#


for i in i_range:
    hashtags = len(i_range)-i
    print('#' * hashtags)

print('rectangle sideways')




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


