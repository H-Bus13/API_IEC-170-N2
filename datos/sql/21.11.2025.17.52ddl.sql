Create table if not exists geos(
    id Integer Auto_increment, 
    lat decimal not null, 
    lng decimal not null, 
    
    Constraint pk_geos primary key(id)
)

Create table if not exists adresses(
    id Integer Auto_increment,
    street Varchar (30) not null, 
    suite Varchar(30) not null, 
    city Varchar(30) not null, 
    zipcode Varchar(10) not null,
    geoId Integer not null, 

    Constraint pk_adresses primary key (id)
    Constraint fk_adress foreign key (geoId) references geos(id)
)

Create table if not exists companies(
    id Integer Auto_increment,
    name Varchar(30) not null,
    catchPhrase Varchar(255) not null, 
    bs Varchar(100) not null, 
    
    Constraint pk_companies primary key(id)
)
Create table if not exists users(
    id Integer Auto_increment,
    name Varchar(30) not null, 
    username Varchar(15) not null, 
    email Varchar(255) not null,
    phone Varchar(25) not null, 
    website Varchar(255) not null, 
    adressId Integer not null, 
    companyId Integer not null, 
     
    Constraint pk_users primary key(id)
    Constraint fk_users_company foreign key (companyId) references companies(id)

);

Create table if not exists posts(
    id Integer Auto_increment,
    title Varchar(50) not null,
    body Varchar(255) not null, 
    userId Integer not null,
    
    Constraint pk_posts primary key(id)
    Constraint fk_posts_users foreign key (userId) references users (id)
);