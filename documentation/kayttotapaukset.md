<h1>Käyttötapaukset</h1
  
<h3>Käyttäjätunnuksen luominen</3>

Jos käyttäjällä ei ole vielä tunnusta, hän klikkaa yläpalkista "Sign in", jolloin avautuu lomake. Lomakkeeseen kirjoitetaan uusi
käyttäjätunnus sekä salasana kahdesti, jonka jälkeen lomake lähetetään alla olevasta painikkeesta. 

SQL: INSERT INTO account (date_created, date_modified, name, username, password) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?) VALUES ('Ash', 'Ash', 'Ketchum')

<h3>Sisäänkirjautuminen</h3>

Kun käyttäjällä on tunnukset, hän klikkaa yläpalkista "Log in" ja syöttää avautuneeseen lomakkeeseen käyttäjätunnuksen ja 
salasanan ja painaa alla olevaa lähetyspainiketta. Jos tunnukset ovat oikein, käyttäjä ohjataan etusivulle, jolloin hän pääsee 
käsiksi tietokannan muokkaamiseen. 

SQL: SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password 
FROM account WHERE account.username = 'Ash' AND account.password = 'Ketchum'

<h3>Liikkeiden lisääminen</h3>

Käyttäjä haluaa lisätä uuden liikkeen tietokantaan. Tällöin hän valitsee yläpalkista linkin "Add a New Move" ja pääsee Moven
lisäämiseen tarkoitettuun lomakkeeseen. Lomakkeeseen syötetään ensin nimi tekstikenttään ja liikkeen tuottama "vahinko" eli
damage numeroina tekstikenttään. Tämän jälkeen klikataan rasti "charged" ruutuun jos liike on charge -tyyppinen. Sitten bars
-kenttään käyttäjän kirjoittaa '0' mikäli liike on "fast" tyyppinen ja muulloin kirjoitetaan numeroina ns. palkkien lukumäärä,
joka on lukuarvo noin yhdestä kahdeksaan. Lomake lähetetään alla olevasta painikkeesta, jolloin isku lisätään tietokantaan. 

SQL: INSERT INTO move (date_created, date_modified, name, damage, chargemove, bars, first_type_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?) VALUES ('Thunder Shock', 5, 0, 0, '5')

<h3>Pokemonin lisääminen</h3>

Käyttäjä haluaa lisätä uuden Pokemonin tietokantaan. Tällöin hän klikkaa sivun yläpalkista linkkiä "Add a New Pokemon" ja pääsee
lomakesivulle. Lomakesivulla hän kirjoittaa tekstikenttiin ensin nimen merkkijonona ja sitten CP arvon (10-4500) ja IV arvon 
(0-100) lukuna. Sitten valitaan dropdown valikoista fastmove ja chargemove. Huomaa, että liikkeiden täytyy olla tietokannassa,
ennen kuin lisäät pokemonia, eli jos haluat käyttää liikkeitä, joita ei ole vielä tietokannassa, katso kohta "Liikkeiden 
lisääminen". Sitten valitaan dropdown menusta Pokemonille kaksi tyyppiä. Jos pokemonilla on vain yksi tyyppi, valitse toisen
tyypin valinnassa "Empty". Lopuksi hän klikkaa "Submit" -otsikon alla olevaa painiketta. Tällöin käyttäjä uudelleenohjataan
etusivulle, jossa on listaus kaikista Pokemoneista ja lisätyn Pokemonin tulisi nyt löytyä listasta.

SQL: INSERT INTO pokemon (date_created, date_modified, name, cp, iv, account_id, fastmove_id, chargemove_id, first_type_id, second_type_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?, ?, ?) VALUES ('Pikachu', 500, 50, 1, '1', '2', '5', '1')

Pokemonien lisäämiseen ja päivittämiseen tarvitaan myös seuraavia kyselyitä, jotta saadaan liikkeiksi tarjolla olevat 
vaihtoehtot.

SQL: "select * from move where chargemove = 0;"

SQL: "select * from move where chargemove = 0;"

<h3>Pokemonien tarkastelu</h3>

