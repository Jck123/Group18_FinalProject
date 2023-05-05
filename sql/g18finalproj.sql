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

CREATE TABLE board (
    name            VARCHAR(64),
    description     TINYTEXT,
    id              INT PRIMARY KEY
);

CREATE TABLE post (
    contents        TEXT(65535),
    id              INT PRIMARY KEY AUTO_INCREMENT,
    board_id		INT,
    author_id		INT,
    post_date		DATETIME,
    FOREIGN KEY (board_id) REFERENCES board(id),
    FOREIGN KEY (author_id) REFERENCES user(id)
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

INSERT INTO post (contents, post_date, author_id, board_id) VALUES
('I need help with SQLAlchemy. I don\'t really understand how to get started', '2023-05-02', 1, 10),
('What time is the final exam?', '2023-05-02', 3, 10),
('A computer scientist walks into a bar and asks for 10 beers for him and his friend', '2023-05-02', 2, 1),
('What is parallel and distributed computing?', '2023-05-02', 1, 11),
('How do I switch majors to be a computer scientist?', '2023-05-02', 4, 0);