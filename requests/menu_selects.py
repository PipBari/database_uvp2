import tkinter as tk

from requests.sql_requests import *


def insert_passport_menu():
    insert_window = tk.Toplevel()
    insert_window.title("Insert Passport")

    passport_label = tk.Label(insert_window, text="Enter passport number:")
    passport_label.pack()

    passport_entry = tk.Entry(insert_window)
    passport_entry.pack()

    dob_label = tk.Label(insert_window, text="Enter date of birth (YYYY-MM-DD):")
    dob_label.pack()

    date_of_birth_entry = tk.Entry(insert_window)
    date_of_birth_entry.pack()

    country_label = tk.Label(insert_window, text="Enter country:")
    country_label.pack()

    country_entry = tk.Entry(insert_window)
    country_entry.pack()

    nationality_label = tk.Label(insert_window, text="Enter nationality:")
    nationality_label.pack()

    nationality_entry = tk.Entry(insert_window)
    nationality_entry.pack()

    submit_button = tk.Button(insert_window, text="Submit", command=lambda: insert_passport(
        session,
        passport_entry.get(),
        date_of_birth_entry.get(),
        country_entry.get(),
        nationality_entry.get()))
    submit_button.pack()


def insert_passenger_menu():
    insert_window = tk.Toplevel()
    insert_window.title("Insert Passenger")

    passport_label = tk.Label(insert_window, text="Enter passport number:")
    passport_label.pack()

    passport_entry = tk.Entry(insert_window)
    passport_entry.pack()

    first_name_label = tk.Label(insert_window, text="Enter first name:")
    first_name_label.pack()

    first_name_entry = tk.Entry(insert_window)
    first_name_entry.pack()

    second_name_label = tk.Label(insert_window, text="Enter second name:")
    second_name_label.pack()

    second_name_entry = tk.Entry(insert_window)
    second_name_entry.pack()

    email_label = tk.Label(insert_window, text="Enter email:")
    email_label.pack()

    email_entry = tk.Entry(insert_window)
    email_entry.pack()

    phone_label = tk.Label(insert_window, text="Enter phone:")
    phone_label.pack()

    phone_entry = tk.Entry(insert_window)
    phone_entry.pack()

    gender_label = tk.Label(insert_window, text="Enter gender:")
    gender_label.pack()

    gender_entry = tk.Entry(insert_window)
    gender_entry.pack()

    submit_button = tk.Button(insert_window, text="Submit", command=lambda: insert_passenger(
        session,
        passport_entry.get(),
        first_name_entry.get(),
        second_name_entry.get(),
        email_entry.get(),
        phone_entry.get(),
        gender_entry.get()))
    submit_button.pack()


def insert_bonus_programm_menu():
    insert_window = tk.Toplevel()
    insert_window.title("Insert Passport")

    passenger_id_label = tk.Label(insert_window, text="Enter passenger ID:")
    passenger_id_label.pack()

    passenger_id_entry = tk.Entry(insert_window)
    passenger_id_entry.pack()

    reservation_id_label = tk.Label(insert_window, text="Enter reservation ID:")
    reservation_id_label.pack()

    reservation_id_entry = tk.Entry(insert_window)
    reservation_id_entry.pack()

    name_programm_label = tk.Label(insert_window, text="Enter program name:")
    name_programm_label.pack()

    name_programm_entry = tk.Entry(insert_window)
    name_programm_entry.pack()

    mil_value_label = tk.Label(insert_window, text="Enter mileage value:")
    mil_value_label.pack()

    mil_value_entry = tk.Entry(insert_window)
    mil_value_entry.pack()

    relaxzone_label = tk.Label(insert_window, text="Enter relax zone (True/False):")
    relaxzone_label.pack()

    relaxzone_var = tk.BooleanVar()
    relaxzone_checkbox = tk.Checkbutton(insert_window, text="Is Relaxzone On Time", variable=relaxzone_var)
    relaxzone_checkbox.pack()

    submit_button = tk.Button(insert_window, text="Submit", command=lambda: insert_bonus_programm(
        session,
        passenger_id_entry.get(),
        reservation_id_entry.get(),
        name_programm_entry.get(),
        mil_value_entry.get(),
        relaxzone_var.get()))
    submit_button.pack()


