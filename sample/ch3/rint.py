csv = """\
e,x,s,y,t,a,f,c,b,g,e,c,s,s,w,w,p,w,o,p,n,s,m
e,f,y,n,t,a,f,c,b,p,e,r,s,y,w,w,p,w,o,p,k,s,p
p,x,y,w,t,p,f,c,n,k,e,e,s,s,w,w,p,w,o,p,k,s,g
e,b,s,w,t,l,f,c,b,g,e,c,s,s,w,w,p,w,o,p,n,s,m
e,f,f,g,f,n,f,c,n,p,e,e,s,s,w,w,p,w,o,p,k,v,u
e,b,y,y,t,l,f,c,b,g,e,c,s,s,w,w,p,w,o,p,n,n,g
e,x,y,n,t,a,f,c,b,w,e,r,s,y,w,w,p,w,o,p,n,y,p
e,x,f,w,f,n,f,w,b,p,t,e,s,f,w,w,p,w,o,e,k,s,g
e,x,s,w,t,l,f,w,n,w,t,b,s,s,w,w,p,w,o,p,n,v,d
e,b,s,w,t,l,f,c,b,w,e,c,s,s,w,w,p,w,o,p,n,s,m
e,f,s,y,t,a,f,w,n,w,t,b,s,s,w,w,p,w,o,p,n,v,d
e,x,s,y,t,a,f,c,b,k,e,c,s,s,w,w,p,w,o,p,n,n,m
e,f,f,g,f,n,f,c,n,g,e,e,s,s,w,w,p,w,o,p,n,y,u
e,b,s,y,t,a,f,c,b,n,e,c,s,s,w,w,p,w,o,p,k,s,g
e,x,s,w,t,l,f,c,b,g,e,c,s,s,w,w,p,w,o,p,n,n,m
e,x,y,w,t,l,f,c,b,n,e,c,s,s,w,w,p,w,o,p,n,s,m
e,f,s,w,t,a,f,w,n,n,t,b,s,s,w,w,p,w,o,p,n,v,d
e,x,y,y,t,l,f,c,b,w,e,c,s,s,w,w,p,w,o,p,n,s,g
e,b,s,w,t,l,f,c,b,w,e,c,s,s,w,w,p,w,o,p,k,s,g
e,x,s,w,t,a,f,c,b,g,e,c,s,s,w,w,p,w,o,p,k,n,g
e,x,f,w,f,n,f,w,b,h,t,e,f,s,w,w,p,w,o,e,k,s,g
e,f,y,n,t,l,f,c,b,n,e,r,s,y,w,w,p,w,o,p,k,y,p
p,x,s,w,t,p,f,c,n,k,e,e,s,s,w,w,p,w,o,p,n,v,u
e,b,s,w,t,a,f,c,b,n,e,c,s,s,w,w,p,w,o,p,n,n,g
e,b,s,w,t,a,f,c,b,k,e,c,s,s,w,w,p,w,o,p,k,s,m
e,b,y,w,t,l,f,c,b,n,e,c,s,s,w,w,p,w,o,p,n,n,g
e,b,y,w,t,a,f,c,b,w,e,c,s,s,w,w,p,w,o,p,k,n,g
e,x,s,y,t,a,f,c,b,w,e,c,s,s,w,w,p,w,o,p,k,s,g
e,b,s,w,t,l,f,c,b,w,e,c,s,s,w,w,p,w,o,p,k,n,m
e,x,f,y,t,a,f,w,n,n,t,b,s,s,w,w,p,w,o,p,n,v,d
e,x,f,g,f,n,f,c,n,n,e,e,s,s,w,w,p,w,o,p,n,y,u
e,f,y,y,t,a,f,c,b,n,e,r,s,y,w,w,p,w,o,p,n,s,g
e,b,s,w,t,l,f,c,b,n,e,c,s,s,w,w,p,w,o,p,k,n,m
e,x,s,y,t,a,f,c,b,g,e,c,s,s,w,w,p,w,o,p,k,s,g
e,x,y,y,t,a,f,c,b,k,e,c,s,s,w,w,p,w,o,p,k,s,g
e,x,y,w,t,l,f,c,b,w,e,c,s,s,w,w,p,w,o,p,n,s,g
e,s,f,g,f,n,f,c,n,p,e,e,s,s,w,w,p,w,o,p,n,v,u
e,x,s,w,t,a,f,c,b,n,e,c,s,s,w,w,p,w,o,p,n,n,m
p,x,s,w,t,p,f,c,n,k,e,e,s,s,w,w,p,w,o,p,k,s,g
e,x,y,y,t,a,f,c,b,n,e,r,s,y,w,w,p,w,o,p,n,s,g
e,f,f,w,t,a,f,w,n,p,t,b,s,s,w,w,p,w,o,p,n,v,d
e,x,y,w,t,l,f,c,b,g,e,c,s,s,w,w,p,w,o,p,k,n,m\
"""

splitted = csv.split("\n")

for item in splitted:
  list_mushroom = item.split(",")
  # print(list_mushroom)
  # 요소 하나를 선택
  # print(list_mushroom[0])
  # print(list_mushroom[-1])
  # print(list_mushroom[1:4])
  # print(list_mushroom[1:])
  print(list_mushroom[:14])