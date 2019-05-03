<h1>Tietokantakaavio</h1>

![GitHub Logo](images/classdiagram1.png)
<br/><br/><br/>
Ohjelmaan kirjautuvat käyttäjät tallennetaan "account" tauluun. Jokaisella accountilla voi olla monta Pokemonia, mutta
Pokemonilla voi olla vain yksi account. Pokemon -olioon liittyy kaksi kokonaislukua: CP (combat power) ja IV (individual value).
Tämän lisäksi Pokemoniin liittyy aina kaksi Move -oliota, fastmove ja chargemove, mutta sama move voi olla käytössä usealla
Pokemonilla. Pokemoniin liittyy yhdestä kahteen Type -enumia. Move:lla on aina kokonaislukuarvoinen iskuvoima (damage). Myös Move
-olioilla on oma Type enum. Huomaa, että vaikka Pokemoniin liittyy kaksi Movea, joista molemmilla on Type, niin nämä tyypit ovat 
riippumattomia itse Pokemoniin liittyvästä yhdestä tai kahdesta tyypistä. Tämän lisäksi kaikilla tietokannan olioilla on 
luonnollisesti nimi (name). 

Ohjelmaan jätettiin myös keskeneräinen PokeStop luokka, jonka toiminnallisuus on oikeastaan irrallinen muista tauluista. Ne ovat
paikkoja, joissa kouluttajat voivat käydä, eli niillä on nimi ja sijaintikaupunki (city).

Alla on lueteltu kaikki SQL Create Table lausekkeet.

CREATE TABLE move (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        damage INTEGER NOT NULL, 
        chargemove INTEGER NOT NULL, 
        bars INTEGER, 
        first_type_id INTEGER NOT NULL, 
        PRIMARY KEY (id)
);

CREATE TABLE account (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        username VARCHAR(144) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id)
);

CREATE TABLE stop (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        city VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id)
);

CREATE TABLE pokemon (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(20) NOT NULL, 
        cp INTEGER NOT NULL, 
        iv INTEGER NOT NULL, 
        account_id INTEGER NOT NULL, 
        fastmove_id INTEGER NOT NULL, 
        chargemove_id INTEGER NOT NULL, 
        first_type_id INTEGER NOT NULL, 
        second_type_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(account_id) REFERENCES account (id), 
        FOREIGN KEY(fastmove_id) REFERENCES move (id), 
        FOREIGN KEY(chargemove_id) REFERENCES move (id)
);
