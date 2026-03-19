package ssad.singleton.reader.problem;

public class Writer1 {
    public void write() {
        System.out.println("Writer 1 is writing...");
        TransitionWords transitionWords = new TransitionWords();
        System.out.println("\t" + transitionWords.getRandomTransition());
        System.out.println("\tInstance: " + transitionWords);
    }
}
