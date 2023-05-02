DROP DATABASE IF EXISTS g18finalproj;

CREATE DATABASE g18finalproj;

USE g18finalproj;
#Create tables
CREATE TABLE user (
    username            VARCHAR(64),
    lname            VARCHAR(64),
    fname            VARCHAR(64),
    password        VARCHAR(64),
    id              INT PRIMARY KEY AUTO_INCREMENT,
    email            VARCHAR(64),
    bio             TINYTEXT,
    join_date		DATE
);

CREATE TABLE post (
    contents        TEXT(65535),
    id              INT PRIMARY KEY AUTO_INCREMENT,
    post_date		DATETIME
);

CREATE TABLE board (
    name            VARCHAR(64),
    description     TINYTEXT,
    id              INT PRIMARY KEY
);

CREATE TABLE author (
    user_id         INT,
    post_id         INT,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (post_id) REFERENCES post(id)
);

CREATE TABLE post_location (
    post_id         INT,
    board_id        INT,
    FOREIGN KEY (post_id) REFERENCES post(id),
    FOREIGN KEY (board_id) REFERENCES board(id)
);