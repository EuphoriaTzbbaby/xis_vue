class St {
    vector<ll> nums;
    vector<vector<ll>> st;
    int n;
    St(int _n, vector<ll> _nums) {
        n = _n;
        nums = _nums;
    }
    void init() {
        int p = LOG[n];
        st.resize(n, vector<ll>(p + 1));
        for(int i = 0; i < n; i += 1) {
            st[i][0] = nums[i];
        }
        ll k = 1;
        while(k <= p) {
            for(ll i = 0; i < n - 1; i += 1) {
                ll v = i + (1 << (k - 1));
                if(v < n - 1) {
                    st[i][k] = lmax(st[i][k - 1], st[v][k - 1]);
                } else {
                    st[i][k] = st[i][k - 1];
                }
            }
            k += 1;
        }
    }
    ll query(ll l, ll r) {
        int k = LOG[r - l + 1];
        return lmax(st[l][k], st[r - (1 << k) + 1][k]);
    }
};