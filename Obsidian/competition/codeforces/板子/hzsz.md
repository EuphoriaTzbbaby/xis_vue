class Hzsz {
public:
    string s;
    vector<pair<char, ll>> nums;
    vector<ll> p, c;
    vector<ll> lcp;
    int n;

    Hzsz(string s) {
        this -> s = s;
        s += '$';
        n = s.size();
    }

    void initP() {
        nums.resize(n);
        p.resize(n);
        c.resize(n);
        fw(i, 0, n) {
            nums[i] = mr(s[i], i);
        }
        sort(nums.begin(), nums.end());
        fw(i, 0, n) {
            p[i] = nums[i].se;
        }
        c[p[0]] = 0;
        fw(i, 1, n) {
            if (nums[i].fi == nums[i - 1].fi) {
                c[p[i]] = c[p[i - 1]];
            } else {
                c[p[i]] = c[p[i - 1]] + 1;
            }
        }
        ll k = 0;
        while ((1 << k) < n) {
            vector<pair<pair<ll, ll>, ll>> nums(n);
            fw(i, 0, n) {
                nums[i] = mr(mr(c[i], c[(i + (1 << k)) % n]), i);
            }
            sort(nums.begin(), nums.end());
            fw(i, 0, n) {
                p[i] = nums[i].se;
            }
            c[p[0]] = 0;
            fw(i, 1, n) {
                if (nums[i].fi == nums[i - 1].fi) {
                    c[p[i]] = c[p[i - 1]];
                } else {
                    c[p[i]] = c[p[i - 1]] + 1;
                }
            }
            k += 1;
        }
    }

    void initLcp() {
        lcp.resize(n);
        int k = 0;
        fw(i, 0, n - 1) {
            ll pi = c[i];
            ll j = p[pi - 1];
            while (s[i + k] == s[j + k]) {
                k += 1;
            }
            lcp[pi] = k;
            k = lmax(0, k - 1);
        }
    }
};