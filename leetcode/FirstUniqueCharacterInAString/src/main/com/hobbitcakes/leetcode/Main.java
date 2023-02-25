

class Solution {
    public int firstUniqChar(String s) {
        Map d = new HashMap<Character, List<Integer>>();

        for(int i = 0; i < s.length(); i++) {
            char key = s.charAt(i);
            d.putIfAbsent(key, new ArrayList<Integer>());
            d.get(key).add(i);
        }


        for(char c : d.keySet()) {
            if(d.get(c).size() == 1) {
                return d.get(c).get(0);
            }
        }

        return -1;
    }
}