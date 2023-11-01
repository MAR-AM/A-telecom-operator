#N=int(input('enter a nbr : '))
#for i in range (1,N+1):
#  triangle=''
#  for j in range (i):
#     triangle=triangle+str(i)
#  print(str(i)*i)


#N=int(input('enter a nbr : '))
#s=0
#for i in range (0,N+1):
 #   s=i*10**(i-1)
 #   print(s)


def durre(time):
  if time>30 and time<60:
     a=(time-30)*1.5+20
     return a
  elif time>60 and time<120:
     b=(time-60)*1+50
     return b
  elif time>120:
     c=(time-120)*0.5+100
     return c
  elif time<30:
     d=time*2
     return d
time=int(input('enter the communication duration in minutes :'))
print('\n')
print('the total to be paid at the end of the month is : ',durre(time),'DH')
print('\n')
print('Monthly subscription-----Free minutes-----Cost per minute')
print('     200DH                illimité             -----     ')
print('     100DH                 2h                  0.5DH     ')
print('      50DH                 1h                  1DH       ')
print('      20DH                 30min               1.5DH     ')
print('       0DH                 0h                  2DH       ')
print('\n')
print('the offer of 200 dh is the most interesting because you will get infinity time to communicate  :) ')