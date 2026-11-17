


drop table if exists Student;
drop table if exists Club;
drop table if exists Member;
drop table if exists Faculty;
drop table if exists Advise;
drop table if exists Events;
drop table if exists Meetings;

create table Student (
    id char(9) primary key,
    name varchar(50)
);

create table Club (
    name varchar(50) primary key
);

create table Member (
    studentID char(9),
    clubName varchar(50),
    memberYear int,
    constraint fk_member_id foreign key (studentID) references Student(id),
    constraint fk_member_club foreign key (clubName) references Club(name),
    primary key(studentID, clubName)
);

create table Faculty (
    id char(9) primary key,
    name varchar(50)
);

create table Advise (
    facultyID char(9),
    clubName varchar(50),
    constraint fk_advise_id foreign key (facultyID) references Faculty(id),
    constraint fk_advise_club foreign key (clubName) references Club(name),
    primary key (facultyID, clubName)
);

create table Events (
    eventDate date,
    startTime time(3),
    clubName varchar(50),
    endTime time,
    eventDescription text,
    constraint fk_event_club foreign key (clubName) references Club(name),
    primary key (eventDate, startTime, clubName)
);

create table Meetings (
    meetingDate date,
    startTime time,
    clubName varchar(50),
    endTime time,
    classroom varchar(50),
    constraint fk_meeting_club foreign key (clubName) references Club(name),
    primary key (meetingDate, startTime, clubName)
);

--Ensures no two events overlap
delimiter //
create trigger if not exists trigger_event_insert
before insert on employee
for each row
begin
    
