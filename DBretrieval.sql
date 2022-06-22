create database CompanyProj;
use CompanyProj;

create table employeeProj (
	Fname varchar(25) not null,
    Minit varchar(2),
    Lname varchar(25) not null,
    Ssn int not null,
    Bdate date,
    Address varchar(25),
    Sex varchar(7),
    Salary int,
    Super_ssn int,
    Dno int not null,
    primary key (Ssn)
);

create table logininfo as select ssn as username from employeeProj;

alter table logininfo 
add password varchar(25);

Alter table companyproj.logininfo 
add  primary key (username);

update logininfo
set password = concat('Aa',username);

