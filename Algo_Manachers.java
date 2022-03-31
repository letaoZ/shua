public int[] calSubstrings(String s) {
    if (s.length() == 0) {
        return new int[0];
    }
    // 存放新的内容
    char[] content = new char[s.length() * 2 + 3];
    // 开头用^
    content[0] = '^';
    // s中的每一个字符要用#包围
    content[1] = '#';
    for (int i = 0; i < s.length(); i++) {
        content[i * 2 + 2] = s.charAt(i);
        content[i * 2 + 3] = '#';
    }
    // 结尾用$
    content[content.length - 1] = '$';

    // 当前的回文串中心下标
    int center = 0;
    // 当前的回文串右边界
    int right = 0;
    // 存储以每一个位置为中心，所能获得的最长回文子串的长度
    int[] maxLength = new int[content.length];
    // 首尾两个字符没有必要计算
    for (int index = 1; index < content.length - 1; index++) {
        // 如果当前求解的位置，在右边界以内
        if (index < right) {
            // 则其最长回文子串的长度，至少为：
            maxLength[index] = Math.min(
                    // 对称center的位置上的
                    maxLength[center * 2 - index],
                    // 或者当前位置到右边界的距离
                    right - index
            );
        }

        // 正常求解，向左右扩展
        while (content[index + (maxLength[index] + 1)] ==
                content[index - (maxLength[index] + 1)]) {
            maxLength[index]++;
        }

        // 如果当前index对应的右边界，比现有的right大
        if (index + maxLength[index] > right) {
            // 更新右边界和中心
            right = index + maxLength[index];
            center = index;
        }
    }

    // 最终的结果
    int[] result = new int[s.length()];
    for (int i = 0; i < s.length(); i++) {
        result[i] = maxLength[i * 2 + 2];
    }
    return result;
}