def insert_reservation_menu():
    insert_window = tk.Toplevel()
    insert_window.title("Insert Reservation")

    ticket_number_label = tk.Label(insert_window, text="Enter ticket number:")
    ticket_number_label.pack()

    ticket_number_entry = tk.Entry(insert_window)
    ticket_number_entry.pack()

    reservation_date_label = tk.Label(insert_window, text="Enter reservation date (YYYY-MM-DD):")
    reservation_date_label.pack()

    reservation_date_entry = tk.Entry(insert_window)
    reservation_date_entry.pack()

    submit_button = tk.Button(insert_window, text="Submit", command=lambda: insert_reservation(
        session,
        ticket_number_entry.get(),
        reservation_date_entry.get()))
    submit_button.pack()


def insert_ticket_menu():
    insert_window = tk.Toplevel()
    insert_window.title("Insert Ticket")

    flight_id_label = tk.Label(insert_window, text="Enter flight ID:")
    flight_id_label.pack()

    flight_id_entry = tk.Entry(insert_window)
    flight_id_entry.pack()

    datepay_ticket_label = tk.Label(insert_window, text="Enter ticket payment date (YYYY-MM-DD):")
    datepay_ticket_label.pack()

    datepay_ticket_entry = tk.Entry(insert_window)
    datepay_ticket_entry.pack()

    numplace_ticket_label = tk.Label(insert_window, text="Enter ticket seat number:")
    numplace_ticket_label.pack()

    numplace_ticket_entry = tk.Entry(insert_window)
    numplace_ticket_entry.pack()

    submit_button = tk.Button(insert_window, text="Submit", command=lambda: insert_ticket(
        session,
        flight_id_entry.get(),
        datepay_ticket_entry.get(),
        numplace_ticket_entry.get()))
    submit_button.pack()


def insert_flight_menu():
    insert_window = tk.Toplevel()
    insert_window.title("Insert Flight")

    arrival_airport_label = tk.Label(insert_window, text="Enter arrival airport:")
    arrival_airport_label.pack()

    arrival_airport_entry = tk.Entry(insert_window)
    arrival_airport_entry.pack()

    departure_airport_label = tk.Label(insert_window, text="Enter departure airport:")
    departure_airport_label.pack()

    departure_airport_entry = tk.Entry(insert_window)
    departure_airport_entry.pack()

    plane_num_label = tk.Label(insert_window, text="Enter plane number:")
    plane_num_label.pack()

    plane_num_entry = tk.Entry(insert_window)
    plane_num_entry.pack()

    flight_date_label = tk.Label(insert_window, text="Enter flight date (YYYY-MM-DD):")
    flight_date_label.pack()

    flight_date_entry = tk.Entry(insert_window)
    flight_date_entry.pack()

    flight_status_label = tk.Label(insert_window, text="Flight Status:")
    flight_status_label.pack()

    flight_status_var = tk.BooleanVar()
    flight_status_checkbox = tk.Checkbutton(insert_window, text="Is Flight On Time", variable=flight_status_var)
    flight_status_checkbox.pack()

    submit_button = tk.Button(insert_window, text="Submit", command=lambda: insert_flight(
        session,
        arrival_airport_entry.get(),
        departure_airport_entry.get(),
        plane_num_entry.get(),
        flight_date_entry.get(),
        flight_status_var.get()))
    submit_button.pack()


def insert_airport_menu():
    insert_window = tk.Toplevel()
    insert_window.title("Insert Airport")

    airport_name_label = tk.Label(insert_window, text="Enter airport name:")
    airport_name_label.pack()

    airport_name_entry = tk.Entry(insert_window)
    airport_name_entry.pack()

    airport_country_label = tk.Label(insert_window, text="Enter airport country:")
    airport_country_label.pack()

    airport_country_entry = tk.Entry(insert_window)
    airport_country_entry.pack()

    city_label = tk.Label(insert_window, text="Enter city:")
    city_label.pack()

    city_entry = tk.Entry(insert_window)
    city_entry.pack()

    terminal_label = tk.Label(insert_window, text="Enter terminal:")
    terminal_label.pack()

    terminal_entry = tk.Entry(insert_window)
    terminal_entry.pack()

    gate_label = tk.Label(insert_window, text="Enter gate:")
    gate_label.pack()

    gate_entry = tk.Entry(insert_window)
    gate_entry.pack()

    submit_button = tk.Button(insert_window, text="Submit", command=lambda: insert_airport(
        session,
        airport_name_entry.get(),
        airport_country_entry.get(),
        city_entry.get(),
        terminal_entry.get(),
        gate_entry.get()))
    submit_button.pack()


