package WordlePackage;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class WordList {

    private List<String> words;
    private Random random;

    public WordList() {
        words = new ArrayList<>();
        random = new Random();
        loadWordsFromFile();
    }

    private void loadWordsFromFile() {
        try (BufferedReader reader = new BufferedReader(new FileReader("wordlist.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                line = line.trim(); // kleine sicherheit
                if (line.length() == 5) {
                    words.add(line.toLowerCase());
                }
            }
        } catch (IOException e) {
            System.out.println("Fehler beim Laden der Wortliste.");
        }
    }

    public String getRandomWord() {
        if (words.size() == 0) {
            return "";
        }
        int index = random.nextInt(words.size());
        return words.get(index);
    }

    public boolean contains(String word) {
        if (word == null) {
            return false;
        }
        return words.contains(word.toLowerCase());
    }
}