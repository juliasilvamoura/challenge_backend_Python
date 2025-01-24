--QUESTÃO 1

-- A ideia é trazer nome, email, descrição de role e de claims para todos os usuários, porém para users que tiver mais de 1 claims será duplicado no resultado
-- Para resolver esse problema utilizei o group_concat para concatenar as claims dos users e agrupar por id, nome, email e descrição da role e ordenar de forma alfabética 

SELECT us.name as name_user, 
    us.email as email_user, 
    rl.description as description_role, 
    GROUP_CONCAT(c.description, ', ') as description_claims -- pois user tem necessáriamente 1 ou mais claims, assim evita linhas repetidas
FROM users us
INNER JOIN roles rl 
    ON rl.id = us.role_id
LEFT JOIN user_claims uc 
    ON uc.user_id = us.id
LEFT JOIN claims c 
    ON c.id = uc.claim_id
GROUP BY us.id, us.name, us.email, rl.description
ORDER BY us.name ASC;