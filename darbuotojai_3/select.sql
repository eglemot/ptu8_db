SELECT * FROM DARBUOTOJAS;
select * FROM PROJEKTAS;
SELECT * from SKYRIUS;

--Išrinkite darbuotojų vardus
--ir pavardes kartu su projekto pavadinimu, kuriame jie dirba.

-- SELECT VARDAS, PAVARDĖ, PAVADINIMAS
--  from DARBUOTOJAS, PROJEKTAS
--  WHERE DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID;

--Išsirinkite darbuotojų dirbančių projekte
--Galerija vardus, pavardes ir projekto pavadinimą.

-- SELECT VARDAS, PAVARDĖ, PAVADINIMAS
-- from DARBUOTOJAS, PROJEKTAS
-- where PAVADINIMAS="Galerija";

-- Išrinkite visus projekto Projektų valdymas vykdytojus
--  dirbančius Pardavimų skyriuje.

-- select vardas from DARBUOTOJAS
-- where PROJEKTAS_ID=2 and SKYRIUS_ID=3;

-- Išrinkite visas moteris, dirbančias projekte Projektų valdymas
-- ir išveskite į ekraną jų vardus, pavardes ir projekto pavadinimą.

-- SELECT VARDAS, PAVARDĖ, PAVADINIMAS from DARBUOTOJAS, PROJEKTAS
-- WHERE (ASMENS_KODAS LIKE "4%" or ASMENS_KODAS LIKE "6%") 
-- and PAVADINIMAS = "Projektų valdymas";

-- Išrinkite skyrių pavadinimus
-- su juose dirbančių darbuotojų skaičiumi.

-- SELECT PAVADINIMAS, count(*) as skaicius from DARBUOTOJAS
-- JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID=SKYRIUS.ID
-- GROUP BY PAVADINIMAS;

-- Apribokite #5 užklausos rezultatą taip,
-- kad rodytų tik tuos skyrius kur dirba bent 5 darbuotojai.

-- SELECT PAVADINIMAS, count(*) as skaicius from DARBUOTOJAS
-- JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID=SKYRIUS.ID
-- GROUP BY PAVADINIMAS
-- HAVING skaicius > 5;

-- Išrinkite darbuotojus (vardus, pavardes, pareigas) kartu su skyrių,
-- kuriuose jie dirba pavadinimais,
-- tačiau nesančius tų skyrių vadovais.

-- SELECT VARDAS, PAVARDĖ, PAREIGOS, PAVADINIMAS 
-- FROM DARBUOTOJAS
-- JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID=SKYRIUS.ID
-- WHERE PAREIGOS != "Vadovas";

-- Sukurkite naują įrašą lentelėje “DARBUOTOJAS”
-- (asmens kodas: 38807117896, vardas: Pranas, pavardė:Logis, Dirba nuo: 2009-11-12, visa kita - Null).

-- INSERT INTO DARBUOTOJAS (VARDAS, PAVARDĖ, ASMENS_KODAS, DIRBA_NUO)
-- VALUES("Pranas", "Logis", 38807117896, "2009-11-12");

-- Išrinkite darbuotojų vardus, pavardes ir skyriaus pavadinimą. 
-- Rodykite, net ir tuos darbuotojus, kurie nedirba jokiame skyriuje
-- (skyriaus pavadinimą pasiimkite iš lentelės SKYRIUS).

-- SELECT VARDAS, PAVARDĖ, PAVADINIMAS from DARBUOTOJAS
-- LEFT JOIN skyrius on darbuotojas.SKYRIUS_ID=SKYRIUS.ID;

-- 1# punkto užklausą pataisykite taip, kad rodytų tik tuos vardus 
-- ir projektų pavadinimus kuriuose dirba daugiau nei 4 darbuotojai.

-- SELECT VARDAS, PAVADINIMAS from DARBUOTOJAS
-- JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
-- WHERE PROJEKTAS_ID IN 
-- (SELECT PROJEKTAS_ID FROM DARBUOTOJAS
-- JOIN PROJEKTAS ON DARBUOTOJAS.PROJEKTAS_ID = PROJEKTAS.ID
-- GROUP BY PROJEKTAS_ID 
-- HAVING count(*) > 4);

-- Naujame stulpeyje parodyti kiekvieno darbuotojo
-- bazinio atlyginimo ir priedų sumą.

-- SELECT VARDAS,PAVARDĖ, BAZINIS_ATLYGINIMAS + PRIEDAI
-- FROM DARBUOTOJAS;

-- Parodyti bendrą atlyginimų, priedų sumą, vidutinį,
-- maksimalų, minimalų atlyginimą.

-- SELECT sum(BAZINIS_ATLYGINIMAS), sum(PRIEDAI),
-- min(BAZINIS_ATLYGINIMAS), max(BAZINIS_ATLYGINIMAS),
--  avg(BAZINIS_ATLYGINIMAS) from DARBUOTOJAS;

