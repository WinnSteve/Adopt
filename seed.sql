"""db creation for adopt"""

DROP DATABASE IF EXISTS  adopt;

CREATE DATABASE adopt;

\c adopt

CREATE TABLE pets
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  species TEXT NOT NULL,
  photo_url TEXT,
  age INT,
  notes TEXT,
  available BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO pets
  (name, species, photo_url, age, notes, available)
VALUES
  ('Doug', 'dog', 'https://vetstreet.brightspotcdn.com/dims4/default/1d87d20/2147483647/thumbnail/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2F3a%2Fc3%2F424ee1bf4768973966bde73acda8%2Fgerman-shepherd-AP-1S7FRX-645sm12913.jpg', 2, 'Loving heart', 't'),
  ('Spikey', 'porcupine', 'https://cdn.mos.cms.futurecdn.net/jFpJp5sJzEeeKtjAnHRM8K-1200-80.jpg', 3, 'Very Huggable', 't'),
  ('Mr Whiskers', 'cat', 'https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png', 4, null, 't'),
  ('Dr. Claw', 'cat', null, null, null, 't');
