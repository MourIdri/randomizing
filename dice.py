import random
import threading
import time
import logging

number_of_users = 30
minimum_value = 1
maximum_value = 6 

logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-10s) %(message)s',)


# calculation service
def my_calculation(minimum_value,maximum_value):
    logging.debug('Starting my function service')
    var_result = random.randint(minimum_value,maximum_value)
    logging.debug('the function returned a value of : %d', var_result )
    logging.debug('Exiting my function service')

# worker activity 
def worker(minimum_value,maximum_value):
    logging.debug('Starting my worker process ')
    #time sleep
    #time.sleep(1)
    my_calculation(minimum_value,maximum_value)
    logging.debug('Exiting my worker process ')

# Threading 
for users in range(number_of_users) :
	users_count = users + 1 
	worker_user_name = 'WORKER %d ACTIVITY ' % users_count
	w = threading.Thread(name=worker_user_name, target=worker, args=(minimum_value,maximum_value,))
	w.start()

# Zeroing variables 
number_of_users = 0
minimum_value = 0
maximum_value = 0 
