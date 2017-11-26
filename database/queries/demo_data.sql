INSERT INTO manufacturer (manufacturer_name)
VALUES
  ('Škoda'),
  ('Audi');

INSERT INTO model (manufacturer_id, model_name)
SELECT
  manufacturer_id, 'Superb' AS model_name
FROM manufacturer
WHERE manufacturer_name = 'Škoda';

INSERT INTO model (manufacturer_id, model_name)
SELECT
  manufacturer_id, 'Octavia' AS model_name
FROM manufacturer
WHERE manufacturer_name = 'Škoda';

INSERT INTO model (manufacturer_id, model_name)
SELECT
  manufacturer_id, 'A6' AS model_name
FROM manufacturer
WHERE manufacturer_name = 'Audi';

INSERT INTO color (color_name, red, blue, green, manufacturer_id)
SELECT 'Blue', 0, 255, 0, manufacturer_id
FROM manufacturer
WHERE manufacturer_name = 'Škoda';

INSERT INTO car (model_id, color_id)
VALUES (1, 1);