def insert_plane_menu():
    insert_window = tk.Toplevel()
    insert_window.title("Insert Plane")

    plane_num_label = tk.Label(insert_window, text="Enter plane number:")
    plane_num_label.pack()

    plane_num_entry = tk.Entry(insert_window)
    plane_num_entry.pack()

    model_plane_label = tk.Label(insert_window, text="Enter plane model:")
    model_plane_label.pack()

    model_plane_entry = tk.Entry(insert_window)
    model_plane_entry.pack()

    name_plane_label = tk.Label(insert_window, text="Enter plane name:")
    name_plane_label.pack()

    name_plane_entry = tk.Entry(insert_window)
    name_plane_entry.pack()

    factplane_num_label = tk.Label(insert_window, text="Enter actual number of planes:")
    factplane_num_label.pack()

    factplane_num_entry = tk.Entry(insert_window)
    factplane_num_entry.pack()

    submit_button = tk.Button(insert_window, text="Submit", command=lambda: insert_plane(
        session,
        plane_num_entry.get(),
        model_plane_entry.get(),
        name_plane_entry.get(),
        factplane_num_entry.get()))
    submit_button.pack()


def delete_passport_menu():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Passport")

    passport_label = tk.Label(delete_window, text="Enter passport number:")
    passport_label.pack()

    passport_entry = tk.Entry(delete_window)
    passport_entry.pack()

    submit_button = tk.Button(delete_window, text="Submit",
                              command=lambda: delete_passport(passport_entry.get(), delete_window))
    submit_button.pack()


def delete_passenger_menu():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Passenger")

    passenger_label = tk.Label(delete_window, text="Enter passenger ID:")
    passenger_label.pack()

    passenger_entry = tk.Entry(delete_window)
    passenger_entry.pack()

    submit_button = tk.Button(delete_window, text="Submit",
                              command=lambda: delete_passenger(passenger_entry.get(), delete_window))
    submit_button.pack()


def delete_bonus_programm_menu():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Bonus Program")

    bonus_programm_label = tk.Label(delete_window, text="Enter bonus program ID:")
    bonus_programm_label.pack()

    bonus_programm_entry = tk.Entry(delete_window)
    bonus_programm_entry.pack()

    submit_button = tk.Button(delete_window, text="Submit",
                              command=lambda: delete_bonus_programm(bonus_programm_entry.get(), delete_window))
    submit_button.pack()


def delete_reservation_menu():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Reservation")

    reservation_label = tk.Label(delete_window, text="Enter reservation ID:")
    reservation_label.pack()

    reservation_entry = tk.Entry(delete_window)
    reservation_entry.pack()

    submit_button = tk.Button(delete_window, text="Submit",
                              command=lambda: delete_reservation(reservation_entry.get(), delete_window))
    submit_button.pack()


def delete_ticket_menu():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Ticket")

    ticket_label = tk.Label(delete_window, text="Enter ticket ID:")
    ticket_label.pack()

    ticket_entry = tk.Entry(delete_window)
    ticket_entry.pack()

    submit_button = tk.Button(delete_window, text="Submit",
                              command=lambda: delete_ticket(ticket_entry.get(), delete_window))
    submit_button.pack()


def delete_flight_menu():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Flight")

    flight_label = tk.Label(delete_window, text="Enter flight ID:")
    flight_label.pack()

    flight_entry = tk.Entry(delete_window)
    flight_entry.pack()

    submit_button = tk.Button(delete_window, text="Submit",
                              command=lambda: delete_flight(flight_entry.get(), delete_window))
    submit_button.pack()


def delete_plane_menu():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Plane")

    plane_label = tk.Label(delete_window, text="Enter plane number:")
    plane_label.pack()

    plane_entry = tk.Entry(delete_window)
    plane_entry.pack()

    submit_button = tk.Button(delete_window, text="Submit",
                              command=lambda: delete_plane(plane_entry.get(), delete_window))
    submit_button.pack()


