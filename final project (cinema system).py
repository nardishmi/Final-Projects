

import random

list_film = ["Inception","Interstellar","Avatar","Titanic","The Dark Knight"]
list_sans = ["10:00-12:00","12:30-14:30","15:00-17:00","18:00-20:00","21:00-23:00"]
list_price = [250000, 300000, 350000, 200000, 280000]
list_sum_price = []
list_reserve = []
list_seats = []
list_paid = []
all_seats = []
for i in range(25):
    seats = []
    for j in range(30):
        seats.append(" ")
    all_seats.append(seats)
while True:
    print("cinema system")
    print("1.reserve Ticket")
    print("2.cancel Reservation")
    print("3.payment")
    print("4.show Seats")
    print("5.sales Report")
    print("6.exit")
    choice= input("Enter your choice: ")
    match choice:
        case "1":
            print("available movies:")
            for i in range(len(list_film)):
                print(i + 1, list_film[i])
            film_number= input("Choose movie number: ")
            if not film_number.isdigit():
                print("Invalid input!")
            elif int(film_number) < 1 or int(film_number) > 5:
                print("Invalid movie number!")
            else:
                film_number = int(film_number) - 1
                print("available sessions:")
                for i in range(len(list_sans)):
                    print(i + 1, list_sans[i])
                sans_number = input("Choose session number: ")
                if not sans_number.isdigit():
                    print("invalid input!")
                elif int(sans_number) < 1 or int(sans_number) > 5:
                    print("invalid session number!")
                else:
                    sans_number = int(sans_number) - 1
                    show_number = film_number * 5 + sans_number
                    empty_seats = []
                    for i in range(30):
                        if all_seats[show_number][i] == " ":
                            empty_seats.append(i)
                    print("Empty seats:", len(empty_seats))
                    ticket_number = input("enter ticket quantity: ")
                    if not ticket_number.isdigit():
                        print("invalid input!")
                    elif int(ticket_number) <= 0:
                        print("invalid ticket quantity!")
                    elif int(ticket_number) > len(empty_seats):
                        print("not enough empty seats!")
                    else:
                        ticket_number = int(ticket_number)
                        selected_seats = random.sample(
                            empty_seats, ticket_number)
                        total_price = ticket_number * list_price[film_number]
                        print("movie:", list_film[film_number])
                        print("session:", list_sans[sans_number])
                        print("ticket quantity:", ticket_number)
                        print("ticket price:", list_price[film_number])
                        print("total price:", total_price)
                        print("selected seats:")
                        for seat in selected_seats:
                            print(seat + 1, end=" ")
                        confirm = input("Confirm reservation? (yes/no): ")
                        if confirm.lower() == "yes":
                            for seat in selected_seats:
                                all_seats[show_number][seat] = "R"
                            list_reserve.append([film_number, sans_number, show_number])
                            list_seats.append(selected_seats)
                            list_sum_price.append(total_price)
                            list_paid.append(False)
                            print("reservation successful!")
                            print("reservation id:", len(list_reserve))
                        else:
                            print("reservation cancelled!")
        case "2":
            if len(list_reserve) == 0:
                print("no reservations found!")
            else:
                print("reservations:")
                for i in range(len(list_reserve)):
                    print("id:", i + 1,"movie:",list_film[list_reserve[i][0]],"session:",list_sans[list_reserve[i][1]],"tickets:",len(list_seats[i]),"paid:",list_paid[i])
                reserve_number = input("enter reservation id: ")
                if not reserve_number.isdigit():
                    print("invalid input!")
                elif int(reserve_number) < 1 or int(reserve_number) > len(list_reserve):
                    print("invalid reservation id!")
                else:
                    reserve_number = int(reserve_number) - 1
                    show_number = list_reserve[reserve_number][2]
                    for seat in list_seats[reserve_number]:
                        all_seats[show_number][seat] = " "
                    list_reserve.pop(reserve_number)
                    list_seats.pop(reserve_number)
                    list_sum_price.pop(reserve_number)
                    list_paid.pop(reserve_number)
                    print("reservation cancelled successfully!")
        case "3":
            unpaid_reservations = []
            for i in range(len(list_reserve)):
                if list_paid[i] == False:
                    unpaid_reservations.append(i)
            if len(unpaid_reservations) == 0:
                print("no unpaid reservations!")
            else:
                print("unpaid reservations:")
                for i in unpaid_reservations:
                    print("id:", i + 1,"movie:",list_film[list_reserve[i][0]],"session:",list_sans[list_reserve[i][1]],"total price:", list_sum_price[i])
                reserve_number = input("enter reservation id:")
                if not reserve_number.isdigit():
                    print("invalid input!")
                elif int(reserve_number) < 1 or int(reserve_number) > len(list_reserve):
                    print("invalid reservation id!")
                else:
                    reserve_number = int(reserve_number) - 1
                    if list_paid[reserve_number] == True:
                        print("this reservation is already paid!")
                    else:
                        print("amount to pay:", list_sum_price[reserve_number])
                        confirm = input("confirm payment? (yes/no): ")
                        if confirm.lower() == "yes":
                            list_paid[reserve_number] = True
                            show_number = list_reserve[reserve_number][2]
                            for seat in list_seats[reserve_number]:
                                all_seats[show_number][seat] = "S"
                            print("Payment successful!")
                            print("your tickets are confirmed!")
                        else:
                            print("Payment cancelled!")
        case "4":
            print("available movies:")
            for i in range(len(list_film)):
                print(i + 1, list_film[i])
            film_number = input("Choose movie number: ")
            if not film_number.isdigit():
                print("invalid input!")
            elif int(film_number) < 1 or int(film_number) > 5:
                print("invalid movie number!")
            else:
                film_number = int(film_number) - 1
                print("available sessions:")
                for i in range(len(list_sans)):
                    print(i + 1, list_sans[i])
                sans_number = input("Choose session number: ")
                if not sans_number.isdigit():
                    print("invalid input!")
                elif int(sans_number) < 1 or int(sans_number) > 5:
                    print("invalid session number!")
                else:
                    sans_number = int(sans_number) - 1
                    show_number = film_number * 5 + sans_number
                    print("movie:",list_film[film_number])
                    print("session:",list_sans[sans_number])
                    print("seat map")
                    print("R = reserved | S = sold | Number = empty")
                    for row in range(5):
                        for column in range(6):
                            seat_number = row * 6 + column
                            seat_status = all_seats[show_number][seat_number]
                            if seat_status == " ":
                                print(seat_number + 1, end="   ")
                            else:
                                print(seat_status, end="   ")
                        print()
                    empty_count = 0
                    reserved_count = 0
                    sold_count = 0
                    for seat in all_seats[show_number]:
                        if seat == " ":
                            empty_count += 1
                        elif seat == "R":
                            reserved_count += 1
                        elif seat == "S":
                            sold_count += 1
                    print("empty seats:", empty_count)
                    print("reserved seats:", reserved_count)
                    print("sold seats:", sold_count)
                    print("total seats:", 30)
        case "5":
            total_revenue = 0
            total_sold = 0
            total_reserved = 0
            total_empty = 0
            print(" sales report")
            for film_number in range(5):
                print("movie:", list_film[film_number])
                for sans_number in range(5):
                    show_number = film_number * 5 + sans_number
                    empty_count = 0
                    reserved_count = 0
                    sold_count = 0
                    for seat in all_seats[show_number]:
                        if seat == " ":
                            empty_count += 1
                        elif seat == "R":
                            reserved_count += 1
                        elif seat == "S":
                            sold_count += 1
                    print("session:", list_sans[sans_number])
                    print("sold tickets:", sold_count)
                    print("reserved tickets:", reserved_count)
                    print("empty seats:", empty_count)
                    total_sold += sold_count
                    total_reserved += reserved_count
                    total_empty += empty_count
            for i in range(len(list_reserve)):
                if list_paid[i] == True:
                    total_revenue += list_sum_price[i]
            print(" total report ")
            print("Total sold tickets:", total_sold)
            print("Total reserved tickets:", total_reserved)
            print("Total empty seats:", total_empty)
            print("Total revenue:")
        case "6":
            print("Thank you for using Cinema System!")
            break
        case _:
            print("invalid choice! Please try again.")
            