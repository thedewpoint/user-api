-- SELECT datname FROM pg_database;
-- CREATE EXTENSION IF NOT EXISTS "uuid-ossp";\




-- SELECT *
-- FROM pg_catalog.pg_tables
-- WHERE schemaname != 'pg_catalog' AND 
--     schemaname != 'information_schema';

-- ALTER TABLE users ALTER COLUMN zip TYPE char(5);


-- ALTER TABLE users ADD UNIQUE(email)



-- CREATE DATABASE mowbro;

-- CREATE TABLE Users (
--     id uuid DEFAULT uuid_generate_v4 (),
--     email VARCHAR(255) NOT NULL,
--     zip CHAR(5) NOT NULL,
--     PRIMARY KEY (id),
    --    UNIQUE(email)

-- );

-- INSERT into users (email, zip) VALUES 
-- ('test1@test.com', '19403'), 
-- ('test2@test.com', '19355') 