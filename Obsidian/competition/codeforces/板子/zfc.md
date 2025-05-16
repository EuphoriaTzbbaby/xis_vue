class Zfc {
public:
    int n;
    string s;
    vector<int> next;
    vector<int> z;

    Zfc(string s) {
        this -> s = s;
        n = s.size();
    }

    void initNext() {
        next.resize(n);
        ll i = 2, j = 0;
        while (i < n) {
            if (s[i - 1] == s[j]) {
                j += 1;
                next[i] = j;
                i += 1;
            } else if (j == 0) {
                next[i] = 0;
                i += 1;
            } else {
                j = next[j];
            }
        }
    }

    void initZ() {
        z.resize(n);
        ll left = 0, right = 0;
        for (ll i = 1; i < n; i += 1) {
            if (i <= right) {
                z[i] = lmin(z[i - left], right - i + 1);
            }
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
                left = i;
                right = i + z[i];
                z[i] += 1;
            }
        }
    }
};