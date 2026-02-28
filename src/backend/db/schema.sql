create table artists (
    id integer primary key,
    name varchar not null
);
create or replace sequence seq_aid start 1;

create table labels (
    id integer primary key,
    name varchar not null
);
create or replace sequence seq_lid start 1;

create table genres (
    id integer primary key,
    name varchar not null
);
create or replace sequence seq_gid start 1;

create table users (
    id integer primary key,
    username varchar unique not null,
    password_hash varchar not null,
    role varchar check (role in ('admin', 'moderator', 'user')) 
);
create or replace sequence seq_uid start 1;

insert into users values (
    nextval('seq_uid'),
    'Admin',
    '$argon2id$v=19$m=65536,t=3,p=4$qomXHLW2pI7MFXycuQ87iA$9uJIkLls/RbQsqNuqiLLw8GBktaImABi780mAt1AgqQ'
);

update
        users
    set
        role = 'admin'
    where
        id = 1;

create table records (
    id integer primary key,
    title varchar not null,
    artist_id integer not null,
    label_id integer not null,
    date date not null,
    art_path varchar,
    foreign key(artist_id) references artists(id),
    foreign key(label_id) references labels(id)
);
create or replace sequence seq_rid start 1;

create table tracks (
    id integer primary key,
    title varchar not null,
    record_id integer  not null,
    track_nr integer not null,
    duration integer not null,
    foreign key(record_id) references records(id)
);
create or replace sequence seq_tid start 1;

create table lyrics (
    track_id integer primary key,
    text text,
    foreign key(track_id) references tracks(id)
);

create table user_records (
    user_id integer,
    record_id integer,
    tag varchar check (tag in ('physical', 'digital', 'wanted', 'favourite')),
    primary key(user_id, record_id, tag),
    foreign key(user_id) references users(id),
    foreign key(record_id) references records(id)
);

create table record_genres (
    record_id integer,
    genre_id integer,
    primary key(record_id, genre_id),
    foreign key(record_id) references records(id),
    foreign key(genre_id) references genres(id)
);

create table track_features (
    track_id integer,
    artist_id integer,
    primary key(track_id, artist_id),
    foreign key(track_id) references tracks(id),
    foreign key(artist_id) references artists(id)
);

create table record_ratings (
    record_id integer,
    user_id integer,
    rating integer not null,
    primary key(record_id, user_id),
    foreign key(record_id) references records(id),
    foreign key(user_id) references users(id)
);

create table track_ratings (
    track_id integer,
    user_id integer,
    rating integer not null,
    primary key(track_id, user_id),
    foreign key(track_id) references tracks(id),
    foreign key(user_id) references users(id)
);

