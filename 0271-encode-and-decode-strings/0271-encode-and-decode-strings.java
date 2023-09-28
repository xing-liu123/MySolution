public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String str : strs) {
            sb.append("/").append(str.length()).append("/").append(str);
        }

        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
       
        List<String> list = new ArrayList<>();

        int i = 0, n = s.length();
        while(i < n) {
            int idx_start = s.indexOf('/', i);
            int idx_end = s.indexOf('/', i + 1);

            int len = Integer.valueOf(s.substring(idx_start + 1, idx_end));
            list.add(s.substring(idx_end + 1, idx_end + len + 1));
            i = idx_end + len + 1;
        }

        return list;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));