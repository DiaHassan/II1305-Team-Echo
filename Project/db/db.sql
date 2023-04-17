CREATE TABLE job_listing (
    id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    source INT NOT NULL,
    employment_type VARCHAR(20),
    duration INT,
    min_salary INT,
    max_salary INT,
    salary_type TINYINT, -- 1 = hourly, 2 = commision, 3 = fixed
    publication_date DATE NOT NULL, 
    job_id INT NOT NULL,
    location_id INT NOT NULL,
    date_gathered DATE NOT NULL
);

ALTER TABLE job_listing ADD CONSTRAINT PK_job_listing PRIMARY KEY (id);

CREATE TABLE job (
    id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    job VARCHAR(50) NOT NULL
);

ALTER TABLE job ADD CONSTRAINT PK_job PRIMARY KEY (id);


CREATE TABLE location (
    id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    county VARCHAR(50),
    municipality VARCHAR(50) -- TODO: Change max varchar
);

ALTER TABLE location ADD CONSTRAINT PK_location PRIMARY KEY (id);

CREATE TABLE requirement (
    id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    requirement VARCHAR(50) NOT NULL,
    years_of_experience INT
);

ALTER TABLE requirement ADD CONSTRAINT PK_requirement PRIMARY KEY (id);

CREATE TABLE work_hours (
    id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    work_hours INT NOT NULL
);

ALTER TABLE work_hours ADD CONSTRAINT PK_work_hours PRIMARY KEY (id);

-- dependancy tables

CREATE TABLE requirement_relation (
    job_listing_id INT NOT NULL,
    requirement_id INT NOT NULL
);

ALTER TABLE requirement_relation ADD CONSTRAINT PK_requirement_relation PRIMARY KEY (job_listing_id, requirement_id);

CREATE TABLE work_hours_relation (
    job_listing_id INT NOT NULL,
    work_hours_id INT NOT NULL
);

ALTER TABLE work_hours_relation ADD CONSTRAINT PK_work_hours_relation PRIMARY KEY (job_listing_id, work_hours_id);





-- TODO: Alter table foreign keys
-- TODO: Add Cascading delete