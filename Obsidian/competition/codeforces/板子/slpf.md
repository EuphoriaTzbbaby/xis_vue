class Slpf {
public:
    int n, tot;
    vector<ll> dfn;
    vector<ll> a;
    vector<ll> nums;
    vector<vector<ll>> g;
    vector<ll> sz;
    vector<ll> dep;
    vector<ll> top;
    vector<ll> pa;
    vector<ll> son;

    Slpf(int n, vector<ll> &a, vector<vector<ll>> &g) {
        tot = 0;
        this -> n = n;
        this -> a = a;
        this -> g = g;
        sz.resize(n + 1);
        dep.resize(n + 1);
        top.resize(n + 1);
        pa.resize(n + 1);
        son.resize(n + 1);
        dfn.resize(n + 1);
        nums.resize(n + 1);
    }

    void dfs1(ll u, ll fa) {
        dep[u] = dep[fa] + 1;
        pa[u] = fa;
        sz[u] = 1;
        ll x = 0;
        for (auto v : g[u]) {
            if (v != fa) {
                dfs1(v, u);
                sz[u] += sz[v];
                if (x < sz[v]) {
                    son[u] = v;
                    x = sz[v];
                }
            }
        }
    };

    void dfs2(ll u, ll t) {
        dfn[u] = ++tot;
        nums[tot] = a[u];
        top[u] = t;
        if (son[u] == 0) return;
        dfs2(son[u], t);
        for (auto v : g[u]) {
            if (v != son[u] && v != pa[u]) {
                dfs2(v, v);
            }
        }
    }
};