class Math {
public:
    int n;
    vector<ll> prime;
    vector<ll> mnPrime;
    vector<vector<ll>> facs;
    vector<vector<ll>> primeFactors;
 
    Math(int n) {
        this -> n = n;
    }
 
    void initPrimeFactors() {
        primeFactors.resize(n + 1);
        for (int x = 2; x <= n; x++) {
            ll i = 2;
            ll y = x;
            while (i * i <= y) {
                ll ok = 0;
                while (y % i == 0) {
                    ok = 1;
                    y /= i;
                }
                if (ok) {
                    primeFactors[x].pb(i);
                }
                i += 1;
            }
            if (y > 1) primeFactors[x].pb(y);
        }
    }
 
    void initPrime() {
        mnPrime.resize(n + 1, n + 1);
        vector<ll> vis(n + 1);
        for (int i = 2; i <= n; i++) {
            if (!vis[i]) {
                prime.pb(i);
                mnPrime[i] = i;
            }
            for (auto p : prime) {
                if (i * p > n) break;
                vis[i * p] = 1;
                mnPrime[i * p] = lmin(mnPrime[i * p], p);
                if (i % p == 0) {
                    break;
                }
            }
        }
    }
 
    void initFactors() {
        facs.resize(n + 1);
        for (int i = 1; i <= n; i++) {
            for (int j = i; j <= n; j += i) {
                facs[j].pb(i);
            }
        }
    }
};