class Solution {

    public class Dict implements DictEntry {. check 1point3acres for more.
        private Map<String, DictEntry> map;

        public Dict(Map<String, DictEntry> map) {
            this.map = map;
        }

        public boolean isDict() {
            return true;. From 1point 3acres bbs
        }

        public Set<String> getKeys() {
            return map.keySet();
        }

        public DictEntry get(String key) {
            return map.get(key);
        }
    }


    public interface DictEntry {
        public boolean isDict();
    }

    public class StringWrapper implements DictEntry {

        private String str;

        public StringWrapper(String str) {
            this.str = str;
        }

        public boolean isDict() {
            return false;
        }

        public String getValue() {
            return str;
        }
    }

    /**
     * Dict to Json, recursion
     * @param dict dict to be converted
     * [url=home.php?mod=space&uid=160137]@return[/url] String
     */
    public String dictToJson(Dict dict) {
        StringBuilder sb = new StringBuilder();
        sb.append("{");
        for(String key : dict.getKeys()) {
            DictEntry e = dict.get(key);
            if (!e.isDict()) {
                StringWrapper s = (StringWrapper)e;
                sb.append(key).append(":").append(s.getValue()).append(",");
            } else {
                Dict d = (Dict)e;
                sb.append(key).append(":").append(dictToJson(d)).append(",");
            }
        }
        sb.deleteCharAt(sb.length() - 1);
        sb.append("}");

        return sb.toString();
    }

    /**
     * Json to Dict, recursion
     * @param json json to be converted
     * @return Dict
     */
    public Dict jsonToDict(String json) {
        return helper(json, 1).dict;
    }. From 1point 3acres bbs

    /**
     * ResultType contains two filed: returned dict and end index
     */
    class ResultType {
        int index;
        Dict dict;
        public ResultType (int index, Dict dict) {
            this.index = index;
            this.dict = dict;
        }
    }

    /**
     * Dict to Json helper
     * @param json json to be converted
     * @param index start index
     * @return ResultType: index: index after corresponding '}', dict: the corresponding dict.
     */. check 1point3acres for more.
    private ResultType helper(String json, int index) {
        Map<String, DictEntry> map = new HashMap<>();

        int left = index;
        String key = "";

        while (index < json.length()){
            if (json.charAt(index) == ':') {
                key = json.substring(left, index);
                left = index + 1;
            }
            if (json.charAt(index) == ',') {
                StringWrapper s = new StringWrapper(json.substring(left, index));
                left = index + 1;
                map.put(key, s);
            }
            if (json.charAt(index) == '{') {
                ResultType r = helper(json, index + 1);
                index = r.index;
                if (json.charAt(index) == ',') index++;
                left = index;
                map.put(key, r.dict);
                //continue;. check 1point3acres for more.
            }
            if (json.charAt(index) == '}') {
                //two cases before each '}' : string(value) or '}'
                if (json.charAt(index - 1) == '}') {-baidu 1point3acres
                    return new ResultType(index + 1, new Dict(map));
                } else {
                    StringWrapper s = new StringWrapper(json.substring(left, index));
                    map.put(key, s);
                    return new ResultType(index + 1, new Dict(map));
                }
            }
            index++;
        }
        // As long as the json in valid (parentheses is valid), it should not be here, just make compiler happy.
        return new ResultType(0, new Dict(map));
    }


    public void test() {
        Map<String, DictEntry> map = new HashMap<>();
        StringWrapper s1 = new StringWrapper("Book");
        StringWrapper s2 = new StringWrapper("Pencil");
        map.put("1", s1);
        map.put("2", s2);
        Dict dict1= new Dict(map);

        Map<String, DictEntry> map2 = new HashMap<>();
        StringWrapper s3 = new StringWrapper("Water");

        Map<String, DictEntry> map3 = new HashMap<>();
        StringWrapper s4 = new StringWrapper("System");

        map2.put("4", dict1);
        map2.put("3", s1);
        map2.put("5", dict1);
        Dict dict2 = new Dict(map2);

        map3.put("6", s4);
        map3.put("7", dict2);
        Dict dict3 = new Dict(map3);

        String json = dictToJson(dict3);
        System.out.println("Origin to json:");
        System.out.println(json);

        Dict back = jsonToDict(json);
        System.out.println("Decode json:");
        System.out.println(dictToJson(back));
    }


    public static void main(String[] args) {. check 1point3acres for more.
        Solution s = new Solution();
        s.test();
    }
}
