# Veji Multimedia Database
by Joona & Lauri. TKK:n ohjelmoinnin harjoitustyö marraskuussa 2018.

## Ohjelman kuvaus
- kyseessä on oma aihe, joka vastaa laajudeltaan muita harjoitustyöaiheita
- ohjelma toimii Googlen AppEngine -palvelimella ja hyädyntää Pythonin lisäksi seuraavia
  teknologioita: HTML, XML, Javascript, CSS
- ohjelma on käytettävissä mistä päin maailmaa tahansa
- ohjelman tarkoitus on toimia käyttäjilleen ensisijaisesti elokuvatietokantana,
  jonne voi lisätä kaikki ne elokuvat, jotka omistaa tai on joskus nähnyt

## Ohjelman käyttöohje
- kirjaudu sisään http://veji.appspot.com/ omalla Google ID:lläsi
- voit lisätä elokuvia kohdasta "Add a new movie"
- elokuvan poistaminen omasta listasta onnistuu valitsemalla elokuvan (klikkaa
  valintaboksia) ja valitsemalla "Delete"
- elokuvien järjestäminen eri kriteerien mukaan implementoidaan, jos jaksetaan

## Ratkaisutapa
- elokuvien tiedot haetaan suoraan IMDB:stä
- IMDB:stä saatu data parsitaan tietokantaan tallennettavaksi rakenteeksi
- kaikkien elokuvien kaikki tiedot poster-kuvaa lukuunottamatta 
- tiedot sijaitsevat Google App Enginen tarjoamassa Datastore-tietokantapilvessä
  

## Arvio projektityöstä
- kerrankin tehtiin jotain hyädyllistä ohjelmointikurssilla
- aikataulu oli tiukka, mutta saatiin tää valmiiksi
- ohjelman erityinen ansio on se, että se on toteutettu olemassa olevan 
  palvelun päälle ja että se on täysin käytettävissä internet-yhteyden yli
- ohjelma käyttää lukuisia eri tekniikoita kokonaisuuden aikaansaamiseksi


## Lähdeviitteet
- Pythonilla tehty Tasklist
- Perl-skripti IMDB-tiedon parsimiseen
- Google App Engine API:t


## Parannusehdotuksia
- tehokkuus huono
-- jos uusi elokuva jo listassa/db:ssä, ei lähdetä etsimään sitä imdb:stä
-- "reaaliaikainen" haku vain jo löydettyihin tuloksiin (käyttäjän
   kirjoittaessa elokuvahakuun haetaan jo ensimmäisellä haulla löydetyistä
   tuloksista eikä tehdä aina uutta hakua imdb:hen)
- oman databasen kentät voisivat olla myös jotain muuta kuin stringejä
- interfacet olis kivoja, mutta python ei tue niitä  
