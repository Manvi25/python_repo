import logging
logging.basicConfig(level= logging.INFO, format= '%(message)s')
def string_mutation(s,position,character):
   #convert the given string to list
   string_list= list(s)
   string_list[position]= character
   logging.info(''.join(string_list))