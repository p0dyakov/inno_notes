package ssad.singleton.reader.solution;

public class Writer2 {
    public void write() {
        System.out.println("Writer 2 is writing");
        System.out.println("\t" + TransitionWords.getInstance().getRandomTransition());
        System.out.println("\tInstance: " + TransitionWords.getInstance());
    }
}
