package ssad.singleton.reader.solution;

public class Writer3 {
    public void write() {
        System.out.println("Writer 3 is writing");
        System.out.println("\t" + TransitionWords.getInstance().getRandomTransition());
        System.out.println("\tInstance: " + TransitionWords.getInstance());
    }
}
