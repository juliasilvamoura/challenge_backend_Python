--QUESTÃO 1

-- A ideia é trazer nome, email, descrição de role e de claims para todos os usuários, porém para users que tiver mais de 1 claims será duplicado no resultado
-- Para resolver esse problema utilizei o group_concat para concatenar as claims dos users e agrupar por id, nome, email e descrição da role e ordenar de forma alfabética 
-- Também é possivel add um filtro por nome, ex: WHERE us.name = 'nome_esperado' na linha 15 entre o ultimo left join e antes de agrupar o resultado.

SELECT us.name as name_user, us.email as email_user, rl.description as description_role, 
GROUP_CONCAT(c.description, ', ') as description_claims -- pois user tem necessáriamente 1 ou mais claims, assim evita linhas repetidas
from users us
inner JOIN roles rl on rl.id = us.role_id
LEFT JOIN user_claims uc on uc.user_id = us.id
LEFT JOIN claims c on c.id = uc.claim_id
GROUP BY us.id, us.name, us.email, rl.description
order by us.name ASC;