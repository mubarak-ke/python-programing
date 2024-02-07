speed_limit=70
speed=int(input("enter speed"))
if speed <= speed_limit:
    print ("ok")
else:
      demerit_point=round((speed-speed_limit)/5)
      if demerit_point>12:
           print("license suspended")
      else:
           print("demerit points")
