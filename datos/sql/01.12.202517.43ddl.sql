Create table if not exists usuarios(
    id Integer Auto_increment,
    username Varchar(30) not null, 
    email Varchar(255) not null,
    contrasena varchar(255) not null,
    sal varchar(255) not null,
     
    Constraint pk_usuarios primary key(id)
);