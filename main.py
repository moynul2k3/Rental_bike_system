from rental_system_for_bike import BikeRental, Customer


def main():
    bike_shop = BikeRental(50)
    customer = Customer()

    while True:
        print(
            """================================================================
    1. Display Available Bikes.
    2. Request a bike on hourly basis. Rent: 60 Tk per hour.
    3. Request a bike on daily basis. Rent: 500 Tk per day.
    4. Request a bike on weakly basis. Rent: 5000 Tk per weak.
    5. Return a bike.
    6. exit.
    
    """
        )
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("That is not a valid choice. Please, enter an integer number.")
            continue

        if choice == 1:
            bike_shop.display_stock()

        elif choice == 2:
            customer.rental_time = bike_shop.rent_bike_on_hourly_basis(
                customer.request_bikes())
            customer.rental_basis = 1

        elif choice == 3:
            customer.rental_time = bike_shop.rent_bike_on_daily_basis(
                customer.request_bikes())
            customer.rental_basis = 2

        elif choice == 4:
            customer.rental_time = bike_shop.rent_bike_on_weakly_basis(
                customer.request_bikes())
            customer.rental_basis = 3

        elif choice == 5:
            customer.bill = bike_shop.return_bike(customer.return_bike())
            customer.rental_basis, customer.rental_time, customer.return_bike = 0, 0, 0

        elif choice == 6:
            break

        else:
            print("Invalid choice! Please Enter a Number from the list below 1 - 6.")

        print("Thank you for rent a bike from us.")


if __name__ == "__main__":
    main()
