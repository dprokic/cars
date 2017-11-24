CREATE TABLE manufacturer (
  manufacturer_id SERIAL PRIMARY KEY,
  manufacturer_name TEXT
);

CREATE TABLE model (
  model_id SERIAL PRIMARY KEY,
  manufacturer_id INTEGER REFERENCES manufacturer,
  model_name TEXT
);

CREATE TABLE color (
  color_id SERIAL PRIMARY KEY,
  color_name TEXT,
  red SMALLINT,
  green SMALLINT,
  blue SMALLINT,
  manufacturer_id INTEGER REFERENCES manufacturer
);

CREATE TABLE equipment (
  equipment_id SERIAL PRIMARY KEY,
  equipment_name TEXT
);

CREATE TABLE equipment_at_manufacturer (
  equipment_id INTEGER REFERENCES equipment,
  manufacturer_id INTEGER REFERENCES manufacturer,
  equipment_name TEXT,
  PRIMARY KEY (equipment_id, manufacturer_id)
);

CREATE TABLE equipment_package (
  package_id SERIAL PRIMARY KEY,
  package_name TEXT,
  model_id INTEGER REFERENCES model
);

CREATE TABLE equipment_package_equipment (
  package_id INTEGER REFERENCES equipment_package,
  equipment_id INTEGER REFERENCES equipment,
  PRIMARY KEY (package_id, equipment_id)
);

CREATE TABLE car (
  car_id SERIAL PRIMARY KEY,
  model_id INTEGER REFERENCES model,
  color_id INTEGER REFERENCES color,
  package_id INTEGER REFERENCES equipment_package
);

CREATE TABLE car_equipment (
  car_id INTEGER REFERENCES car,
  equipment_id INTEGER REFERENCES equipment,
  PRIMARY KEY (car_id, equipment_id)
);
