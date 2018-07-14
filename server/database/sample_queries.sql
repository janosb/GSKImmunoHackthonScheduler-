SELECT timestamp
FROM public.schedule
WHERE num_resources_available >= 2
ORDER BY timestamp;

SELECT
  p.full_name,
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