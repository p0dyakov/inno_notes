package ssad.singleton.reader.solution;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class TransitionWords {

    private List<String> dataCollection;
    private static TransitionWords instance;

    private TransitionWords() {
        dataCollection = new ArrayList<>();
        readFile();
    }

    public static TransitionWords getInstance() {
        if (instance == null)
            instance = new TransitionWords();
        return instance;
    }

    private void readFile() {
        try {
            Thread.sleep(5000);
            File myObj = new File("week9/src/main/java/ssad/singleton/reader/transitions.txt");
            try (Scanner myReader = new Scanner(myObj)) {
                while (myReader.hasNextLine()) {
                    String data = myReader.nextLine();
                    dataCollection.add(data);
                }
            }
        } catch (FileNotFoundException | InterruptedException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    /**
     * This method allows to find Random number between range [minValue,maxValue]
     * minValue + rand.nextInt(maxValue - minValue + 1)
     * @return random position string
     */
    public String getRandomTransition() {
        Random rand = new Random();
        return dataCollection.get(rand.nextInt(dataCollection.size() - 1));
    }
}




