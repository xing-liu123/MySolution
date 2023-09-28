public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String str : strs) {
            sb.append("/" + str.length() + "/");
            sb.append(str);
        }

        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        StringBuilder sb = new StringBuilder(s);
        List<String> list = new ArrayList<>();

        while(!sb.isEmpty()) {
            if (sb.charAt(0) == '/') {
                sb.deleteCharAt(0);
                String num = "";
                while (sb.charAt(0) != '/') {
                    num += sb.charAt(0);
                    sb.deleteCharAt(0);
                }
                sb.deleteCharAt(0);
                int len = Integer.valueOf(num);
                list.add(sb.substring(0, len));
                sb.delete(0, len);
            }
        }

        return list;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));