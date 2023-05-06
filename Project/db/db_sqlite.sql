CREATE TABLE job_listing (
    id INTEGER NOT NULL,
    source VARCHAR(20) NOT NULL,
    employment_type VARCHAR(20),
    duration VARCHAR(20),
    publication_date DATE NOT NULL, 
    profession VARCHAR(50) NOT NULL,
    county VARCHAR(50),
    requirement VARCHAR(50) NOT NULL,
    years_of_experience INT,
    seniority VARCHAR(15),
    date_gathered DATE NOT NULL,

    PRIMARY KEY (id)
    -- FOREIGN KEY (job_id) REFERENCES job (id) ON DELETE CASCADE
);

-- CREATE TABLE job (
--     id INTEGER NOT NULL,
--     profession VARCHAR(50) NOT NULL,
--     PRIMARY KEY (id)
-- );

-- CREATE TABLE requirement (
--     id INTEGER NOT NULL,
--     requirement VARCHAR(50) NOT NULL,
--     PRIMARY KEY (id)
-- );


-- CREATE TABLE work_hours (
--     id INT NOT NULL,
--     work_hours VARCHAR(20) NOT NULL,
--     PRIMARY KEY (id)
-- );

-- dependancy tables

-- CREATE TABLE requirement_relation (
--     job_listing_id INTEGER NOT NULL,
--     requirement_id INTEGER NOT NULL,
--     PRIMARY KEY (job_listing_id, requirement_id),
--     FOREIGN KEY (job_listing_id) REFERENCES job_listing (id) ON DELETE CASCADE,
--     FOREIGN KEY (requirement_id) REFERENCES requirement (id) ON DELETE CASCADE
-- );


-- CREATE TABLE work_hours_relation (
--     job_listing_id INT NOT NULL,
--     work_hours_id INT NOT NULL,
--     PRIMARY KEY (job_listing_id, work_hours_id),
--     FOREIGN KEY (job_listing_id) REFERENCES job_listing (id) ON DELETE CASCADE,
--     FOREIGN KEY (work_hours_id) REFERENCES work_hours (id) ON DELETE CASCADE
-- );