def delete_airport_menu():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Airport")

    airport_label = tk.Label(delete_window, text="Enter airport code-name:")
    airport_label.pack()

    airport_entry = tk.Entry(delete_window)
    airport_entry.pack()

    submit_button = tk.Button(delete_window, text="Submit",
                              command=lambda: delete_airport(airport_entry.get(), delete_window))
    submit_button.pack()


def select_passport_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Passport")

    passport_label = tk.Label(select_window, text="Enter passport number:")
    passport_label.pack()

    passport_entry = tk.Entry(select_window)
    passport_entry.pack()

    dob_label = tk.Label(select_window, text="Enter date of birth (YYYY-MM-DD):")
    dob_label.pack()

    date_of_birth_entry = tk.Entry(select_window)
    date_of_birth_entry.pack()

    country_label = tk.Label(select_window, text="Enter country:")
    country_label.pack()

    country_entry = tk.Entry(select_window)
    country_entry.pack()

    nationality_label = tk.Label(select_window, text="Enter nationality:")
    nationality_label.pack()

    nationality_entry = tk.Entry(select_window)
    nationality_entry.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_passport(
        session,
        passport_entry.get(),
        date_of_birth_entry.get(),
        country_entry.get(),
        nationality_entry.get()))
    submit_button.pack()


def select_passenger_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Passenger")

    passenger_id_label = tk.Label(select_window, text="Enter passenger ID:")
    passenger_id_label.pack()

    passenger_id_entry = tk.Entry(select_window)
    passenger_id_entry.pack()

    pass_number_label = tk.Label(select_window, text="Enter passport number:")
    pass_number_label.pack()

    pass_number_entry = tk.Entry(select_window)
    pass_number_entry.pack()

    first_name_label = tk.Label(select_window, text="Enter first name:")
    first_name_label.pack()

    first_name_entry = tk.Entry(select_window)
    first_name_entry.pack()

    second_name_label = tk.Label(select_window, text="Enter second name:")
    second_name_label.pack()

    second_name_entry = tk.Entry(select_window)
    second_name_entry.pack()

    email_label = tk.Label(select_window, text="Enter email:")
    email_label.pack()

    email_entry = tk.Entry(select_window)
    email_entry.pack()

    phone_label = tk.Label(select_window, text="Enter phone:")
    phone_label.pack()

    phone_entry = tk.Entry(select_window)
    phone_entry.pack()

    gender_label = tk.Label(select_window, text="Enter gender:")
    gender_label.pack()

    gender_entry = tk.Entry(select_window)
    gender_entry.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_passenger(
        session,  # Add the 'session' parameter here
        passenger_id_entry.get(),
        pass_number_entry.get(),
        first_name_entry.get(),
        second_name_entry.get(),
        email_entry.get(),
        phone_entry.get(),
        gender_entry.get()
    ))
    submit_button.pack()


def select_bonus_programm_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Bonus Program")

    programm_id_label = tk.Label(select_window, text="Enter program ID:")
    programm_id_label.pack()

    programm_id_entry = tk.Entry(select_window)
    programm_id_entry.pack()

    passenger_id_label = tk.Label(select_window, text="Enter passenger ID:")
    passenger_id_label.pack()

    passenger_id_entry = tk.Entry(select_window)
    passenger_id_entry.pack()

    reservation_id_label = tk.Label(select_window, text="Enter reservation ID:")
    reservation_id_label.pack()

    reservation_id_entry = tk.Entry(select_window)
    reservation_id_entry.pack()

    name_programm_label = tk.Label(select_window, text="Enter program name:")
    name_programm_label.pack()

    name_programm_entry = tk.Entry(select_window)
    name_programm_entry.pack()

    mil_value_label = tk.Label(select_window, text="Enter mileage value:")
    mil_value_label.pack()

    mil_value_entry = tk.Entry(select_window)
    mil_value_entry.pack()

    relaxzone_label = tk.Label(select_window, text="Enter relax zone (True/False):")
    relaxzone_label.pack()

    relaxzone_var = tk.BooleanVar()
    relaxzone_checkbox = tk.Checkbutton(select_window, text="Is Relaxzone On Time", variable=relaxzone_var)
    relaxzone_checkbox.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_bonus_programm(
            session,
            programm_id_entry.get(),
            passenger_id_entry.get(),
            reservation_id_entry.get(),
            name_programm_entry.get(),
            mil_value_entry.get(),
            relaxzone_var.get()
        )
    )
    submit_button.pack()


