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

![GitHub Logo](images/createtable.png)
