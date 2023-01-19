select * from person;
SELECT * FROM car;
select * from company;
-- WHERE
SELECT person.first_name, person.last_name, car.plate
from person, car 
where person.car_id = car.id;

SELECT last_name, name, make FROM person, company, car
WHERE person.company_id = company_id AND person.car_id = car.id
order by name, make;
--join
select last_name, make, model FROM person JOIN car ON
person.car_id=car.id;

SELECT last_name,make, model, plate, name FROM person
    JOIN car on person.car_id = car.id
    join company on person.company_id = company.id
    where make = "Ford"
    ORDER BY name DESC;

SELECT name, count(*) as count FROM person 
JOIN company on company_id = company.id
GROUP BY name
HAVING count > 3;

--isrinkti tik apple darbuotoju auto numerius
SELECT plate, make FROM car
JOIN person ON person.car_id = car.id
JOIN company on person.company_id = company.id
where company.name = "Apple";

--isrinkti varda, pav, auto gamintoja ir imone tik is tu imoniu, kuriose dirba iki 3 darbuotoju.
SELECT first_name, last_name, make, name FROM person
join car on car_id = car.id
JOIN company on company_id = company.id
WHERE company_id IN (
SELECT company.id FROM company
join person on person.company_id=company.id
GROUP BY name HAVING count() <=3 order by name);

SELECT first_name, last_name, make, model, plate FROM person
LEFT join car on car_id = car.id;

-- insert into car (make, model, plate)
-- values("Dethleffs", "A1558", "BGI555");

SELECT first_name, last_name, make, model FROM car
left join  person on car.id = person.car_id;