def select_reservation_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Reservation")

    reservation_id_label = tk.Label(select_window, text="Enter reservation ID:")
    reservation_id_label.pack()

    reservation_id_entry = tk.Entry(select_window)
    reservation_id_entry.pack()

    ticket_number_label = tk.Label(select_window, text="Enter ticket number:")
    ticket_number_label.pack()

    ticket_number_entry = tk.Entry(select_window)
    ticket_number_entry.pack()

    reservation_date_label = tk.Label(select_window, text="Enter reservation date:")
    reservation_date_label.pack()

    reservation_date_entry = tk.Entry(select_window)
    reservation_date_entry.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_reservation(
            session,
            reservation_id_entry.get(),
            ticket_number_entry.get(),
            reservation_date_entry.get()
        )
    )
    submit_button.pack()


def select_ticket_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Ticket")

    ticket_number_label = tk.Label(select_window, text="Enter ticket number:")
    ticket_number_label.pack()

    ticket_number_entry = tk.Entry(select_window)
    ticket_number_entry.pack()

    flight_id_label = tk.Label(select_window, text="Enter flight ID:")
    flight_id_label.pack()

    flight_id_entry = tk.Entry(select_window)
    flight_id_entry.pack()

    ticket_payment_date_label = tk.Label(select_window, text="Enter date of payment ticket (YYYY-MM-DD):")
    ticket_payment_date_label.pack()

    ticket_payment_date_entry = tk.Entry(select_window)
    ticket_payment_date_entry.pack()

    seat_number_label = tk.Label(select_window, text="Enter seat number:")
    seat_number_label.pack()

    seat_number_entry = tk.Entry(select_window)
    seat_number_entry.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_ticket(
            session,
            ticket_number_entry.get(),
            flight_id_entry.get(),
            ticket_payment_date_entry.get(),
            seat_number_entry.get()))
    submit_button.pack()


def select_flight_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Flight")

    flight_id_label = tk.Label(select_window, text="Enter flight ID:")
    flight_id_label.pack()

    flight_id_entry = tk.Entry(select_window)
    flight_id_entry.pack()

    departure_airport_label = tk.Label(select_window, text="Enter departure airport:")
    departure_airport_label.pack()

    departure_airport_entry = tk.Entry(select_window)
    departure_airport_entry.pack()

    arrival_airport_label = tk.Label(select_window, text="Enter arrival airport:")
    arrival_airport_label.pack()

    arrival_airport_entry = tk.Entry(select_window)
    arrival_airport_entry.pack()

    plane_num_label = tk.Label(select_window, text="Enter plane number:")
    plane_num_label.pack()

    plane_num_entry = tk.Entry(select_window)
    plane_num_entry.pack()

    flight_date_label = tk.Label(select_window, text="Enter flight date (YYYY-MM-DD):")
    flight_date_label.pack()

    flight_date_entry = tk.Entry(select_window)
    flight_date_entry.pack()

    flight_status_label = tk.Label(select_window, text="Enter flight status (True/False):")
    flight_status_label.pack()

    flight_status_var = tk.BooleanVar()
    flight_status_checkbox = tk.Checkbutton(select_window, text="Is flight status On Time", variable=flight_status_var)
    flight_status_checkbox.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_flight(
            session,
            flight_id_entry.get(),
            departure_airport_entry.get(),
            arrival_airport_entry.get(),
            plane_num_entry.get(),
            flight_date_entry.get(),
            flight_status_var.get()))
    submit_button.pack()


def select_airport_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Airports")

    airport_name_label = tk.Label(select_window, text="Enter airport name:")
    airport_name_label.pack()

    airport_name_entry = tk.Entry(select_window)
    airport_name_entry.pack()

    airport_country_label = tk.Label(select_window, text="Enter airport country:")
    airport_country_label.pack()

    airport_country_entry = tk.Entry(select_window)
    airport_country_entry.pack()

    city_label = tk.Label(select_window, text="Enter city:")
    city_label.pack()

    city_entry = tk.Entry(select_window)
    city_entry.pack()

    terminal_label = tk.Label(select_window, text="Enter terminal:")
    terminal_label.pack()

    terminal_entry = tk.Entry(select_window)
    terminal_entry.pack()

    gate_label = tk.Label(select_window, text="Enter gate:")
    gate_label.pack()

    gate_entry = tk.Entry(select_window)
    gate_entry.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_airport(
            session,
            airport_name_entry.get(),
            airport_country_entry.get(),
            city_entry.get(),
            terminal_entry.get(),
            gate_entry.get()))
    submit_button.pack()


