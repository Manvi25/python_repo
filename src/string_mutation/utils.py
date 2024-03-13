import logging
logging.basicConfig(level= logging.INFO, format= '%(message)s')
def string_mutation():
   s = input().strip()
   position, character = map(str, input().split())
   pos=int(position)
   #convert the given string to list
   string_list= list(s)
   string_list[pos]= character
   logging.info(''.join(string_list))
   return ''.join(string_list)