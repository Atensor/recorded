create table artists (
    id integer primary key,
    name varchar
);
create or replace sequence seq_aid start 1;

create table labels (
    id integer primary key,
    name varchar
);
create or replace sequence seq_lid start 1;

create table genres (
    id integer primary key,
    name varchar
);
create or replace sequence seq_gid start 1;

create table users (
    id integer primary key,
    username varchar unique,
    password_hash varchar
);
create or replace sequence seq_uid start 1;

create table records (
    id integer primary key,
    title varchar,
    artist_id integer,
    label_id integer,
    date date,
    foreign key(artist_id) references artists(id),
    foreign key(label_id) references labels(id)
);
create or replace sequence seq_rid start 1;

create table tracks (
    id integer primary key,
    title varchar,
    record_id integer,
    track_nr integer,
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
    state varchar check (state in ('physical', 'digital', 'wanted', 'favourite')),
    primary key(user_id, record_id),
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
    rating integer,
    primary key(record_id, user_id),
    foreign key(record_id) references records(id),
    foreign key(user_id) references users(id)
);

create table track_ratings (
    track_id integer,
    user_id integer,
    rating integer,
    primary key(track_id, user_id),
    foreign key(track_id) references tracks(id),
    foreign key(user_id) references users(id)
);

