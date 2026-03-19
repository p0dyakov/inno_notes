package ssad.singleton.reader.problem;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class TransitionWords {
    private List<String> dataCollection;

    // expensive object
    public TransitionWords() {
        dataCollection = new ArrayList<>();
        readFile();
    }

    private void readFile() {
        // simulating a long process, depends on the file size
        try {
            Thread.sleep(3000);
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




