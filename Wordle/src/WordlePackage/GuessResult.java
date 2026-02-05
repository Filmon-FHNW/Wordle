package WordlePackage;

public class GuessResult {

    // Wort der Spieler geraten hat
    private String guess;

    //  Feedback jeden Buchstaben
    private char[] feedback;

    // konstruktor
    public GuessResult(String guess) {
        this.guess = guess;
        this.feedback = new char[5];
    }

    // Setze Feedback eine Position
    public void setFeedback(int position, char status) {
        feedback[position] = status;
    }

    // holt das geratene Wort
    public String getGuess() {
        return guess;
    }

    // holt feedback für eine Position
    public char getFeedback(int position) {
        return feedback[position];
    }

    // zeigt das ergebnis
    public void printResult() {
        System.out.println("Wort: " + guess);
        System.out.print("Feedback: ");
        for (int i = 0; i < feedback.length; i++) {
            System.out.print(feedback[i] + " ");
        }
        System.out.println();
    }
}
