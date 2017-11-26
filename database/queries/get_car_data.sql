SELECT
  mf.manufacturer_name,
  m.model_name,
  color.color_name
FROM car
  INNER JOIN model m
    ON car.model_id = m.model_id
  INNER JOIN manufacturer mf
    ON m.manufacturer_id = mf.manufacturer_id
  INNER JOIN color
    ON car.color_id = color.color_id