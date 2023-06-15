from requests.menu_selects import *
from requests.select_updates import select_passport_to_update
from requests.sql_requests import *
import tkinter as tk

from requests.update_menu import *


def main_menu():
    main_window = tk.Tk()
    main_window.iconbitmap("logo.ico")
    main_window.title("Reservation Menu")
    main_window.geometry("500x300")
    bg_image = tk.PhotoImage(file="logo.png")

    background_label = tk.Label(main_window, image=bg_image)
    background_label.place(x=80, y=0, relwidth=1, relheight=1)

    operation_label = tk.Label(main_window, text="Select operation:", font=("Arial", 12, "bold"))
    operation_label.pack(anchor='w', padx=10, pady=10)

    insert_button = tk.Button(main_window, text="Insert Data", command=insert_menu, font=("Arial", 12), relief="solid",
                              borderwidth=1)
    insert_button.pack(anchor='w', padx=10, pady=10)

    delete_button = tk.Button(main_window, text="Delete Data", command=delete_menu, font=("Arial", 12), relief="solid",
                              borderwidth=1)
    delete_button.pack(anchor='w', padx=10, pady=10)

    select_button = tk.Button(main_window, text="Select Tables Data", command=select_data_menu, font=("Arial", 12),
                              relief="solid", borderwidth=1)
    select_button.pack(anchor='w', padx=10, pady=10)

    update_button = tk.Button(main_window, text="Update Tables Data", command=update_data_menu, font=("Arial", 12),
                              relief="solid", borderwidth=1)
    update_button.pack(anchor='w', padx=10, pady=10)

    exit_button = tk.Button(main_window, text="Exit", command=main_window.quit, font=("Arial", 12), relief="solid",
                            borderwidth=1)
    exit_button.pack(anchor='w', padx=10, pady=10)

    main_window.mainloop()


def insert_menu():
    insert_window = tk.Toplevel()
    insert_window.title("Insert Menu")
    insert_window.geometry("200x420")

    table_label = tk.Label(insert_window, text="Select table to insert into:")
    table_label.pack()

    button_style = {
        "font": ("Arial", 12),
        "relief": "solid",
        "borderwidth": 1,
        "highlightthickness": 0,
        "highlightbackground": "white"
    }

    passport_button = tk.Button(insert_window, text="Passport", command=insert_passport_menu, **button_style)
    passport_button.pack()
    passport_button.pack(pady=10)

    passenger_button = tk.Button(insert_window, text="Passenger", command=insert_passenger_menu, **button_style)
    passenger_button.pack()
    passenger_button.pack(pady=10)

    bonus_button = tk.Button(insert_window, text="BonusProgramm", command=insert_bonus_programm_menu, **button_style)
    bonus_button.pack()
    bonus_button.pack(pady=10)

    reservation_button = tk.Button(insert_window, text="Reservation", command=insert_reservation_menu, **button_style)
    reservation_button.pack()
    reservation_button.pack(pady=10)

    ticket_button = tk.Button(insert_window, text="Ticket", command=insert_ticket_menu, **button_style)
    ticket_button.pack()
    ticket_button.pack(pady=10)

    flight_button = tk.Button(insert_window, text="Flight", command=insert_flight_menu, **button_style)
    flight_button.pack()
    flight_button.pack(pady=10)

    airport_button = tk.Button(insert_window, text="Airport", command=insert_airport_menu, **button_style)
    airport_button.pack()
    airport_button.pack(pady=10)

    plane_button = tk.Button(insert_window, text="Plane", command=insert_plane_menu, **button_style)
    plane_button.pack()
    plane_button.pack(pady=10)


def delete_menu():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Menu")
    delete_window.geometry("200x420")

    table_label = tk.Label(delete_window, text="Select table to delete from:")
    table_label.pack()

    button_style = {
        "font": ("Arial", 12),
        "relief": "solid",
        "borderwidth": 1,
        "highlightthickness": 0,
        "highlightbackground": "white"
    }

    passport_button = tk.Button(delete_window, text="Passport", command=delete_passport_menu, **button_style)
    passport_button.pack()
    passport_button.pack(pady=10)

    passenger_button = tk.Button(delete_window, text="Passenger", command=delete_passenger_menu, **button_style)
    passenger_button.pack()
    passenger_button.pack(pady=10)

    bonus_button = tk.Button(delete_window, text="BonusProgramm", command=delete_bonus_programm_menu, **button_style)
    bonus_button.pack()
    bonus_button.pack(pady=10)

    reservation_button = tk.Button(delete_window, text="Reservation", command=delete_reservation_menu, **button_style)
    reservation_button.pack()
    reservation_button.pack(pady=10)

    ticket_button = tk.Button(delete_window, text="Ticket", command=delete_ticket_menu, **button_style)
    ticket_button.pack()
    ticket_button.pack(pady=10)

    flight_button = tk.Button(delete_window, text="Flight", command=delete_flight_menu, **button_style)
    flight_button.pack()
    flight_button.pack(pady=10)

    airport_button = tk.Button(delete_window, text="Airport", command=delete_airport_menu, **button_style)
    airport_button.pack()
    airport_button.pack(pady=10)

    plane_button = tk.Button(delete_window, text="Plane", command=delete_plane_menu, **button_style)
    plane_button.pack()
    plane_button.pack(pady=10)


