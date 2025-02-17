from django.db import models
from datetime import datetime
from django_ckeditor_5.fields import CKEditor5Field
from multiselectfield import MultiSelectField

# Create your models here.

class Car(models.Model):
    
    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    
    Year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        Year_choice.append((r,r))
        
    feature_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )
    
    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    
    brand_choices = (
    ('Acura', 'Acura'),
    ('Alfa Romeo', 'Alfa Romeo'),
    ('Aston Martin', 'Aston Martin'),
    ('Audi', 'Audi'),
    ('Bentley', 'Bentley'),
    ('BMW', 'BMW'),
    ('Bugatti', 'Bugatti'),
    ('Buick', 'Buick'),
    ('Cadillac', 'Cadillac'),
    ('Chevrolet', 'Chevrolet'),
    ('Chrysler', 'Chrysler'),
    ('Citroën', 'Citroën'),
    ('Dacia', 'Dacia'),
    ('Daihatsu', 'Daihatsu'),
    ('Dodge', 'Dodge'),
    ('Ferrari', 'Ferrari'),
    ('Fiat', 'Fiat'),
    ('Ford', 'Ford'),
    ('Genesis', 'Genesis'),
    ('GMC', 'GMC'),
    ('Great Wall', 'Great Wall'),
    ('Haval', 'Haval'),
    ('Honda', 'Honda'),
    ('Hyundai', 'Hyundai'),
    ('Infiniti', 'Infiniti'),
    ('Isuzu', 'Isuzu'),
    ('Jaguar', 'Jaguar'),
    ('Jeep', 'Jeep'),
    ('Kia', 'Kia'),
    ('Koenigsegg', 'Koenigsegg'),
    ('Lamborghini', 'Lamborghini'),
    ('Lancia', 'Lancia'),
    ('Land Rover', 'Land Rover'),
    ('Lexus', 'Lexus'),
    ('Lincoln', 'Lincoln'),
    ('Lotus', 'Lotus'),
    ('Lucid', 'Lucid'),
    ('Mahindra', 'Mahindra'),
    ('Maserati', 'Maserati'),
    ('Maybach', 'Maybach'),
    ('Mazda', 'Mazda'),
    ('McLaren', 'McLaren'),
    ('Mercedes-Benz', 'Mercedes-Benz'),
    ('MG', 'MG'),
    ('Mini', 'Mini'),
    ('Mitsubishi', 'Mitsubishi'),
    ('Nio', 'Nio'),
    ('Nissan', 'Nissan'),
    ('Opel', 'Opel'),
    ('Pagani', 'Pagani'),
    ('Peugeot', 'Peugeot'),
    ('Polestar', 'Polestar'),
    ('Pontiac', 'Pontiac'),
    ('Porsche', 'Porsche'),
    ('Proton', 'Proton'),
    ('Ram', 'Ram'),
    ('Ravon', 'Ravon'),
    ('Renault', 'Renault'),
    ('Rimac', 'Rimac'),
    ('Rivian', 'Rivian'),
    ('Rolls-Royce', 'Rolls-Royce'),
    ('Saab', 'Saab'),
    ('Saturn', 'Saturn'),
    ('Scion', 'Scion'),
    ('Seat', 'Seat'),
    ('Skoda', 'Skoda'),
    ('Smart', 'Smart'),
    ('SsangYong', 'SsangYong'),
    ('Subaru', 'Subaru'),
    ('Suzuki', 'Suzuki'),
    ('Tata', 'Tata'),
    ('Tesla', 'Tesla'),
    ('Toyota', 'Toyota'),
    ('Vauxhall', 'Vauxhall'),
    ('Volkswagen', 'Volkswagen'),
    ('Volvo', 'Volvo'),
    ('Wuling', 'Wuling'),
    ('Zotye', 'Zotye'),
    ('Unknown', 'Unknown'),
)
    
    
    car_title = models.CharField(max_length=255)
    state = models.CharField(max_length=100, choices= state_choice)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    brand = models.CharField(max_length=20, choices=brand_choices, default='Unknown')
    model = models.CharField(max_length=100)
    Year = models.IntegerField(('year'), choices=Year_choice    )
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = CKEditor5Field('Text', config_name='extends')
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField( choices=feature_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=300)
    miles = models.IntegerField()
    doors = models.CharField(max_length=10, choices=door_choices)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    
    
    def __str__(self):
        return self.car_title
    
    