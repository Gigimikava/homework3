# class Celcius:
#   def __init__(self,temp):
#     self.__temp = temp
#   def get_temp(self):
#     return self.__temp
#   def set_temp(self, new_temp):
#     self.__temp = new_temp
#   def del_temp(self):
#     del self.__temp

#   temp = property(get_temp, set_temp, del_temp)

# t1 = Celcius(20)
# t2 = Celcius(100)
# print(t1.get_temp())
# print(t2.get_temp())

# t1.temp = 100
# t2.temp = 0
# print(t1.temp, t2.temp)

# del t1.temp
# del t2.temp