Käyttäjä haluaa tarkastella Pokemonien listaa. Tällöin hän klikkaa sivun yläpalkista linkkiä "Front Page", jolloin hänet ohjataan
etusivulle, jossa on kaikki Pokemonit listattuna. "Name" -sarakkeessa on Pokemonin nimi, "CP" -sarakkeessa Combat Points -arvo ja
"IV" -sarakkeessa Individual Value -arvo. "Fast Move" ja "Charge Move" -sarakkeista löytyy pokemonin liikkeiden nimet. "Type 1"
ja "Type 2" -sarakkeista löytyy pokemonin molemmat tyypit. Jos käyttäjä haluaa tutkia pokemonin omia sivuja, hän klikkaa tämän
pokemonin riviltä "View" -saraketta, josta avautuu Pokemonin oma sivu, jolla kerrotaan tarkemmin, mitä pokemoniin liittyvillä
tiedoilla tarkoitetaan. Tähän sivuun liittyy alla oleva SQL -kysely.

SQL: SELECT pokemon.id AS pokemon_id, pokemon.date_created AS pokemon_date_created, pokemon.date_modified AS pokemon_date_modified, pokemon.name AS pokemon_name, pokemon.cp AS pokemon_cp, pokemon.iv AS pokemon_iv, pokemon.account_id AS pokemon_account_id, pokemon.fastmove_id AS pokemon_fastmove_id, pokemon.chargemove_id AS pokemon_chargemove_id, pokemon.first_type_id AS pokemon_first_type_id, pokemon.second_type_id AS pokemon_second_type_id 
FROM pokemon WHERE pokemon.id = 1

<h3>Liikkeiden tarkastelu</h3>

Käyttäjä haluaa tarkastella liikkeiden listaa. Tällöin hän klikkaa sivun yläpalkista linkkiä "Front Page", jolloin hänet ohjataan
etusivulle, jossa on kaikki tietokannan liikkeet listattuna, pokemonien listan alapuolella. "Name" -sarakkeessa on liikkeen nimi.
"Damage" -sarakkeessa on iskun tuottama vahinko pisteinä. Jos liike on charge -tyyppinen, vahinko on ilmoitettu per bar tyyliin,
esim. jos bareja eli palkkeja olisi 2 ja damagen määräksi on ilmoitettu 90, vahinko on 90 per käytetty palkki. "Is Charged" 
-sarake ilmoittaa onko liike charged -tyyppinen (true) vai fast -tyyppinen (false). "Bars" -sarake ilmoittaa palkkien määrän,
jonka tulisi olla 0 kaikilla fast moveilla. Jos käyttäjä haluaa tutkia liikkeen omia sivuja, hän klikkaa tämän
moven riviltä "View" -saraketta, josta avautuu liikkeen oma sivu, jolla kerrotaan tarkemmin, mitä liikkeeseen liittyvillä
tiedoilla tarkoitetaan. Tähän sivuun liittyy alla oleva SQL -kysely.

SQL: SELECT move.id AS move_id, move.date_created AS move_date_created, move.date_modified AS move_date_modified, move.name AS move_name, move.damage AS move_damage, move.chargemove AS move_chargemove, move.bars AS move_bars, move.first_type_id AS move_first_type_id FROM move WHERE move.id = 1

<h3>Liikkeiden ja pokemonien päivittäminen</h3>

Käyttäjä menee etusivulle klikkaamalla yläpalkista "Front Page". Sivulta löytyvissä listoissa jokaisen pokemonin ja liikkeen
kohdalla on "Update" painike. Käyttäjä painaa tuota painiketta siltä riviltä, jossa päivitettävä objekti on. Jos hän päivittää
pokemonia, hän täyttää saman lomakkeen joka on kuvattu kohdassa "Pokemonin lisääminen", jos taas päivitetään liikettä, täyttää
hän lomakkeen, joka on kuvattu kohdassa "Liikkeen lisääminen".

SQL: UPDATE pokemon SET date_modified=CURRENT_TIMESTAMP, name=?, cp=?, iv=?, fastmove_id=?, chargemove_id=?, first_type_id=?, second_type_id=? WHERE pokemon.id = ? VALUES ('Bulbasaur', '500', '50', '1', '2', '5', '1', 1) 

<h3>Liikkeiden ja pokemonien poisto</h3>

Käyttäjä menee etusivulle klikkaamalla yläpalkista "Front Page". Sivulta löytyvissä listoissa jokaisen pokemonin ja liikkeen
kohdalla on "Delete" painike. Tätä painamalla kirjautunut käyttäjä voi poistaa haluamansa objektin. Poistamisessa on kuitenkin
rajoituksia. Koska liikkeen poistaminen poistaa samalla kaikki sen liikkeen omaavat pokemonit, on asetettu rajoitus, että
käyttäjä ei saa poistaa liikkeitä, jotka ovat käytössä muiden pelaajien pokemoneilla. Lisäksi käyttäjä ei voi poistaa muiden
käyttäjien pokemoneja. 