def select_plane_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Plane")

    plane_num_label = tk.Label(select_window, text="Enter plane number:")
    plane_num_label.pack()

    plane_num_entry = tk.Entry(select_window)
    plane_num_entry.pack()

    model_plane_label = tk.Label(select_window, text="Enter model plane:")
    model_plane_label.pack()

    model_plane_entry = tk.Entry(select_window)
    model_plane_entry.pack()

    name_plane_label = tk.Label(select_window, text="Enter name plane:")
    name_plane_label.pack()

    name_plane_entry = tk.Entry(select_window)
    name_plane_entry.pack()

    factplane_num_label = tk.Label(select_window, text="Enter factplane number:")
    factplane_num_label.pack()

    factplane_num_entry = tk.Entry(select_window)
    factplane_num_entry.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_plane(
            session,
            plane_num_entry.get(),
            model_plane_entry.get(),
            name_plane_entry.get(),
            factplane_num_entry.get()))
    submit_button.pack()


def show_update_passport_form(session, passports):
    update_window = tk.Toplevel()
    update_window.title("Update Passport")

    selected_passport = tk.StringVar()
    selected_passport.set(passports[0].pass_number)

    passport_label = tk.Label(update_window, text="Select passport to update:")
    passport_label.pack()

    passport_menu = tk.OptionMenu(update_window, selected_passport, *[passport.pass_number for passport in passports])
    passport_menu.pack()

    dob_label = tk.Label(update_window, text="Enter new date of birth (YYYY-MM-DD):")
    dob_label.pack()

    date_of_birth_entry = tk.Entry(update_window)
    date_of_birth_entry.pack()

    country_label = tk.Label(update_window, text="Enter new country:")
    country_label.pack()

    country_entry = tk.Entry(update_window)
    country_entry.pack()

    nationality_label = tk.Label(update_window, text="Enter new nationality:")
    nationality_label.pack()

    nationality_entry = tk.Entry(update_window)
    nationality_entry.pack()

    submit_button = tk.Button(update_window, text="Submit", command=lambda: update_selected_passport(
        session,
        selected_passport.get(),
        date_of_birth_entry.get(),
        country_entry.get(),
        nationality_entry.get()))
    submit_button.pack()


def show_update_passenger_form(session, passengers):
    update_window = tk.Toplevel()
    update_window.title("Update Passenger")

    selected_passenger = tk.StringVar()
    selected_passenger.set(passengers[0].passenger_id)

    passenger_label = tk.Label(update_window, text="Select passenger to update:")
    passenger_label.pack()

    passenger_menu = tk.OptionMenu(update_window, selected_passenger,
                                   *[passenger.passenger_id for passenger in passengers])
    passenger_menu.pack()

    pass_number_label = tk.Label(update_window, text="Enter new passport number:")
    pass_number_label.pack()

    pass_number_entry = tk.Entry(update_window)
    pass_number_entry.pack()

    first_name_label = tk.Label(update_window, text="Enter new first name:")
    first_name_label.pack()

    first_name_entry = tk.Entry(update_window)
    first_name_entry.pack()

    second_name_label = tk.Label(update_window, text="Enter new second name:")
    second_name_label.pack()

    second_name_entry = tk.Entry(update_window)
    second_name_entry.pack()

    email_label = tk.Label(update_window, text="Enter new email:")
    email_label.pack()

    email_entry = tk.Entry(update_window)
    email_entry.pack()

    phone_label = tk.Label(update_window, text="Enter new phone number:")
    phone_label.pack()

    phone_entry = tk.Entry(update_window)
    phone_entry.pack()

    gender_label = tk.Label(update_window, text="Enter new gender:")
    gender_label.pack()

    gender_entry = tk.Entry(update_window)
    gender_entry.pack()

    submit_button = tk.Button(update_window, text="Submit", command=lambda: update_selected_passenger(
        session,
        selected_passenger.get(),
        pass_number_entry.get(),
        first_name_entry.get(),
        second_name_entry.get(),
        email_entry.get(),
        phone_entry.get(),
        gender_entry.get()))
    submit_button.pack()

