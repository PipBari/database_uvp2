import tk

from requests.select_updates import *


def select_passport_to_update_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Passport to Update")

    passport_label = tk.Label(select_window, text="Enter passport number:")
    passport_label.pack()

    passport_entry = tk.Entry(select_window)
    passport_entry.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_passport_to_update(
        session,
        passport_entry.get()))
    submit_button.pack()

def select_passenger_to_update_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Passenger to Update")

    passenger_label = tk.Label(select_window, text="Enter passenger ID:")
    passenger_label.pack()

    passenger_entry = tk.Entry(select_window)
    passenger_entry.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_passenger_to_update(
        session,
        passenger_entry.get()))
    submit_button.pack()

def select_bonus_program_to_update_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Bonus Program to Update")

    program_label = tk.Label(select_window, text="Enter program ID:")
    program_label.pack()

    program_entry = tk.Entry(select_window)
    program_entry.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_bonus_program_to_update(
        session,
        program_entry.get()))
    submit_button.pack()

def select_reservation_to_update_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Reservation to Update")

    reservation_label = tk.Label(select_window, text="Enter reservation ID:")
    reservation_label.pack()

    reservation_entry = tk.Entry(select_window)
    reservation_entry.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_reservation_to_update(
        session,
        reservation_entry.get()))
    submit_button.pack()

def select_ticket_to_update_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Ticket to Update")

    ticket_label = tk.Label(select_window, text="Enter ticket number:")
    ticket_label.pack()

    ticket_entry = tk.Entry(select_window)
    ticket_entry.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_ticket_to_update(
        session,
        ticket_entry.get()))
    submit_button.pack()

def select_flight_to_update_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Flight to Update")

    flight_id_label = tk.Label(select_window, text="Enter flight ID:")
    flight_id_label.pack()

    flight_id_entry = tk.Entry(select_window)
    flight_id_entry.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_flight_to_update(
        session,
        flight_id_entry.get()))
    submit_button.pack()

def select_airport_to_update_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Airport to Update")

    airport_label = tk.Label(select_window, text="Enter airport code:")
    airport_label.pack()

    airport_entry = tk.Entry(select_window)
    airport_entry.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_airport_to_update(
        session,
        airport_entry.get()))
    submit_button.pack()


def select_plane_to_update_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Plane to Update")

    plane_label = tk.Label(select_window, text="Enter plane number:")
    plane_label.pack()

    plane_entry = tk.Entry(select_window)
    plane_entry.pack()

    submit_button = tk.Button(select_window, text="Submit", command=lambda: select_plane_to_update(
        session,
        plane_entry.get()))
    submit_button.pack()