from sqlalchemy import column,String,Integer,Float,ForeignKey 
from sqlalchemy.ext.declarative import declarative_base

class Geo():
    __tablename__: 'geos'
    id = column(Integer, primarykey = True)
    lat = column(Float, nullable=False)
    lng = column(Float, nullable=False)

class Address():
    __tablename__: 'adressess'
    id = column(Integer, primarykey = True)
    street = column(String(30), nullable = False) 
    suite = column(String(30), nullable = False) 
    city = column(String(30), nullable = False)
    zipcode = column(String(10),nullable = False)
    geoId = column(Integer, nullable = False) 

class Company():
    __tablename__: 'companies'
    id = column( Integer,primarykey = True) 
    name = column(String (30),nullable = False) 
    catchPhrase = column(String(255),nullable = False) 
    bs = column(String(100),nullable = False) 

class User():
    __tablename__: 'users'
    id = column(Integer, primarykey = True)
    name = column(String(30),nullable = False)
    username = column(String(15),nullable = False) 
    email = column(String(255),nullable = False)
    phone = column(String(25), nullable = False)
    website = column(String(255),nullable = False) 
    adressId = column(Integer, nullable = False)
    companyId = column(Integer, nullable = False)

class Post():
    __tablename__: 'posts'
    id = column(Integer, primarykey = True)
    title = column(String(50), nullable = False)
    body = column(String(255), nullable = False)
    userId = column(Integer, nullable = False)

class Usuario():
    __tablename__: 'usuarios'
    id =column(Integer, primarykey = True)
    username = column(String(30),nullable = False)
    email = column(String(255),nullable = False)
    contrasena = column(String(255), nullable = False)
    sal = column(String(255),nullable = False)

