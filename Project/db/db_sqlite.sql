CREATE TABLE job_listing (
    id INT NOT NULL,
    source INT NOT NULL,
    employment_type VARCHAR(20),
    duration INT,
    min_salary INT,
    max_salary INT,
    salary_type SMALLINT, -- 1 = hourly, 2 = commision, 3 = fixed
    publication_date DATE NOT NULL, 
    job_id INT NOT NULL,
    location_id INT NOT NULL,
    date_gathered DATE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (job_id) REFERENCES job (id) ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES location (id) ON DELETE CASCADE
);

CREATE TABLE job (
    id INT NOT NULL,
    job VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE location (
    id INT NOT NULL,
    county VARCHAR(50),
    municipality VARCHAR(50),
    PRIMARY KEY (id)
);

CREATE TABLE requirement (
    id INT NOT NULL,
    requirement VARCHAR(50) NOT NULL,
    years_of_experience INT,
    PRIMARY KEY (id)
);


CREATE TABLE work_hours (
    id INT NOT NULL,
    work_hours VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);

-- dependancy tables

CREATE TABLE requirement_relation (
    job_listing_id INT NOT NULL,
    requirement_id INT NOT NULL,
    PRIMARY KEY (job_listing_id, requirement_id),
    FOREIGN KEY (job_listing_id) REFERENCES job_listing (id) ON DELETE CASCADE,
    FOREIGN KEY (requirement_id) REFERENCES requirement (id) ON DELETE CASCADE
);


CREATE TABLE work_hours_relation (
    job_listing_id INT NOT NULL,
    work_hours_id INT NOT NULL,
    PRIMARY KEY (job_listing_id, work_hours_id),
    FOREIGN KEY (job_listing_id) REFERENCES job_listing (id) ON DELETE CASCADE,
    FOREIGN KEY (work_hours_id) REFERENCES work_hours (id) ON DELETE CASCADE
);