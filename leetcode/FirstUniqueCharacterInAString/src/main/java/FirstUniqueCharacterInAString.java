import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FirstUniqueCharacterInAString {
        public int firstUniqChar(String s) {
            Map d = new HashMap<Character, ArrayList<Integer>>();

            for(int i = 0; i < s.length(); i++) {
                char key = s.charAt(i);
                d.putIfAbsent(key, new ArrayList<Integer>());
                ArrayList<Integer> l = d.get(key);

            }


            for(Character c : d.keySet()) {
                if(d.get(c).size() == 1) {
                    return d.get(c).get(0);
                }
            }

            return -1;
        }
}
