``` c++
class Dsu {
public:
    int n;
    vector<ll> s;
    Dsu(int n) {
        this -> n = n;
        s.resize(n + 1);
        fw(i, 0, n + 1) s[i] = i;
    }
    ll find(ll x) {
        if(x != s[x]) {
            s[x] = find(s[x]);
        }
        return s[x];
    }
    bool same(ll x, ll y) {
        return find(x) == find(y);
    }
    void merge(ll x, ll y) {
        ll fax = find(x), fay = find(y);
        s[fax] = fay;
    }
};
```
```