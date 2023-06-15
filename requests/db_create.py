from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from unicodedata import numeric
import tkinter as tk

from configs.config import engine

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Passport(Base):
    __tablename__ = 'passport'

    pass_number = Column(BIGINT, primary_key=True)
    date_of_birth = Column(Date, nullable=False)
    country = Column(String, nullable=False)
    nationality = Column(String, nullable=False)


class Passenger(Base):
    __tablename__ = 'passenger'

    passenger_id = Column(Integer, primary_key=True, autoincrement=True)
    pass_number = Column(BIGINT, ForeignKey('passport.pass_number', ondelete='CASCADE'), nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(Numeric, nullable=False, unique=True)
    gender = Column(String, nullable=False)
    passport = relationship('Passport')


class BonusProgramm(Base):
    __tablename__ = 'bonus_programm'

    programm_id = Column(Integer, primary_key=True, autoincrement=True)
    passenger_id = Column(Integer, ForeignKey('passenger.passenger_id', ondelete='CASCADE'), nullable=False)
    reservation_id = Column(Integer, ForeignKey('reservation.reservation_id', ondelete='CASCADE'), nullable=False)
    name_programm = Column(String, nullable=False)
    mil_value = Column(Numeric, nullable=False)
    relaxzone = Column(Boolean, nullable=False)
    passenger = relationship('Passenger')
    reservation = relationship('Reservation')


class Reservation(Base):
    __tablename__ = 'reservation'

    reservation_id = Column(Integer, primary_key=True, autoincrement=True)
    ticket_number = Column(Integer, ForeignKey('ticket.ticket_number', ondelete='CASCADE'), nullable=False)
    reservation_date = Column(Date, nullable=False)
    ticket = relationship('Ticket')


class Ticket(Base):
    __tablename__ = 'ticket'

    ticket_number = Column(Integer, primary_key=True, autoincrement=True)
    flight_id = Column(Integer, ForeignKey('flight.flight_id', ondelete='CASCADE'), nullable=False)
    datepay_ticket = Column(Date, nullable=False)
    numplace_ticket = Column(String, nullable=False)
    flight = relationship('Flight')


class Flight(Base):
    __tablename__ = 'flight'

    flight_id = Column(Integer, primary_key=True, autoincrement=True)
    arrival_airport = Column(String, ForeignKey('airports.airport_name', ondelete='CASCADE'), nullable=False)
    departure_airport = Column(String, ForeignKey('airports.airport_name', ondelete='CASCADE'), nullable=False)
    plane_num = Column(String, ForeignKey('plane.plane_num', ondelete='CASCADE'), nullable=False)
    flight_date = Column(Date, nullable=False)
    flight_status = Column(Boolean, nullable=False)
    arrival = relationship('Airport', foreign_keys=[arrival_airport])
    departure = relationship('Airport', foreign_keys=[departure_airport])
    plane = relationship('Plane')


class Airport(Base):
    __tablename__ = 'airports'

    airport_name = Column(String, primary_key=True)
    airport_country = Column(String, nullable=False)
    city = Column(String, nullable=False)
    terminal = Column(String, nullable=False)
    gate = Column(String, nullable=False)


class Plane(Base):
    __tablename__ = 'plane'

    plane_num = Column(String, primary_key=True)
    model_plane = Column(String, nullable=False)
    name_plane = Column(String, nullable=False)
    factplane_num = Column(String, nullable=False)


Base.metadata.create_all(engine)