def show_update_bonus_program_form(session, programs):
    update_window = tk.Toplevel()
    update_window.title("Update Bonus Program")

    selected_program = tk.StringVar()
    selected_program.set(programs[0].programm_id)

    program_label = tk.Label(update_window, text="Select program to update:")
    program_label.pack()

    program_menu = tk.OptionMenu(update_window, selected_program,
                                 *[program.programm_id for program in programs])
    program_menu.pack()

    passenger_label = tk.Label(update_window, text="Enter new passenger ID:")
    passenger_label.pack()

    passenger_entry = tk.Entry(update_window)
    passenger_entry.pack()

    reservation_label = tk.Label(update_window, text="Enter new reservation ID:")
    reservation_label.pack()

    reservation_entry = tk.Entry(update_window)
    reservation_entry.pack()

    name_label = tk.Label(update_window, text="Enter new program name:")
    name_label.pack()

    name_entry = tk.Entry(update_window)
    name_entry.pack()

    mileage_label = tk.Label(update_window, text="Enter new mileage value:")
    mileage_label.pack()

    mileage_entry = tk.Entry(update_window)
    mileage_entry.pack()

    relaxzone_label = tk.Label(update_window, text="Enter relax zone (True/False):")
    relaxzone_label.pack()

    relaxzone_entry = tk.Entry(update_window)
    relaxzone_entry.pack()

    submit_button = tk.Button(update_window, text="Submit", command=lambda: update_selected_bonus_program(
        session,
        selected_program.get(),
        passenger_entry.get(),
        reservation_entry.get(),
        name_entry.get(),
        mileage_entry.get(),
        relaxzone_entry.get()))
    submit_button.pack()

def show_update_reservation_form(session, reservations):
    update_window = tk.Toplevel()
    update_window.title("Update Reservation")

    selected_reservation = tk.StringVar()
    selected_reservation.set(reservations[0].reservation_id)

    reservation_label = tk.Label(update_window, text="Select reservation to update:")
    reservation_label.pack()

    reservation_menu = tk.OptionMenu(update_window, selected_reservation,
                                     *[reservation.reservation_id for reservation in reservations])
    reservation_menu.pack()

    ticket_number_label = tk.Label(update_window, text="Enter new ticket number:")
    ticket_number_label.pack()

    ticket_number_entry = tk.Entry(update_window)
    ticket_number_entry.pack()

    reservation_date_label = tk.Label(update_window, text="Enter new reservation date:")
    reservation_date_label.pack()

    reservation_date_entry = tk.Entry(update_window)
    reservation_date_entry.pack()

    submit_button = tk.Button(update_window, text="Submit", command=lambda: update_selected_reservation(
        session,
        selected_reservation.get(),
        ticket_number_entry.get(),
        reservation_date_entry.get()))
    submit_button.pack()

def show_update_ticket_form(session, tickets):
    update_window = tk.Toplevel()
    update_window.title("Update Ticket")

    selected_ticket = tk.StringVar()
    selected_ticket.set(tickets[0].ticket_number)

    ticket_label = tk.Label(update_window, text="Select ticket to update:")
    ticket_label.pack()

    ticket_menu = tk.OptionMenu(update_window, selected_ticket,
                                *[ticket.ticket_number for ticket in tickets])
    ticket_menu.pack()

    flight_id_label = tk.Label(update_window, text="Enter new flight ID:")
    flight_id_label.pack()

    flight_id_entry = tk.Entry(update_window)
    flight_id_entry.pack()

    datepay_label = tk.Label(update_window, text="Enter new payment date:")
    datepay_label.pack()

    datepay_entry = tk.Entry(update_window)
    datepay_entry.pack()

    numplace_label = tk.Label(update_window, text="Enter new seat number:")
    numplace_label.pack()

    numplace_entry = tk.Entry(update_window)
    numplace_entry.pack()

    submit_button = tk.Button(update_window, text="Submit", command=lambda: update_selected_ticket(
        session,
        selected_ticket.get(),
        flight_id_entry.get(),
        datepay_entry.get(),
        numplace_entry.get()))
    submit_button.pack()

