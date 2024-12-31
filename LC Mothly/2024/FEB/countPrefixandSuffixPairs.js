var countPrefixandSuffixPairs = function (words) {
    const n = words.length;
    let c = 0;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const s1 = words[i];
            const s2 = words[j];
            if (s2.startsWith(s1) && s1.endsWith(s2)) {
                c++;
            }
        }
    }
    return c;
};