import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;


/**
 * Created by Yusuf on 2017-08-03.
 */
public class Parse {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String line;
        String data = null;
        BufferedReader br = null;
        String delim = "[-]";
        String delim2 = "[;]+";
        String placeholder = "placeholder";
        StringBuilder buffer = new StringBuilder();
        String[] tokens;
        int add = 0;
        int i = 0;
        try {
            br = new BufferedReader(new FileReader("//Users//Yusuf//Desktop//" + scanner.next()));
        } catch (FileNotFoundException fnfex) {

            System.out.println(fnfex.getMessage() + "The file was not found");
            System.exit(0);
        }

        try {
            while ((line = br.readLine()) != null) {
                 data = line;
                 tokens = data.split(delim);

                 buffer.append(tokens[0]);
                 buffer.append(";");
                 buffer.append(tokens[1]);
                 buffer.append(";");
                 buffer.append(tokens[2]);
                 buffer.append(";");
            }

            data  = buffer.toString();
            tokens = data.split(delim2);
            System.out.println(tokens[1]);

        } catch (IOException ioex) {
            System.out.println(ioex.getMessage() + "Error reading file");
        }
        finally {

            System.exit(0);
        }
    }
}
