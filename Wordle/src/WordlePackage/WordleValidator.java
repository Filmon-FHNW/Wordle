package WordlePackage;

public class WordleValidator {

    private WordList wordList;

    public WordleValidator(WordList wordList) {
        this.wordList = wordList;
    }

    public boolean isValid(String input) {
        if (input == null) {
            return false;
        }

        input = input.trim();

        if (input.length() != 5) {
            return false;
        }

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (!Character.isLetter(c)) {
                return false;
            }
        }

        input = input.toLowerCase();

        return wordList.contains(input);
    }
}
