drop table if exists cards;

-- Cards
create table cards (
    id serial primary key,

    title varchar(100) not null,
    description text,
    status varchar(30) not null default 'To Do',
    date_created timestamp default current_timestamp
);

insert into cards (title, description, status) values 
    ('Start the project', 'Stage 1 - ERD Creation', 'Done'),
    ('ORM Queries', 'Stage 2 - Implement CRUD queries', 'In Progress'),
    ('Marshmallow', 'Stage 3 - Implement JSONify of models', 'In Progress')
;