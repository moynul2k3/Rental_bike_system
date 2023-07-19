import datetime


class BikeRental:
    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        print(f"{self.stock} number of bike curently available in stock.")
        return self.stock

    def rent_bike_on_hourly_basis(self, n):
        if n <= 0:
            print(f"Number of bike cannot be negative or zero.")
            return None
        elif n > self.stock:
            print(f"Sorry! we don't have {n} of bike available. currently stock: {self.stock}")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You have successfully rented {n} bike on hourly basis at {now}.")
            print(f"You will be charged 60 taka per hour.")
            self.stock -= n
            return now

    def rent_bike_on_daily_basis(self, n):
        if n <= 0:
            print(f"Number of bike cannot be negative or zero.")
            return None
        elif n > self.stock:
            print(f"Sorry! we don't have {n} of bike available. currently stock: {self.stock}")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You have successfully rented {n} bike on daily basis at {now}.")
            print(f"You will be charged 500 taka per day.")
            self.stock -= n
            return now

    def rent_bike_on_weakly_basis(self, n):
        if n <= 0:
            print(f"Number of bike cannot be negative or zero.")
            return None
        elif n > self.stock:
            print(f"Sorry! we don't have {n} of bike available. currently stock: {self.stock}")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You have successfully rented {n} bike on weakly basis at {now}.")
            print(f"You will be charged 5000 taka per weak.")
            self.stock -= n
            return now

    def return_bike(self, request):
        rental_basis, rental_time, num_of_bike = request
        bill = 0

        if rental_basis and rental_time and num_of_bike:
            self.stock += num_of_bike
            now = datetime.datetime.now()
            rental_period = now - rental_time

            if rental_basis == 1:
                bill = round(rental_period.seconds/3600) * num_of_bike * 60

            elif rental_basis == 2:
                bill = round(rental_period.days) * num_of_bike * 500

            elif rental_basis == 3:
                bill = round(rental_period.days/7) * num_of_bike * 5000

            print(f"Thank you for renting {num_of_bike} from us. Your bill is: {bill}")
            return bill

        else:
            print(f"Are you sure that you have rented a bike from us?")
            return None


class Customer:
    def __init__(self):
        self.rental_basis = 0
        self.rental_time = 0
        self.bikes = 0
        self.bill = 0

    def request_bikes(self):
        bikes = input("How many bikes would you like to rent from us?")
        try:
            bikes = int(bikes)

        except ValueError:
            print(f"That is not a valid number.")
            return -1

        if bikes < 1:
            print(f"Invalid number! Number should be greater than zero.")
            return -1

        else:
            self.bikes = bikes

        return self.bikes

    def return_bike(self):
        if self.rental_basis and self.rental_time and self.bikes:
            return self.rental_basis, self.rental_time, self.bikes
        
        else:
            return 0,0,0
