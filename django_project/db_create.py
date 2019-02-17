import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()

from django.contrib.auth.models import User
from carRental.models import CarModel, Car



def add_admin_user():
    password = 'Hasło123'
    my_admin = User.objects.create_superuser('admin2', 'admin@example.com', password)

def add_users():
    user = User.objects.create_user('Rejman', 'rejman@example.com', 'Hasło123')

def add_CarModel(mark, model, sort, doors, desc, price):
    m = CarModel.objects.get_or_create(
        mark = mark,
        model = model,
        sort = sort,
        doors = doors,
        desc = desc,
        price = price
    )[0]
    m.save()
    return m

carModels = []
carModels.append(add_CarModel('Citroen','Berlingo II','dostawcze','4','Rok produkcji: 2012 Silnik: 3.0 CDI V6 190KM 440 NM Nadwozie: van',350))
carModels.append(add_CarModel('Mercedes-Benz','Sprinter II','dostawcze','3','Rok produkcji: 2010 Silnik: 1.6 HDI 110 KM Nadwozie: kombivan', 200))
carModels.append(add_CarModel('Renault','Megane IV','osobowy','5','Rok produkcji: 2018 Silnik: 1.3 TCE 115KM 85KW Nadwozie: Hatchback', 200))
carModels.append(add_CarModel('Jaguar','F-TYPE','osobowy','2','Rok produkcji: 2013 Silnik:  V6 3.0 S/C 340 KM (250 kW) Nadwozie: Roadster/Coupé', 450))
carModels.append(add_CarModel('Jaguar','XE','osobowy','4','Rok produkcji: 2015 Silnik: 2.0 Turbo R4 237KM 340NM Nadwozie: Sedan', 450))
carModels.append(add_CarModel('Opel','Corsa E','osobowy','3','Rok produkcji: 2015 Silnik: R3 1.0 ECOTEC Direct Injection Turbo 90 KM Nadwozie: Hatchback', 100))
carModels.append(add_CarModel('Opel','Astra K','osobowy','5','Rok produkcji: 2015 Silnik: R4 1.6 CDTI 136 KM Nadwozie: Kombi', 150))


def add_Car(plate, color, CarModel):
    c = Car.objects.get_or_create(
        plate = plate,
        color = color,
        carModel = CarModel
        
        )[0]
    c.save()
    return c

add_Car('RZ1999V', 'Biały', carModels[2])
add_Car('RZ1778V', 'Biały', carModels[2])
add_Car('RZ1542V', 'Niebieski', carModels[2])
add_Car('RZ6473V', 'Biały', carModels[2])
add_Car('RZj574V', 'Czerwony', carModels[2])
add_Car('RZ0385V', 'Żółty', carModels[2])

add_Car('RZ1342V', 'Biały', carModels[1])
add_Car('RZ9667V', 'Biały', carModels[1])
add_Car('RZ8787V', 'Srebrny', carModels[1])

add_Car('RZd765V', 'Czerwony', carModels[2])
add_Car('RZf987V', 'Biały', carModels[2])
add_Car('RZ749jV', 'Żółty', carModels[2])

add_Car('RZ987dV', 'Biały', carModels[3])
add_Car('RZ345gV', 'Niebieski', carModels[3])
add_Car('RZ6ghyV', 'Żółty', carModels[3])

add_Car('RZ6578V', 'Czarny', carModels[4])
add_Car('RZ1119V', 'Biały', carModels[4])
add_Car('RZ8789V', 'Żółty', carModels[4])

add_Car('RZ6678V', 'Biały', carModels[5])
add_Car('RZ0989V', 'Granatowy', carModels[5])
add_Car('RZ5546V', 'Żółty', carModels[5])

add_Car('RZ8888V', 'Czarny', carModels[6])
add_Car('RZ1568V', 'Biały', carModels[6])
add_Car('RZ5442V', 'Beżowy', carModels[6])

add_admin_user()
#add_users()

        