SQL: DELETE FROM move WHERE move.id = 2

Rajoituksien toteutumista varten käytetään myös seuraavia kyselyitä.'

SQL: SELECT name FROM Move WHERE Move.id =:x;

SQL: select * from pokemon where chargemove_id =:x or fastmove_id =:x;

SQL: delete from pokemon where chargemove_id =:x or fastmove_id =:x;

<h3>Statistiikan tutkiminen</h3>

Käyttäjä menee etusivulle klikkaamalla yläpalkista "Front Page". Sivun alaosasta löytyy hieman statistiikkaa. Sieltä löytyy
tietokannan paras pokemon CP arvon ja paras pokemon IV arvon perusteella. Lisäksi, jos käyttäjä on kirjautunut sisään, löytyy
käyttäjän pokemonien yleisin liike.

SQL: select * from pokemon order by cp desc limit 1;

SQL: select * from pokemon order by iv desc limit 1;

SQL: SELECT fastmove_id FROM Pokemon, Account WHERE Pokemon.account_id =:x group by fastmove_id ORDER BY COUNT(*) desc limit 1;

SQL: SELECT chargemove_id FROM Pokemon, Account WHERE Pokemon.account_id =:x group by chargemove_id ORDER BY COUNT(*) desc limit 1;

<h3>PokeStop:ien tarkastelu</h3>

Käyttäjä haluaa tarkastella tietokannasta löytyviä PokeStop:eja. Tällöin hän klikkaa sivun ylälaidasta linkkiä "List of
PokeStops" ja pääsee sivulle, jossa on listattuna kaikki tietokannan stopit taulukkoon. Jos käyttäjä haluaa tutkia tietoja
ja niiden selityksiä tarkemmin hän valitsee haluamansa stopin ja klikkaa siltä riviltä "View" sarakkeen painiketta, joka
ohjaa hänet stopin omalle sivulle. Silloin suoritetaan alla oleva kysely.

SQL: SELECT stop.id AS stop_id, stop.date_created AS stop_date_created, stop.date_modified AS stop_date_modified, stop.name AS stop_name, stop.city AS stop_city FROM stop WHERE stop.id = 1

<h3>PokeStop:ien lisääminen</h3>

Käyttäjä haluaa lisätä uuden stopin tietokantaan. Hän klikkaa yläkulmasta linkkiä "Add a New PokeStop" ja hänet ohjataan 
lomakkeen sivulle. Hän täyttää sivuilla lukevien ohjeiden mukaan kentät ja lähettää alla olevasta painikkeesta lomakkeen, 
jolloin hänet ohjataan sivulle, jossa stopit ovat listattuna ja siellä pitäisi näkyä myös vasta lisätty stop.

SQL: INSERT INTO stop (date_created, date_modified, name, city) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?) VALUES ('Bunkkeri', 'Helsinki')

<h3>PokeStopien päivittäminen</h3>

Käyttäjä haluaa päivittää tietokannasta löytyvää PokeStop:ia. Tällöin hän klikkaa sivun ylälaidasta linkkiä "List of
PokeStops" ja pääsee sivulle, jossa on listattuna kaikki tietokannan stopit taulukkoon. Jos käyttäjä haluaa tutkia tietoja
ja niiden selityksiä tarkemmin hän valitsee haluamansa stopin ja klikkaa siltä riviltä "Update" sarakkeen painiketta, joka
ohjaa hänet edellisessä kohdassa (PokeStopien lisääminen) kuvattuun lomakkeeseen, jonka käyttäjä täyttää sivun ohjeiden mukaan,
jonka jälkeen hänet ohjataan PokeStopit listaavalle sivulle.

SQL: UPDATE stop SET date_modified=CURRENT_TIMESTAMP, name=? WHERE stop.id = ? VALUES ('Kontulan Kirjasto', 2)

<h3>PokeStopien poistaminen</h3>

Käyttäjä haluaa päivittää poistaa jonkin PokeStop:in. Tällöin hän klikkaa sivun ylälaidasta linkkiä "List of
PokeStops" ja pääsee sivulle, jossa on listattuna kaikki tietokannan stopit taulukkoon. Jos käyttäjä haluaa tutkia tietoja
ja niiden selityksiä tarkemmin hän valitsee haluamansa stopin ja klikkaa siltä riviltä "Delete" sarakkeen painiketta, jolloin
stoppi poistuu tietokannasta.

SQL: DELETE FROM stop WHERE stop.id = 2
