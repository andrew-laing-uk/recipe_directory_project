-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  dish_name text,
  cooking_time int,
  rating int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (dish_name, cooking_time, rating) VALUES ('Creamy Vegan Pasta', 120, 4);
INSERT INTO recipes (dish_name, cooking_time, rating) VALUES ('Cold Noodles with Roasted Tomatoes', 45, 3);
INSERT INTO recipes (dish_name, cooking_time, rating) VALUES ('Curried Jasmine Rice with Tofu and Vegetables', 90, 4);
INSERT INTO recipes (dish_name, cooking_time, rating) VALUES ('Bucatini Pasta with Arugula Pesto', 100, 4);
INSERT INTO recipes (dish_name, cooking_time, rating) VALUES ('Crispy BBQ Tofu Sandwich', 30, 5);
INSERT INTO recipes (dish_name, cooking_time, rating) VALUES ('Morrocan Chickpea Salad', 40, 3);
INSERT INTO recipes (dish_name, cooking_time, rating) VALUES ('Tamales', 20, 2);
INSERT INTO recipes (dish_name, cooking_time, rating) VALUES ('Vegan Pozole', 60, 5);
INSERT INTO recipes (dish_name, cooking_time, rating) VALUES ('Thick Soup with Beans', 60, 3);
INSERT INTO recipes (dish_name, cooking_time, rating) VALUES ('Berry-tastic Desert', 40, 5);

