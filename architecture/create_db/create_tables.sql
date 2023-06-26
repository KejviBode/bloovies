DROP TABLE IF EXISTS film_weekly_rank
DROP TABLE IF EXISTS film_review
DROP TABLE IF EXISTS film_review_score
DROP TABLE IF EXISTS film

CREATE TABLE film (
    film_id SERIAL4 PRIMARY KEY,
    film_name varchar(255) NOT NULL UNIQUE,
    release_date DATE NOT NULL
)

CREATE TABLE film_weekly_rank(
    film_rank_id SERIAL4 PRIMARY KEY,
    film_rank int NOT NULL,
    film_id int NOT NULL,
    created_at DATE NOT NULL,
    FOREIGN KEY (film_id) REFERENCES film (film_id)
)

CREATE TABLE film_review_score(
    film_review_score_id SERIAL4 PRIMARY KEY,
    film_id int NOT NULL,
    film_score int,
    film_score_date DATE NOT NULL,
    FOREIGN KEY (film_id) REFERENCES film (film_id)
)

CREATE TABLE film_review(
    film_review_id SERIAL4 PRIMARY KEY,
    film_review varchar(1024),
    film_id int NOT NULL,
    platform varchar(100) NOT NULL,
    created_at DATE NOT NULL,
    FOREIGN KEY (film_id) REFERENCES film (film_id)
)
