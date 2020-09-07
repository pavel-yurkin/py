from solution import *
#print(Car('Nissan', 'f1.jpg', '1.3', '5').photo_file_name)

cars = get_car_list('cars.csv')
print('>' + str(len(cars)))
print(cars)