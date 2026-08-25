create table if not exists customers(
    id serial primary key,
    name text not null,
    updated_at timestamp default now()
);
insert into customers(name) values ('Cliente A');
update customers set name='Cliente A atualizado' where id=1;
