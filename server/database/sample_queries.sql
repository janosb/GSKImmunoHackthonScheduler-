SELECT COUNT(*) as num_rooms_available FROM schedule
WHERE timestamp = '2018-08-06Z09:00:00'
AND is_available;


SELECT
  p.first_name,
  p.last_name,
  v.vaccine_name,
  v.recommendation_text
  FROM patients p
   JOIN demos d
    ON
     (p.current_age_bin = d.age_bin)
     AND
     (p.sex = d.sex)
     AND
     (p.is_known_pregnant = d.is_pregnant)
   JOIN vaccine_recommendations v
    ON
     (d.demo_id = v.demo_id)
  WHERE
   family_id = (SELECT family_id
                FROM patients
                WHERE full_name = 'Margaret-Ann_De_Luca')
   AND
   is_vaccine_hesitant = 0;