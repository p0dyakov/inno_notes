package ssad.singleton.reader.solution;

public class Writer1 {
    public void write() {
        System.out.println("Writer 1 is writing");
        System.out.println("\t" + TransitionWords.getInstance().getRandomTransition());
        System.out.println("\tInstance: " + TransitionWords.getInstance());
    }
}
