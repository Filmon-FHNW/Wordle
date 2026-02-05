package WordlePackage;

public class WordleGame {

    // variablen
    private String geheimesWort;
    private int versucheUebrig;
    private boolean spielVorbei;
    private boolean gewonnen;

    // konstruktor der startet neues Spiel
    public WordleGame(WordList wortListe) {
        this.geheimesWort = wortListe.getRandomWord();
        this.geheimesWort = this.geheimesWort.toUpperCase();
        this.versucheUebrig = 6;
        this.spielVorbei = false;
        this.gewonnen = false;
    }

    // Spieler gibt ein Wort ein
    public GuessResult submitGuess(String guess) {

        // Spiel schon vorbei?
        if (spielVorbei) {
            return null;
        }

        // Mache alles Grossbuchstaben
        guess = guess.toUpperCase();

        // müssen 5 buchstaben sein
        if (guess.length() != 5) {
            return null;
        }

        // erstelle Ergebnis
        GuessResult ergebnis = new GuessResult(guess);

        // Suche richtige Buchstaben an richtiger Stelle
        for (int i = 0; i < 5; i++) {
            if (guess.charAt(i) == geheimesWort.charAt(i)) {
                ergebnis.setFeedback(i, 'C');
            }
        }

        // 2 suche Buchstaben die im Wort sind
        for (int i = 0; i < 5; i++) {

            // Wenn schon richtig dann skip
            if (ergebnis.getFeedback(i) == 'C') {
                continue;
            }

            char buchstabe = guess.charAt(i);
            boolean gefunden = false;

            // search the for secret word
            for (int j = 0; j < 5; j++) {
                if (buchstabe == geheimesWort.charAt(j)) {
                    gefunden = true;
                    break;
                }
            }

            // Setze  Feedback
            if (gefunden) {
                ergebnis.setFeedback(i, 'P');
            } else {
                ergebnis.setFeedback(i, 'A');
            }
        }

        // reduziere Versuche
        versucheUebrig = versucheUebrig - 1;

        // Gewonnen?
        if (guess.equals(geheimesWort)) {
            gewonnen = true;
            spielVorbei = true;
        }

        // Keine Versuche mehr?
        if (versucheUebrig <= 0) {
            spielVorbei = true;
        }

        return ergebnis;
    }

    // getter Methoden
    public boolean isGameOver() {
        return spielVorbei;
    }

    public boolean isWon() {
        return gewonnen;
    }

    public int getAttemptsLeft() {
        return versucheUebrig;
    }

    public String getSecretWord() {
        return geheimesWort;
    }
}