from datetime import datetime
import tkinter as tk

from tkinter import *
from tkinter import messagebox, ttk

from requests.db_create import *

Session = sessionmaker(bind=engine)
session = Session()


def create_result_window(title, columns, data):
    result_window = tk.Toplevel()
    result_window.title(title)

    tree = ttk.Treeview(result_window, columns=columns)
    for col in columns:
        tree.heading(col, text=col)

    for row in data:
        tree.insert("", "end", values=row)

    tree.pack()


def insert_passport(session, pass_number, date_of_birth, country, nationality):
    passport = Passport(
        pass_number=pass_number,
        date_of_birth=date_of_birth,
        country=country,
        nationality=nationality
    )

    session.add(passport)
    session.commit()
    print("Passport inserted successfully.")


def insert_passenger(session, pass_number, first_name, second_name, email, phone, gender):
    passport = session.query(Passenger).filter_by(pass_number=pass_number).first()

    passenger = Passenger(
        pass_number=pass_number,
        first_name=first_name,
        second_name=second_name,
        email=email,
        phone=phone,
        gender=gender
    )

    session.add(passenger)
    session.commit()
    print("Passenger inserted successfully.")


def insert_bonus_programm(session, passenger_id, reservation_id, name_programm, mil_value, relaxzone):
    passenger = session.query(Passenger).filter_by(passenger_id=passenger_id).first()
    reservation = session.query(Reservation).filter_by(reservation_id=reservation_id).first()

    bonus_programm = BonusProgramm(
        passenger_id=passenger_id,
        reservation_id=reservation_id,
        name_programm=name_programm,
        mil_value=mil_value,
        relaxzone=relaxzone,
        passenger=passenger,
        reservation=reservation
    )
    session.add(bonus_programm)
    session.commit()
    print("Bonus program inserted successfully.")


def insert_reservation(session, ticket_number, reservation_date):
    ticket = session.query(Ticket).filter_by(ticket_number=ticket_number).first()

    if ticket:
        flight_date = ticket.flight.flight_date

        reservation_date = datetime.strptime(reservation_date, "%Y-%m-%d").date()

        if reservation_date < flight_date:
            reservation = Reservation(
                ticket_number=ticket_number,
                reservation_date=reservation_date,
                ticket=ticket
            )
            session.add(reservation)
            session.commit()
            print("Reservation inserted successfully.")
        else:
            print("Error: Invalid reservation date.")
    else:
        print("Error: Ticket not found.")


def insert_ticket(session, flight_id, datepay_ticket, numplace_ticket):
    flight = session.query(Flight).filter_by(flight_id=flight_id).first()

    if flight:
        datepay_ticket = datetime.datetime.strptime(datepay_ticket, "%Y-%m-%d").date()
        if datepay_ticket < flight.flight_date:
            ticket = Ticket(
                flight_id=flight_id,
                datepay_ticket=datepay_ticket,
                numplace_ticket=numplace_ticket,
                flight=flight
            )
            session.add(ticket)
            session.commit()
            print("Ticket inserted successfully.")
        else:
            print("Error: Invalid ticket payment date.")
    else:
        print("Error: Invalid flight_id.")


def insert_flight(session, arrival_airport, departure_airport, plane_num, flight_date, flight_status):
    arrival = session.query(Airport).filter_by(airport_name=arrival_airport).first()
    departure = session.query(Airport).filter_by(airport_name=departure_airport).first()
    plane = session.query(Plane).filter_by(plane_num=plane_num).first()

    if arrival and departure and plane:
        flight = Flight(
            arrival_airport=arrival_airport,
            departure_airport=departure_airport,
            plane_num=plane_num,
            flight_date=flight_date,
            flight_status=flight_status,
            arrival=arrival,
            departure=departure,
            plane=plane
        )
        session.add(flight)
        session.commit()
        print("Flight inserted successfully.")
    else:
        print("Error: Invalid arrival, departure, or plane.")


def insert_airport(session, airport_name, airport_country, city, terminal, gate):
    airport = Airport(
        airport_name=airport_name,
        airport_country=airport_country,
        city=city,
        terminal=terminal,
        gate=gate
    )

    session.add(airport)
    session.commit()
    print("Airport inserted successfully.")


