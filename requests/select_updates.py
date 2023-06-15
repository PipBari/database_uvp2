from sqlalchemy import func

from requests.db_create import *
from requests.menu_selects import *
from requests.sql_requests import create_result_window


def select_passport_to_update(session, pass_number):
    query = session.query(Passport)

    if pass_number:
        query = query.filter(func.CAST(Passport.pass_number, String).like(f"%{pass_number}%"))

    passports = query.all()

    if passports:
        data = [(passport.pass_number, passport.date_of_birth, passport.country, passport.nationality) for passport in passports]
        create_result_window("Passport Search Results", ["Passport Number", "Date of Birth", "Country", "Nationality"], data)
        show_update_passport_form(session, passports)
    else:
        print("Passport not found.")


def select_passenger_to_update(session, passenger_id):
    query = session.query(Passenger)

    if passenger_id:
        query = query.filter(Passenger.passenger_id == passenger_id)

    passengers = query.all()

    if passengers:
        data = [(passenger.passenger_id, passenger.pass_number, passenger.first_name, passenger.second_name,
                 passenger.email, passenger.phone, passenger.gender) for passenger in passengers]
        create_result_window("Passenger Search Results", ["Passenger ID", "Passport Number", "First Name", "Last Name",
                                                           "Email", "Phone", "Gender"], data)
        show_update_passenger_form(session, passengers)
    else:
        print("Passenger not found.")

def select_bonus_program_to_update(session, program_id):
    query = session.query(BonusProgramm)

    if program_id:
        query = query.filter(BonusProgramm.programm_id == program_id)

    programs = query.all()

    if programs:
        data = [(program.programm_id, program.passenger_id, program.reservation_id, program.name_programm,
                 program.mil_value, program.relaxzone) for program in programs]
        create_result_window("Bonus Program Search Results", ["Program ID", "Passenger ID", "Reservation ID", "Program Name",
                                                               "Mileage Value", "Relax Zone"], data)
        show_update_bonus_program_form(session, programs)
    else:
        print("Bonus program not found.")

def select_reservation_to_update(session, reservation_id):
    query = session.query(Reservation)

    if reservation_id:
        query = query.filter(Reservation.reservation_id == reservation_id)

    reservations = query.all()

    if reservations:
        data = [(reservation.reservation_id, reservation.ticket_number, reservation.reservation_date) for reservation in reservations]
        create_result_window("Reservation Search Results", ["Reservation ID", "Ticket Number", "Reservation Date"], data)
        show_update_reservation_form(session, reservations)
    else:
        print("Reservation not found.")

def select_ticket_to_update(session, ticket_number):
    query = session.query(Ticket)

    if ticket_number:
        query = query.filter(Ticket.ticket_number == ticket_number)

    tickets = query.all()

    if tickets:
        data = [(ticket.ticket_number, ticket.flight_id, ticket.datepay_ticket, ticket.numplace_ticket) for ticket in tickets]
        create_result_window("Ticket Search Results", ["Ticket Number", "Flight ID", "Payment Date", "Seat Number"], data)
        show_update_ticket_form(session, tickets)
    else:
        print("Ticket not found.")

def select_flight_to_update(session, flight_id):
    query = session.query(Flight)

    if flight_id:
        query = query.filter(Flight.flight_id == flight_id)

    flights = query.all()

    if flights:
        data = [(flight.flight_id, flight.departure_airport, flight.arrival_airport, flight.flight_date, flight.plane_num, flight.flight_status) for flight in flights]
        create_result_window("Flight Search Results",
                             ["Flight ID", "Departure Airport", "Arrival Airport", "Flight Date", "Aircraft Number", "Flight Status"], data)
        show_update_flight_form(session, flights)
    else:
        print("Flight not found.")

def select_airport_to_update(session, airport_name):
    query = session.query(Airport)

    if airport_name:
        query = query.filter(Airport.airport_name == airport_name)

    airports = query.all()

    if airports:
        data = [(airport.airport_name, airport.airport_country, airport.city, airport.terminal, airport.gate) for airport in airports]
        create_result_window("Airport Search Results", ["Airport Name", "Country", "City", "Terminal", "Gate"], data)
        show_update_airport_form(session, airports)
    else:
        print("Airport not found.")

def select_plane_to_update(session, plane_num):
    query = session.query(Plane)

    if plane_num:
        query = query.filter(Plane.plane_num == plane_num)

    planes = query.all()

    if planes:
        data = [(plane.plane_num, plane.model_plane, plane.name_plane, plane.factplane_num) for plane in planes]
        create_result_window("Plane Search Results", ["Plane Number", "Model", "Name", "Factplane Number"], data)
        show_update_plane_form(session, planes)
    else:
        print("Plane not found.")