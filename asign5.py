#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:05:23 2019

@author: jonsilverman
"""

import sys


def mean_stat(nums):
    """

    >>> mean_stat([5, 3, 17])
    8.33

    >>> mean_stat([5])
    5.0

    >>> mean_stat([-1, 4, .5, 2.5])
    1.0
    """
    return sum(nums) / len(nums)





def median_stat(nums):
    
    nums.sort()
    cnt = len(nums)
    mid = int(cnt / 2)
    if cnt % 2 == 0:
        return (nums[mid] + nums[mid - 1]) / 2
    else:
        return nums[mid]

    
    
li1 = [1, 3, 5]
li2 = [2, 8, 6, 4]

cmd = sys.argv[1]
cmd = cmd.lower()
if cmd == 'mean':
    print('1) Mean statistics')
    print('List: {}, Average: {}'.format(li1, mean_stat(li1)))
    print('List: {}, Average: {}'.format(li2, mean_stat(li2)))    
elif cmd == 'median':
    print('\n3) Median statistics')
    print('List: {}, Median: {}'.format(li1, median_stat(li1)))
    print('List: {}, Median: {}'.format(li2, median_stat(li2)))
else:
    print('Command line: descr_stats <"mean | median">')