def insert_plane(session, plane_num, model_plane, name_plane, factplane_num):
    plane = Plane(
        plane_num=plane_num,
        model_plane=model_plane,
        name_plane=name_plane,
        factplane_num=factplane_num
    )

    session.add(plane)
    session.commit()
    print("Plane inserted successfully.")


def delete_passport(pass_number, delete_window):
    passport = session.query(Passport).filter_by(pass_number=pass_number).first()
    if passport:
        session.delete(passport)
        session.commit()
        print("Passport deleted successfully.")
    else:
        print("Passport not found.")
    delete_window.destroy()


def delete_passenger(passenger_id, delete_window):
    passenger = session.query(Passenger).filter_by(passenger_id=passenger_id).first()
    if passenger:
        session.delete(passenger)
        session.commit()
        print("Passenger deleted successfully.")
    else:
        print("Passenger not found.")
    delete_window.destroy()


def delete_bonus_programm(programm_id, delete_window):
    bonus_programm = session.query(BonusProgramm).filter_by(programm_id=programm_id).first()
    if bonus_programm:
        session.delete(bonus_programm)
        session.commit()
        print("Bonus program deleted successfully.")
    else:
        print("Bonus program not found.")
    delete_window.destroy()


def delete_reservation(reservation_id, delete_window):
    reservation = session.query(Reservation).filter_by(reservation_id=reservation_id).first()
    if reservation:
        session.delete(reservation)
        session.commit()
        print("Reservation deleted successfully.")
    else:
        print("Reservation not found.")
    delete_window.destroy()


def delete_ticket(ticket_number, delete_window):
    ticket = session.query(Ticket).filter_by(ticket_number=ticket_number).first()
    if ticket:
        session.delete(ticket)
        session.commit()
        print("Ticket deleted successfully.")
    else:
        print("Ticket not found.")
    delete_window.destroy()


def delete_flight(flight_id, delete_window):
    flight = session.query(Flight).filter_by(flight_id=flight_id).first()
    if flight:
        session.delete(flight)
        session.commit()
        print("Flight deleted successfully.")
    else:
        print("Flight not found.")
    delete_window.destroy()


def delete_airport(airport_name, delete_window):
    airport = session.query(Airport).filter_by(airport_name=airport_name).first()
    if airport:
        session.delete(airport)
        session.commit()
        print("Airport deleted successfully.")
    else:
        print("Airport not found.")
    delete_window.destroy()


def delete_plane(plane_num, delete_window):
    plane = session.query(Plane).filter_by(plane_num=plane_num).first()
    if plane:
        session.delete(plane)
        session.commit()
        print("Plane deleted successfully.")
    else:
        print("Plane not found.")
    delete_window.destroy()


def select_passport(session, pass_number, date_of_birth, country, nationality):
    query = session.query(Passport)

    if pass_number:
        query = query.filter(func.CAST(Passport.pass_number, String).like(f"%{pass_number}%"))

    if date_of_birth:
        query = query.filter(or_(Passport.date_of_birth == date_of_birth, Passport.date_of_birth.is_(None)))

    if country:
        query = query.filter(or_(Passport.country == country, Passport.country.is_(None)))

    if nationality:
        query = query.filter(or_(Passport.nationality == nationality, Passport.nationality.is_(None)))

    passports = query.all()

    if passports:
        data = [(passport.pass_number, passport.date_of_birth, passport.country, passport.nationality) for passport in
                passports]
        create_result_window("Passport Search Results", ["Passport Number", "Date of Birth", "Country", "Nationality"],
                             data)
    else:
        messagebox.showinfo("No Passport Found", "No passport found")


