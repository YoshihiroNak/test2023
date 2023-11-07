drop table items;
drop table caategories;

-- Categories
create table categories (
    id serial primary key,

    name varchar(50) not null unique,
    description text
);

insert into categories (name, description) values
    ('Electronic', 'Gadgets to make life easier'),
    ('Car Parts', 'Expensive stuff for the box with 4 wheels'),
    ('Sports', 'Get out and play'),
    ('Video Game', 'Stay in and play!')
;


-- items
create table items (
    id serial primary key,

    name varchar(200) not null,
    description text not null,

    category_id integer not null,
    foreign key (category_id) references categories (id)
);


