import logging
Format="%(asctime)s:%(levelname)s:%(lineno)d:%(message)s"
logging.basicConfig(filename="app.log",level=logging.DEBUG,force=True,format=Format)
a=range(2,5)
li=[]
try:
  for i in fjh:
      li.append(i)
      # Manually creating exception
  # if(len(li)==3):
  #   raise Exception
except Exception as e:
  logging.debug(f"Error:{e}")
else:
  print(li)
finally:
  print("I will run no matter if the program is sucessful or not")
  print("It is created to close things like database or anythings that ca lead to disruotion")