def select_passenger(session, passenger_id, pass_number, first_name, second_name, email, phone, gender):
    query = session.query(Passenger)

    if passenger_id:
        query = query.filter(func.cast(Passenger.passenger_id, String).like(f'%{passenger_id}%'))
    if pass_number:
        query = query.filter(func.cast(Passenger.pass_number, String).like(f'%{pass_number}%'))
    if first_name:
        query = query.filter(func.cast(Passenger.first_name, String).like(f'%{first_name}%'))
    if second_name:
        query = query.filter(func.cast(Passenger.second_name, String).like(f'%{second_name}%'))
    if email:
        query = query.filter(func.cast(Passenger.email, String).like(f'%{email}%'))
    if phone:
        query = query.filter(func.cast(Passenger.phone, String).like(f'%{phone}%'))
    if gender:
        query = query.filter(func.cast(Passenger.gender, String).like(f'%{gender}%'))

    passengers = query.all()

    if passengers:
        data = [(passenger.passenger_id, passenger.pass_number, passenger.first_name, passenger.second_name,
                 passenger.email, passenger.phone, passenger.gender) for passenger in passengers]
        create_result_window("Passenger Search Results",
                             ["Passenger ID", "Passport ID", "First Name", "Second Name", "Email", "Phone", "Gender"],
                             data)
    else:
        messagebox.showinfo("Passengers not found", "Passengers not found.")


def select_bonus_programm(session, programm_id, passenger_id, reservation_id, name_programm, mil_value, relaxzone):
    query = session.query(BonusProgramm)

    if programm_id:
        query = query.filter(func.cast(BonusProgramm.programm_id, String).like(f'%{programm_id}%'))

    if passenger_id:
        query = query.filter(func.cast(BonusProgramm.passenger_id, String).like(f'%{passenger_id}%'))

    if reservation_id:
        query = query.filter(func.cast(BonusProgramm.reservation_id, String).like(f'%{reservation_id}%'))

    if name_programm:
        query = query.filter(func.cast(BonusProgramm.name_programm, String).like(f'%{name_programm}%'))

    if mil_value:
        query = query.filter(func.cast(BonusProgramm.mil_value, String).like(f'%{mil_value}%'))

    if relaxzone:
        query = query.filter(func.cast(BonusProgramm.relaxzone, String).like(f'%{relaxzone}%'))

    bonus_programs = query.all()

    if bonus_programs:
        data = [(program.programm_id, program.passenger_id, program.reservation_id, program.name_programm,
                 program.mil_value, program.relaxzone) for program in bonus_programs]
        create_result_window("Bonus Program Search Results",
                             ["Program ID", "Passenger ID", "Reservation ID", "Program Name", "Mile Value",
                              "Relaxzone"], data)
    else:
        messagebox.showinfo("No Bonus Programs Found", "No bonus programs found")


def select_reservation(session, reservation_id, ticket_number, reservation_date):
    query = session.query(Reservation)

    if reservation_id:
        query = query.filter(func.cast(Reservation.reservation_id, String).like(f'%{reservation_id}%'))

    if ticket_number:
        query = query.filter(func.cast(Reservation.ticket_number, String).like(f'%{ticket_number}%'))

    if reservation_date:
        query = query.filter(func.cast(Reservation.reservation_date, String).like(f'%{reservation_date}%'))

    reservations = query.all()

    if reservations:
        data = [(reservation.reservation_id, reservation.ticket_number, reservation.reservation_date) for reservation in
                reservations]
        create_result_window("Reservation Search Results", ["Reservation ID", "Ticket Number", "Reservation Date"],
                             data)
    else:
        messagebox.showinfo("No Reservation Found", "No reservation found")


def select_ticket(session, ticket_number, flight_id, datepay_ticket, numplace_ticket):
    query = session.query(Ticket)

    if ticket_number:
        query = query.filter(func.cast(Ticket.ticket_number, String).like(f'%{ticket_number}%'))
    if flight_id:
        query = query.filter(func.cast(Ticket.flight_id, String).like(f'%{flight_id}%'))
    if datepay_ticket:
        query = query.filter(func.cast(Ticket.datepay_ticket, String).like(f'%{datepay_ticket}%'))
    if numplace_ticket:
        query = query.filter(func.cast(Ticket.numplace_ticket, String).like(f'%{numplace_ticket}%'))

    tickets = query.all()

    if tickets:
        data = [(ticket.ticket_number, ticket.flight_id, ticket.datepay_ticket, ticket.numplace_ticket) for ticket in
                tickets]
        create_result_window("Ticket Search Results", ["Ticket Number", "Flight ID", "Payment Date", "Seat Number"],
                             data)
    else:
        messagebox.showinfo("No Tickets Found", "No tickets found")


