# coding: utf-8

# @Time    : 2018/2/23 20:02
# @Author  : wangmuy
# @Contact : wangmuy@gmail.com
# @Desc    :

from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Album(Base):
    __tablename__ = 'Album'

    AlbumId = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String, nullable=False)
    ArtistId = Column(Integer, ForeignKey('Artist.ArtistId'), nullable=False)

    def __init__(self, title='', artistId=0):
        self.Title = title
        self.ArtistId = artistId

    def __repr__(self):
        return '<Album %r, status=%d>' % (self.Title, self.ArtistId)

    @classmethod
    def query(cls, session):
        return session.query(cls)


class Artist(Base):
    __tablename__ = 'Artist'

    ArtistId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)

    def __init__(self, name):
        self.Name = name

    def __repr__(self):
        return '<Artist %r, id=%d>' % (self.Name, self.ArtistId)

    @classmethod
    def query(cls, session):
        return session.query(cls)


class Customer(Base):
    __tablename__ = 'Customer'

    CustomerId = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    Company = Column(String)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String, nullable=False)
    SupportRepId = Column(Integer, ForeignKey('Employee.EmployeeId'))

    def __init__(self, firstName='', lastName='', email=''):
        self.FirstName = firstName
        self.LastName = lastName
        self.Email = email

    def __repr__(self):
        return '<Customer %r %r %r, id=%d>' % (self.FirstName, self.LastName, self.Email, self.CustomerId)

    @classmethod
    def query(cls, session):
        return session.query(cls)


class Employee(Base):
    __tablename__ = 'Employee'

    EmployeeId = Column(Integer, primary_key=True, autoincrement=True)
    LastName = Column(String, nullable=False)
    FirstName = Column(String, nullable=False)
    Title = Column(String)
    ReportsTo = Column(Integer, ForeignKey('Employee.EmployeeId'))
    BirthDate = Column(DateTime)
    HireDate = Column(DateTime)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)

    def __init__(self, firstName, lastName):
        self.FirstName = firstName
        self.LastName = lastName

    def __repr__(self):
        return '<Employee %r %r, id=%d>' % (self.FirstName, self.LastName, self.EmployeeId)

    @classmethod
    def query(cls, session):
        return session.query(cls)


class Genre(Base):
    __tablename__ = 'Genre'

    GenreId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)

    def __init__(self, name=''):
        self.Name = name

    def __repr__(self):
        return '<Genre %r, id=%d>' % (self.Name, self.GenreId)

    @classmethod
    def query(cls, session):
        return session.query(cls)


class Invoice(Base):
    __tablename__ = 'Invoice'

    InvoiceId = Column(Integer, primary_key=True, autoincrement=True)
    CustomerId = Column(Integer, ForeignKey('Customer.CustomerId'), nullable=False)
    InvoiceDate = Column(DateTime, nullable=False)
    BillingAddress = Column(String)
    BillingCity = Column(String)
    BillingState = Column(String)
    BillingCountry = Column(String)
    BillingPostalCode = Column(String)
    Total = Column(Numeric)

    def __init__(self, invoiceDate, customerId):
        self.CustomerId = customerId
        self.InvoiceDate = invoiceDate

    def __repr__(self):
        return '<Invoice %d, cusId=%d, date=%r>' % (self.InvoiceId, self.CustomerId, self.InvoiceDate)

    @classmethod
    def query(cls, session):
        return session.query(cls)


class InvoiceLine(Base):
    __tablename__ = 'InvoiceLine'

    InvoiceLineId = Column(Integer, primary_key=True, autoincrement=True)
    InvoiceId = Column(Integer, ForeignKey('Invoice.InvoiceId'), nullable=False)
    TrackId = Column(Integer, ForeignKey('Track.TrackId'), nullable=False)
    UnitPrice = Column(Numeric)
    Quantity = Column(Integer, nullable=False)

    def __init__(self, invoiceId, trackId, quantity):
        self.InvoiceId = invoiceId
        self.TrackId = trackId
        self.Quantity = quantity

    def __repr__(self):
        return '<InvoiceLine invoicdId=%d, trackId=%d, quantity=%d>' % (self.InvoiceId, self.TrackId, self.Quantity)

    @classmethod
    def query(cls, session):
        return session.query(cls)


class MediaType(Base):
    __tablename__ = 'MediaType'

    MediaTypeId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)

    def __init__(self, name=''):
        self.Name = name

    def __repr__(self):
        return '<MediaType %r, id=%d>' % (self.Name, self.MediaTypeId)

    @classmethod
    def query(cls, session):
        return session.query(cls)


class Playlist(Base):
    __tablename__ = 'Playlist'

    PlaylistId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)

    def __init__(self, name=''):
        self.Name = name

    def __repr__(self):
        return '<Playlist %r, id=%d>' % (self.Name, self.PlaylistId)

    @classmethod
    def query(cls, session):
        return session.query(cls)


class PlaylistTrack(Base):
    __tablename__ = 'PlaylistTrack'

    PlaylistId = Column(Integer, ForeignKey('Playlist.PlaylistId'), nullable=False, primary_key=True)
    TrackId = Column(Integer, ForeignKey('Track.TrackId'), nullable=False, primary_key=True)

    def __init__(self, playListId, trackId):
        self.PlaylistId = playListId
        self.TrackId = trackId

    def __repr__(self):
        return '<PlaylistTrack playlistId=%d, trackId=%d>' % (self.PlaylistId, self.TrackId)

    @classmethod
    def query(cls, session):
        return session.query(cls)


class Track(Base):
    __tablename__ = 'Track'

    TrackId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String, nullable=False)
    AlbumId = Column(Integer, ForeignKey('Album.AlbumId'))
    MediaTypeId = Column(Integer, ForeignKey('MediaType.MediaTypeId'), nullable=False)
    GenreId = Column(Integer, ForeignKey('Genre.GenreId'))
    Composer = Column(String)
    Milliseconds = Column(Integer, nullable=False)
    Bytes = Column(Integer)
    UnitPrice = Column(Numeric)

    def __init__(self, name, mediaTypeId, milliseconds):
        self.Name = name
        self.MediaTypeId = mediaTypeId
        self.Milliseconds = milliseconds

    def __repr__(self):
        return '<Track %r, mediaTypeId=%d, milliseconds=%d>' % (self.Name, self.MediaTypeId, self.Milliseconds)

    @classmethod
    def query(cls, session):
        return session.query(cls)
