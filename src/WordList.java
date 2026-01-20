// holt die klasse zufällig um zufall zahlen zu erzeugen
import java.util.Random;

// enthält die wörterliste fürs spiel
public class WordList {


    // array mit allen deutschen Wörtern
    private String[] words = {
            "abend", "acker", "alarm", "alter", "angel", "arten", "autos", "beton",
            "bezug", "blick", "boot", "brand", "buhne", "chance", "decke", "dosis",
            "durst", "ehren", "eisen", "faktor", "feind", "feld", "ferne", "fisch",
            "forum", "front", "frost", "geben", "geist", "geld", "gleis", "gras",
            "gruppe", "hand", "heben", "holz", "hotel", "hund", "irren", "kappe",
            "kauf", "kette", "krise", "licht", "liste", "liter", "lobby", "lupe",
            "markt", "mauer", "milch", "mitte", "monat", "motor", "nacht", "nutzen",
            "opfer", "orden", "paket", "pause", "pfand", "phase", "preis", "quote",
            "radio", "raum", "reich", "regel", "reise", "ringe", "rolle", "salat",
            "sehen", "seife", "seite", "szene", "stand", "stern", "strom", "tasse",
            "thema", "timer", "traum", "trend", "trocken", "union", "uralt", "wagen",
            "werts", "wiese", "wolke", "worter", "zaun", "zelt", "zonen", "zweck"
    };

    public String getRandomWord() {
        Random random = new Random();
        int position = random.nextInt(words.length);
        return words[position];
    }
}