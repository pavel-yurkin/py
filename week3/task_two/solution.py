import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
         try:
            photo = self.photo_file_name.split('.')
            if len(photo) == 2 and photo[0] != '':
                value = '.' + photo[1]
                if value == '.jpg' or value == '.jpeg' or value == '.png' or value == '.gif':
                    return value
                else:
                    photo[len(photo)]
            else:
                photo[len(photo)]
         except(IndexError):
             return None


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.brand = brand
        self.car_type = 'car'
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        try:
            if int(passenger_seats_count) < 0:
                raise ValueError
            self.passenger_seats_count = int(passenger_seats_count)
        except(ValueError):
            self.passenger_seats_count = -1



class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.car_type = 'truck'
        try:
            if body_whl == '':
                body_whl = '0.0x0.0x0.0'
            store = body_whl.split('x')

            try:
                if len(store) > 3:
                    raise ValueError
                float(store[0])
                float(store[1])
                float(store[2])
            except ValueError:
                store = [0, 0, 0]

            self.body_length = float(store[0])
            self.body_width = float(store[1])
            self.body_height = float(store[2])
        except(IndexError):
            self.body_whl = -1

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.car_type = 'spec_machine'
        self.extra = extra

def check_for_float(carrying):
    try:
        float(carrying)
    except ValueError:
        return False
    return True

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            if len(row) != 7:
                continue

            if not check_for_float(row[5]):
                continue

            if row[1] == '':
                continue

            if row[0] == 'car':
                if Car(row[1], row[3], row[5], row[2]).get_photo_file_ext() != None and Car(row[1], row[3], row[5], row[2]).passenger_seats_count != -1:
                    car_list.append(Car(row[1], row[3], row[5], row[2]))

            if row[0] == 'truck':
                if Truck(row[1], row[3], row[5], row[4]).get_photo_file_ext() != None:
                    car_list.append(Truck(row[1], row[3], row[5], row[4]))

            if row[0] == 'spec_machine':
                if SpecMachine(row[1], row[3], row[5], row[6]).get_photo_file_ext() != None and row[6] != '':
                    car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
    return car_list