def select_flight(session, flight_id, departure_airport, arrival_airport, flight_date, plane_num, flight_status):
    query = session.query(Flight)

    if flight_id:
        query = query.filter(func.cast(Flight.flight_id, String).like(f'%{flight_id}%'))
    if departure_airport:
        query = query.filter(func.cast(Flight.departure_airport, String).like(f'%{departure_airport}%'))
    if arrival_airport:
        query = query.filter(func.cast(Flight.destination_airport, String).like(f'%{arrival_airport}%'))
    if flight_date:
        query = query.filter(func.cast(Flight.flight_date, String).like(f'%{flight_date}%'))
    if plane_num:
        query = query.filter(func.cast(Flight.plane_num, String).like(f'%{plane_num}'))
    if flight_status:
        query = query.filter(func.cast(Flight.flight_status, String).like(f'%{flight_status}'))

    flights = query.all()

    if flights:
        data = [(flight.flight_id, flight.departure_airport, flight.arrival_airport, flight.plane_num,
                 flight.flight_date, flight.flight_status) for flight in flights]
        create_result_window("Flight Search Results",
                             ["Flight ID", "Departure Airport", "Arrival Airport", "Aircraft Number", "Flight Date",
                              "Flight Status"], data)
    else:
        messagebox.showinfo("No flight Found", "No flight found")


def select_airport(session, airport_name, airport_country, city, terminal, gate):
    query = session.query(Airport)

    if airport_name:
        query = query.filter(func.cast(Airport.airport_name, String).like(f'%{airport_name}%'))
    if airport_country:
        query = query.filter(func.cast(Airport.airport_country, String).like(f'%{airport_country}%'))
    if city:
        query = query.filter(func.cast(Airport.city, String).like(f'%{city}%'))
    if terminal:
        query = query.filter(func.cast(Airport.terminal, String).like(f'%{terminal}%'))
    if gate:
        query = query.filter(func.cast(Airport.gate, String).like(f'%{gate}%'))

    airports = query.all()

    if airports:
        result_window = tk.Toplevel()
        result_window.title("Search Results")

        # Create a treeview table
        tree = ttk.Treeview(result_window, columns=("airport_name", "airport_country", "city", "terminal", "gate"))
        tree.heading("airport_name", text="Airport Name")
        tree.heading("airport_country", text="Airport Country")
        tree.heading("city", text="City")
        tree.heading("terminal", text="Terminal")
        tree.heading("gate", text="Gate")

        for airport in airports:
            tree.insert("", "end", values=(
                airport.airport_name, airport.airport_country, airport.city, airport.terminal, airport.gate))

        tree.pack()
    else:
        messagebox.showinfo("No Airport Found", "No airport found")


def select_plane(session, plane_num, model_plane, name_plane, factplane_num):
    query = session.query(Plane)

    if plane_num:
        query = query.filter(func.cast(Plane.plane_num, String).like(f'%{plane_num}%'))
    if model_plane:
        query = query.filter(func.cast(Plane.model_plane, String).like(f'%{model_plane}%'))
    if name_plane:
        query = query.filter(func.cast(Plane.name_plane, String).like(f'%{name_plane}%'))
    if factplane_num:
        query = query.filter(func.cast(Plane.factplane_num, String).like(f'%{factplane_num}%'))

    planes = query.all()

    if planes:
        result_window = tk.Toplevel()
        result_window.title("Search Result")

        treeview = ttk.Treeview(result_window)

        treeview["columns"] = ("Aircraft Number", "Airplane Model", "Aircraft Name", "Serial Number")

        treeview.heading("Aircraft Number", text="Aircraft Number")
        treeview.heading("Airplane Model", text="Airplane Model")
        treeview.heading("Aircraft Name", text="Aircraft Name")
        treeview.heading("Serial Number", text="Serial Number")

        for plane in planes:
            treeview.insert("", tk.END,
                            values=(plane.plane_num, plane.model_plane, plane.name_plane, plane.factplane_num))

        treeview.pack()
    else:
        result_window = tk.Toplevel()
        result_window.title("Search Result")

        no_results_label = tk.Label(result_window, text="Aircraft not found.")
        no_results_label.pack()


