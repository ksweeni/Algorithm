while(True):
  a = list(map(int,input().split( )))
  if(a[0] == a[1] and a[0]==0):
    break
  if(a[2]-a[1] == a[1]-a[0]):
    print('AP ', a[2]+(a[2]-a[1]))
  else:
    print('GP ', a[2]*(a[2]//a[1]))