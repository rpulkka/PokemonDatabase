<h1>Käyttötapaukset</h1
  
<h3>Käyttäjätunnuksen luominen</3>

Jos käyttäjällä ei ole vielä tunnusta, hän klikkaa yläpalkista "Sign in", jolloin avautuu lomake. Lomakkeeseen kirjoitetaan uusi
käyttäjätunnus sekä salasana, jonka jälkeen lomake lähetetään alla olevasta painikkeesta. 

<h3>Sisäänkirjautuminen</h3>

Kun käyttäjällä on tunnukset, hän klikkaa yläpalkista "Log in" ja syöttää avautuneeseen lomakkeeseen käyttäjätunnuksen ja salasanan
ja painaa alla olevaa lähetyspainiketta. Jos tunnukset ovat oikein, käyttäjä ohjataan etusivulle, jolloin hän pääsee käsiksi
tietokannan muokkaamiseen. 

<h3>Liikkeiden lisääminen</h3>

Käyttäjä haluaa lisätä uuden liikkeen tietokantaan. Tällöin hän valitsee yläpalkista linkin "Add a New Move" ja pääsee Moven
lisäämiseen tarkoitettuun lomakkeeseen. Lomakkeeseen syötetään ensin nimi tekstikenttään ja liikkeen tuottama "vahinko" eli
damage numeroina tekstikenttään. Tämän jälkeen klikataan rasti "charged" ruutuun jos liike on charge -tyyppinen. Sitten bars
-kenttään käyttäjän kirjoittaa '0' mikäli liike on "fast" tyyppinen ja muulloin kirjoitetaan numeroina ns. palkkien lukumäärä,
joka on lukuarvo noin yhdestä kuuteen. Lomake lähetetään alla olevasta painikkeesta, jolloin isku lisätään tietokantaan. 

<h3>Pokemonin lisääminen</h3>

Käyttäjä haluaa lisätä uuden Pokemonin tietokantaan. Tällöin hän klikkaa sivun yläpalkista linkkiä "Add a New Pokemon" ja pääsee
lomakesivulle. Lomakesivulla hän kirjoittaa tekstikenttiin ensin nimen merkkijonona ja sitten CP arvon (10-4500) ja IV arvon 
(0-100) lukuna. Sitten valitaan dropdown valikoista fastmove ja chargemove. Huomaa, että liikkeiden täytyy olla tietokannassa,
ennen kuin lisäät pokemonia, eli jos haluat käyttää liikkeitä, joita ei ole vielä tietokannassa, katso kohta "Liikkeiden 
lisääminen". Sitten valitaan dropdown menusta Pokemonille kaksi tyyppiä. Jos pokemonilla on vain yksi tyyppi, valitse toisen
tyypin valinnassa "empty". Lopuksi hän klikkaa "Submit" -otsikon alla olevaa painiketta. Tällöin käyttäjä uudelleenohjataan
etusivulle, jossa on listaus kaikista Pokemoneista ja lisätyn Pokemonin tulisi nyt löytyä listasta.

<h3>Pokemonien tarkastelu</h3>

Käyttäjä haluaa tarkastella Pokemonien listaa. Tällöin hän klikkaa sivun yläpalkista linkkiä "Front Page", jolloin hänet ohjataan
etusivulle, jossa on kaikki Pokemonit listattuna. "Name" -sarakkeessa on Pokemonin nimi, "CP" -sarakkeessa Combat Points -arvo ja
"IV" -sarakkeessa Individual Value -arvo. "Fast Move" ja "Charge Move" -sarakkeista löytyy pokemonin liikkeiden nimet. "Type 1"
ja "Type 2" -sarakkeista löytyy pokemonin molemmat tyypit.

<h3>Liikkeiden tarkastelu</h3>

Käyttäjä haluaa tarkastella liikkeiden listaa. Tällöin hän klikkaa sivun yläpalkista linkkiä "Front Page", jolloin hänet ohjataan
etusivulle, jossa on kaikki tietokannan liikkeet listattuna, pokemonien listan alapuolella. "Name" -sarakkeessa on liikkeen nimi.
"Damage" -sarakkeessa on iskun tuottama vahinko pisteinä. Jos liike on charge -tyyppinen, vahinko on ilmoitettu per bar tyyliin,
esim. jos bareja eli palkkeja olisi 2 ja damagen määräksi on ilmoitettu 90, vahinko on 90 per käytetty palkki. "Is Charged" 
-sarake ilmoittaa onko liike charged -tyyppinen (true) vai fast -tyyppinen (false). "Bars" -sarake ilmoittaa palkkien määrän,
jonka tulisi olla 0 kaikilla fast moveilla. 

<h3>Liikkeiden ja pokemonien päivittäminen</h3>

Käyttäjä menee etusivulle klikkaamalla yläpalkista "Front Page". Sivulta löytyvissä listoissa jokaisen pokemonin ja liikkeen
kohdalla on "Update" painike. Käyttäjä painaa tuota painiketta siltä riviltä, jossa päivitettävä objekti on. Jos hän päivittää
pokemonia, hän täyttää saman lomakkeen joka on kuvattu kohdassa "Pokemonin lisääminen", jos taas päivitetään liikettä, täyttää
hän lomakkeen, joka on kuvattu kohdassa "Liikkeen lisääminen".

<h3>Liikkeiden ja pokemonien poisto</h3>

Käyttäjä menee etusivulle klikkaamalla yläpalkista "Front Page". Sivulta löytyvissä listoissa jokaisen pokemonin ja liikkeen
kohdalla on "Delete" painike. Tätä painamalla kirjautunut käyttäjä voi poistaa haluamansa objektin.