def select_data_menu():
    select_window = tk.Toplevel()
    select_window.title("Select Data Menu")
    select_window.geometry("200x420")

    table_label = tk.Label(select_window, text="Select tables to select from:")
    table_label.pack()

    button_style = {
        "font": ("Arial", 12),
        "relief": "solid",
        "borderwidth": 1,
        "highlightthickness": 0,
        "highlightbackground": "white"
    }

    passport_button = tk.Button(select_window, text="Passport", command=select_passport_menu, **button_style)
    passport_button.pack()
    passport_button.pack(pady=10)

    passenger_button = tk.Button(select_window, text="Passenger", command=select_passenger_menu, **button_style)
    passenger_button.pack()
    passenger_button.pack(pady=10)

    bonus_button = tk.Button(select_window, text="BonusProgramm", command=select_bonus_programm_menu, **button_style)
    bonus_button.pack()
    bonus_button.pack(pady=10)

    reservation_button = tk.Button(select_window, text="Reservation", command=select_reservation_menu, **button_style)
    reservation_button.pack()
    reservation_button.pack(pady=10)

    ticket_button = tk.Button(select_window, text="Ticket", command=select_ticket_menu, **button_style)
    ticket_button.pack()
    ticket_button.pack(pady=10)

    flight_button = tk.Button(select_window, text="Flight", command=select_flight_menu, **button_style)
    flight_button.pack()
    flight_button.pack(pady=10)

    airport_button = tk.Button(select_window, text="Airport", command=select_airport_menu, **button_style)
    airport_button.pack()
    airport_button.pack(pady=10)

    plane_button = tk.Button(select_window, text="Plane", command=select_plane_menu, **button_style)
    plane_button.pack()
    plane_button.pack(pady=10)


def update_data_menu():
    select_window = tk.Toplevel()
    select_window.title("Update Data Menu")
    select_window.geometry("200x420")

    table_label = tk.Label(select_window, text="Select tables to update from:")
    table_label.pack()

    button_style = {
        "font": ("Arial", 12),
        "relief": "solid",
        "borderwidth": 1,
        "highlightthickness": 0,
        "highlightbackground": "white"
    }

    passport_button = tk.Button(select_window, text="Passport", command=select_passport_to_update_menu, **button_style)
    passport_button.pack()
    passport_button.pack(pady=10)

    passport_button = tk.Button(select_window, text="Passenger", command=select_passenger_to_update_menu,
                                **button_style)
    passport_button.pack()
    passport_button.pack(pady=10)

    bonus_button = tk.Button(select_window, text="Bonus Program", command=select_bonus_program_to_update_menu,
                             **button_style)
    bonus_button.pack()
    bonus_button.pack(pady=10)

    reservation_button = tk.Button(select_window, text="Reservation", command=select_reservation_to_update_menu, **button_style)
    reservation_button.pack()
    reservation_button.pack(pady=10)

    ticket_button = tk.Button(select_window, text="Ticket", command=select_ticket_to_update_menu, **button_style)
    ticket_button.pack()
    ticket_button.pack(pady=10)

    flight_button = tk.Button(select_window, text="Flight", command=select_flight_to_update_menu, **button_style)
    flight_button.pack()
    flight_button.pack(pady=10)

    airport_button = tk.Button(select_window, text="Airport", command=select_airport_to_update_menu, **button_style)
    airport_button.pack()
    airport_button.pack(pady=10)

    plane_button = tk.Button(select_window, text="Plane", command=select_plane_to_update_menu, **button_style)
    plane_button.pack()
    plane_button.pack(pady=10)


if __name__ == '__main__':
    main_menu()
