

# Problemvorstellung  (Wordle)


### Erste Einschätzung / Problem / Aufgabenstellung

* Es soll ein Wordle Spiel entwickelt werden, das korrekt, verständlich und regelkonform funktioniert.


### Art des Problems?


Das **Problem** ist ein Logik und Regelproblem. Eingaben müssen geprüft werden und das Spiel muss nach jedem Versuch richtiges Feedback geben, auch bei doppelten Buchstaben

  
### Beschreibung

Der Spieler errät ein Wort mit fünf Buchstaben in maximal sechs Versuchen.
Nach jedem Versuch werden die Buchstaben bewertet als:

* Richtig
* Falsche Position
* Nicht im Wort enthalten

##### Welches Problem hat den grössten Einfluss?

Der grösste Einfluss liegt in der korrekten Bewertungslogik.

### Begründung
* Ist die Bewertung falsch, wirkt das Spiel unfair.
* Ist die Bewertung korrekt, fühlt sich das Spiel wie das echte Wordle an.

##### **Einfaches Beispiel** 

Zielwort: **_APFEL_**

Eingabe: _**ALLEE**_

Das Spiel muss:

- **A** → richtig, richtige Position ✅
    
- **L** → nur einmal als richtig zählen ❗
    
- **E** → richtig, aber nicht doppelt bewerten

**Besonders** wichtig ist der korrekte Umgang mit doppelten Buchstaben sowie mit ungültigen Eingaben.
Das Spiel darf ausschliesslich gültige Wörter aus alphabetischen Buchstaben (A-Z) akzeptieren.
Umlaute (ä, ö, ü), Zahlen sowie Sonderzeichen sind nicht erlaubt und müssen vom Spiel abgewiesen werden.