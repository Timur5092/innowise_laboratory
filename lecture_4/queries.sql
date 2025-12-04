-- 3. Все оценки Alice Johnson
SELECT g.subject, g.grade
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.full_name = 'Alice Johnson';

-- 4. Средняя оценка каждого студента
SELECT s.full_name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id;

-- 5. Студенты, родившиеся после 2004
SELECT full_name, birth_year
FROM students
WHERE birth_year > 2004;

-- 6. Средняя оценка по каждому предмету
SELECT subject, AVG(grade) AS average_grade
FROM grades
GROUP BY subject;

-- 7. Топ-3 студента по среднему баллу
SELECT s.full_name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 3;

-- 8. Студенты с оценками ниже 80
SELECT DISTINCT s.full_name
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80;
