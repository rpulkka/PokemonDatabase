<h2>Aihemäärittely</h2>

Nimensä mukaisesti projektin aihe on Pokemon GO peliin liittyvä tietokantasovellus. Pääpiirteissään tietonkantasovellus tulee 
toimimaan s.e. kouluttajat (trainer) voivat lisätä tietokantaan omia Pokemon olioita, joita voidaan sitten verrata erinäisillä
tietokantahauilla. Pokemonien ominaisuuksia ovat esimerkiksi niiden taisteluvoima (CP / combat points), liikkeet (move),
tyyppi (type) ja potentiaali (IV / individual value). Jo näiden pohjalta saa tehtyä mielenkiintoisia tietokantakyselyitä, esim.
millä kouluttajalla on suurimman taisteluvoiman omaava Pokemon, millä tietokannan Pikachu oliolla on suurin potentiaali, minkä
tyyppisiä Pokemoneja tietyllä kouluttajalla on eniten, mikä on yleisin liike, ja niin edelleen. Tietokantatauluja olisivat siis 
vähintään kouluttaja, pokemon ja liikkeet. Luultavasti myös tyypistä on järkevää toteuttaa tietokantataulu, vaikka niitä onkin
rajattu määrä (noin 15). Taisteluvoima ja potentiaali sen sijaan ovat Pokemoniin liittyviä lukuarvoja. Tietokantakaaviossa 
olisi siis yhdestä moneen yhteys kouluttajan ja pokemonien välille, ja pokemonilla on aina kaksi liikettä, fast attack ja 
charged attack, jotka olisivat sitten liikkeen tyyppinä. Pokemoniin liittyy sen lisäksi yksi tai kaksi tyyppiä ja kaksi 
integer attribuuttia, jotka ovat taisteluvoima ja potentiaali. Työhön on helppo lisätä uusiakin ominaisuuksia, jos jää aikaa ja 
samoin osan ominaisuuksista voi jättää pois ja silti saada aikaan toimiva työ.
