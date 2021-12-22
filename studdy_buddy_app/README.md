## Study Buddy App

Aplicatie web pentru studenti prin intermediul careia pot sa isi gaseasca parteneri de studiu.

### Module 
1. Sign up + sign in
2. My Profile 
   * O pagina in care utilizatorul poate sa isi adauge detalii despre ce studiaza, date de contact, mini biografie, interese si specializari
3. Home page 
   * O pagina cu toti utilizatorii unde un utilizator poate sa caute persoane cu care sa lucreze sau care sa ii ofere ajutor
4. Messages
   * O pagina unde un utilizator poate sa vada mesajele primite si poate sa raspunda
5. FAQ / Contact 
   * Utilizatorul poate sa gaseasca un mini tutorial si sa contacteze persoanele de suport pentru a isi rezolva anumite probleme cu aplicatia sau pentru a afla mai multe despre cum pot folosi aplicatia

#### Signup + signin

1. O baza de date cu un tabel cu detaliile utilizatorilor
   * ID, integer
   * First name, text
   * Last name, text
   * Email, text
   * Password, text
   * Faculty ID, integer
2. API Endpoint for signup 
   * primeste detaliile unui utilizator si il inregistreaza in baza de date
3. API Endpoint for signin
   * primeste email + password, verifica daca email exista si daca password e corecta. 
   * returneaza o eroare in caz contrar

#### My profile
1. Un tabel in baza de date sa stocam informatiile despre utilizator
   * ID, integer
   * UserID, integer
   * Facultatea, interger
   * Specialitatea + nivel (stele de la 0 la 5, 0 = fara experienta, 5 = expert), text
     * Algebra liniara 4*
     * Python 2*
     * C++ 1*
     * C# 5*
   * Anul de studiu, integer
   * Email (optional), text
   * Telefon (optional), text

[comment]: <> (   [{"name": "algebra liniara", "level": 5},)
[comment]: <> (   {"name": "matematica", "level": 2}])

2. MyProfile API
   * Editez profilul = endpoint care sa primeasca informatii despre user si sa le salveze in tabelul cu detalii
   * Vad profilul = endpoint care sa extraga din baza de date profilul unui utilizator
