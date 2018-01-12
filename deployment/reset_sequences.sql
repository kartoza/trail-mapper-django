SELECT setval('trail_mapper_category_id_seq', COALESCE((SELECT MAX(id)+1 FROM trail_mapper_category), 1), false);
SELECT setval('trail_mapper_grade_id_seq', COALESCE((SELECT MAX(id)+1 FROM trail_mapper_grade), 1), false);
SELECT setval('trail_mapper_poi_id_seq', COALESCE((SELECT MAX(id)+1 FROM trail_mapper_pointofinterest), 1), false);
SELECT setval('trail_mapper_trail_id_seq', COALESCE((SELECT MAX(id)+1 FROM trail_mapper_trail), 1), false);
SELECT setval('trail_mapper_trailsection_id_seq', COALESCE((SELECT MAX(id)+1 FROM trail_mapper_trailsection), 1), false);
