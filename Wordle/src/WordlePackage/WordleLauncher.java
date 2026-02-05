package WordlePackage;

import java.util.Scanner;
import WordlePackage.ui.ConsoleUI;
import WordlePackage.ui.JavaFXUI;

public class WordleLauncher {
    public static void main(String[] args) {

        String choice;
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Wordle Starter");
            System.out.println("1) Konsole");
            System.out.println("2) JavaFX");
            System.out.print("Auswahl: ");
            choice = sc.nextLine().trim();
        }

        if (choice.equals("2")) {
            JavaFXUI.launch(JavaFXUI.class);
        } else {
            if (!choice.equals("1")) {
                System.out.println("Ungültige Auswahl. Konsole wird gestartet...");
            }
            WordList wordList = new WordList();
            WordleGame game = new WordleGame(wordList);
            WordleValidator validator = new WordleValidator(wordList);
            ConsoleUI ui = new ConsoleUI(game, validator);
            ui.start();
        }
    }
}