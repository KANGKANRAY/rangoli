# -*- coding: utf-8 -*-
"""rangoli.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YqTMA1u8tUDd1hZVdIVKiilxqZEi98qq
"""

def rangoli(size) :
  n = size
  alpha = list(map(chr,range(97,123)))
  left_list = alpha[n-1::-1]
  right_list = alpha[1:n]
  one_list = left_list + right_list
  length = len(' '.join(one_list))
  for i in range(1,n) :
    print(' '.join(alpha[n-1:n-i:-1]+alpha[n-i:n]).center(length,' '))
  
  for i in range(n,0,-1) :
    print(' '.join(alpha[n-1:n-i:-1]+alpha[n-i:n]).center(length,' '))

if __name__ == '__main__':
  n = int(input())
  rangoli(n)