def update_selected_passport(session, pass_number, date_of_birth, country, nationality):
    selected_passport = session.query(Passport).filter(Passport.pass_number == pass_number).first()

    if selected_passport:
        if date_of_birth:
            selected_passport.date_of_birth = date_of_birth
        if country:
            selected_passport.country = country
        if nationality:
            selected_passport.nationality = nationality

        session.commit()

        print("Passport updated successfully.")
    else:
        print("Passport not found.")


def update_selected_passenger(session, passenger_id, pass_number, first_name, second_name, email, phone, gender):
    selected_passenger = session.query(Passenger).filter(Passenger.passenger_id == passenger_id).first()

    if selected_passenger:
        if pass_number:
            selected_passenger.pass_number = pass_number
        if first_name:
            selected_passenger.first_name = first_name
        if second_name:
            selected_passenger.second_name = second_name
        if email:
            selected_passenger.email = email
        if phone:
            selected_passenger.phone = phone
        if gender:
            selected_passenger.gender = gender

        session.commit()

        print("Passenger updated successfully.")
    else:
        print("Passenger not found.")


def update_selected_bonus_program(session, program_id, passenger_id, reservation_id, name_programm, mil_value, relaxzone):
    selected_program = session.query(BonusProgramm).filter(BonusProgramm.programm_id == program_id).first()

    if selected_program:
        if passenger_id:
            selected_program.passenger_id = passenger_id
        if reservation_id:
            selected_program.reservation_id = reservation_id
        if name_programm:
            selected_program.name_programm = name_programm
        if mil_value:
            selected_program.mil_value = mil_value
        if relaxzone:
            selected_program.relaxzone = bool(relaxzone)

        session.commit()

        print("Bonus program updated successfully.")
    else:
        print("Bonus program not found.")

def update_selected_reservation(session, reservation_id, ticket_number, reservation_date):
    selected_reservation = session.query(Reservation).filter(Reservation.reservation_id == reservation_id).first()

    if selected_reservation:
        if ticket_number:
            selected_reservation.ticket_number = ticket_number
        if reservation_date:
            selected_reservation.reservation_date = reservation_date

        session.commit()

        print("Reservation updated successfully.")
    else:
        print("Reservation not found.")

def update_selected_ticket(session, ticket_number, flight_id, datepay_ticket, numplace_ticket):
    selected_ticket = session.query(Ticket).filter(Ticket.ticket_number == ticket_number).first()

    if selected_ticket:
        if flight_id:
            selected_ticket.flight_id = flight_id
        if datepay_ticket:
            selected_ticket.datepay_ticket = datepay_ticket
        if numplace_ticket:
            selected_ticket.numplace_ticket = numplace_ticket

        session.commit()

        print("Ticket updated successfully.")
    else:
        print("Ticket not found.")

def update_selected_flight(session, flight_id, departure_airport, arrival_airport, flight_date, plane_num, flight_status):
    selected_flight = session.query(Flight).filter(Flight.flight_id == flight_id).first()

    if selected_flight:
        if departure_airport:
            selected_flight.departure_airport = departure_airport
        if arrival_airport:
            selected_flight.arrival_airport = arrival_airport
        if flight_date:
            selected_flight.flight_date = flight_date
        if plane_num:
            selected_flight.plane_num = plane_num
        if flight_status:
            selected_flight.flight_status = flight_status

        session.commit()

        print("Flight updated successfully.")
    else:
        print("Flight not found.")

def update_selected_airport(session, airport_name, airport_country, city, terminal, gate):
    selected_airport = session.query(Airport).filter(Airport.airport_name == airport_name).first()

    if selected_airport:
        if airport_country:
            selected_airport.airport_country = airport_country
        if city:
            selected_airport.city = city
        if terminal:
            selected_airport.terminal = terminal
        if gate:
            selected_airport.gate = gate

        session.commit()

        print("Airport updated successfully.")
    else:
        print("Airport not found.")

def update_selected_plane(session, plane_num, model_plane, name_plane, factplane_num):
    selected_plane = session.query(Plane).filter(Plane.plane_num == plane_num).first()

    if selected_plane:
        if model_plane:
            selected_plane.model_plane = model_plane
        if name_plane:
            selected_plane.name_plane = name_plane
        if factplane_num:
            selected_plane.factplane_num = factplane_num

        session.commit()

        print("Plane updated successfully.")
    else:
        print("Plane not found.")