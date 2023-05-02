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

#Create data

INSERT INTO user (username, lname, fname, password, email, bio, join_date)
VALUES ('jkelly', 'Kelly', 'James', 'cheese123!', 'jkelly81@uncc.edu', 'I love SQL programming', '2023-05-02'),
('epatel', 'Patel', 'Esha', 'crackers123!', 'epatel7@uncc.edu', 'I love HTML programming', '2023-05-02'),
('jxu', 'Xu', 'Jeffrey', 'grapes123!', 'jxu18@uncc.edu',  'I love SQLAlchemy programming', '2023-05-02'),
('jyang', 'Yang', 'Jim', 'pigsinablanket123!', 'jyang77@uncc.edu', 'I love HTML programming', '2023-05-02');

INSERT INTO board VALUES
('General Help/Questions', 'A spot for all your questions regarding CCI or UNCC as a whole!', 0),
('Memes', 'Memes and jokes about UNCC CCI for when you\'re taking a break!', 1),
('ITSC-3155', 'A forum for all questions regarding Intro to Software Engineering', 10),
('ITCS-3145', ' A forum for all questions regarding Intro to Parallel and Distributed Computing', 11);

INSERT INTO post (contents, post_date) VALUES
('I need help with SQLAlchemy. I don\'t really understand how to get started', '2023-05-02'),
('What time is the final exam?', '2023-05-02'),
('A computer scientist walks into a bar and asks for 10 beers for him and his friend', '2023-05-02'),
('What is parallel and distributed computing?', '2023-05-02'),
('How do I switch majors to be a computer scientist?', '2023-05-02');

INSERT INTO post_location VALUES
(1, 10),
(2, 10),
(3, 1),
(4, 11),
(5, 0);

INSERT INTO author VALUES
(1, 1),
(3, 2),
(2, 3),
(1, 4),
(4, 5);