def show_update_flight_form(session, flights):
    update_window = tk.Toplevel()
    update_window.title("Update Flight")

    selected_flight = tk.StringVar()
    selected_flight.set(flights[0].flight_id)

    flight_label = tk.Label(update_window, text="Select flight to update:")
    flight_label.pack()

    flight_menu = tk.OptionMenu(update_window, selected_flight, *[flight.flight_id for flight in flights])
    flight_menu.pack()

    departure_airport_label = tk.Label(update_window, text="Enter new departure airport:")
    departure_airport_label.pack()

    departure_airport_entry = tk.Entry(update_window)
    departure_airport_entry.pack()

    arrival_airport_label = tk.Label(update_window, text="Enter new arrival airport:")
    arrival_airport_label.pack()

    arrival_airport_entry = tk.Entry(update_window)
    arrival_airport_entry.pack()

    flight_date_label = tk.Label(update_window, text="Enter new flight date:")
    flight_date_label.pack()

    flight_date_entry = tk.Entry(update_window)
    flight_date_entry.pack()

    plane_num_label = tk.Label(update_window, text="Enter new aircraft number:")
    plane_num_label.pack()

    plane_num_entry = tk.Entry(update_window)
    plane_num_entry.pack()

    flight_status_label = tk.Label(update_window, text="Enter new flight status:")
    flight_status_label.pack()

    flight_status_entry = tk.Entry(update_window)
    flight_status_entry.pack()

    submit_button = tk.Button(update_window, text="Submit", command=lambda: update_selected_flight(
        session,
        selected_flight.get(),
        departure_airport_entry.get(),
        arrival_airport_entry.get(),
        flight_date_entry.get(),
        plane_num_entry.get(),
        flight_status_entry.get()))
    submit_button.pack()

def show_update_airport_form(session, airports):
    update_window = tk.Toplevel()
    update_window.title("Update Airport")

    selected_airport = tk.StringVar()
    selected_airport.set(airports[0].airport_name)

    airport_label = tk.Label(update_window, text="Select airport to update:")
    airport_label.pack()

    airport_menu = tk.OptionMenu(update_window, selected_airport,
                                *[airport.airport_name for airport in airports])
    airport_menu.pack()

    country_label = tk.Label(update_window, text="Enter new country:")
    country_label.pack()

    country_entry = tk.Entry(update_window)
    country_entry.pack()

    city_label = tk.Label(update_window, text="Enter new city:")
    city_label.pack()

    city_entry = tk.Entry(update_window)
    city_entry.pack()

    terminal_label = tk.Label(update_window, text="Enter new terminal:")
    terminal_label.pack()

    terminal_entry = tk.Entry(update_window)
    terminal_entry.pack()

    gate_label = tk.Label(update_window, text="Enter new gate:")
    gate_label.pack()

    gate_entry = tk.Entry(update_window)
    gate_entry.pack()

    submit_button = tk.Button(update_window, text="Submit", command=lambda: update_selected_airport(
        session,
        selected_airport.get(),
        country_entry.get(),
        city_entry.get(),
        terminal_entry.get(),
        gate_entry.get()))
    submit_button.pack()

def show_update_plane_form(session, planes):
    update_window = tk.Toplevel()
    update_window.title("Update Plane")

    selected_plane = tk.StringVar()
    selected_plane.set(planes[0].plane_num)

    plane_label = tk.Label(update_window, text="Select plane to update:")
    plane_label.pack()

    plane_menu = tk.OptionMenu(update_window, selected_plane,
                               *[plane.plane_num for plane in planes])
    plane_menu.pack()

    model_label = tk.Label(update_window, text="Enter new model:")
    model_label.pack()

    model_entry = tk.Entry(update_window)
    model_entry.pack()

    name_label = tk.Label(update_window, text="Enter new name:")
    name_label.pack()

    name_entry = tk.Entry(update_window)
    name_entry.pack()

    factplane_label = tk.Label(update_window, text="Enter new factplane number:")
    factplane_label.pack()

    factplane_entry = tk.Entry(update_window)
    factplane_entry.pack()

    submit_button = tk.Button(update_window, text="Submit", command=lambda: update_selected_plane(
        session,
        selected_plane.get(),
        model_entry.get(),
        name_entry.get(),
        factplane_entry.get()))
    submit_button.pack()
