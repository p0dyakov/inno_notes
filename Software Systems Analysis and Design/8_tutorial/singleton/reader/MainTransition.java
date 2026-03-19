package ssad.singleton.reader;

// Without singleton
//import ssad.singleton.reader.problem.Writer1;
//import ssad.singleton.reader.problem.Writer2;
//import ssad.singleton.reader.problem.Writer3;

// With singleton
import ssad.singleton.reader.solution.Writer1;
import ssad.singleton.reader.solution.Writer2;
import ssad.singleton.reader.solution.Writer3;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class MainTransition {

    public static void main(String[] args) {
        System.out.print("Program started at " );
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("HH:mm:ss");
        System.out.println(dtf.format(LocalDateTime.now()));
        Writer1 writer1 = new Writer1();
        writer1.write();
        Writer2 writer2 = new Writer2();
        writer2.write();
        Writer3 writer3 = new Writer3();
        writer3.write();
        System.out.print("Program finished at ");
        System.out.println(dtf.format(LocalDateTime.now()));
    }
}
