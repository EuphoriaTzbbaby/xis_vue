class Tarjan {

public:

    ll tot = 0;

    ll n = 0;

    ll root = 0;

    vector<vector<ll>> g;

    vector<ll> dfn;

    vector<ll> low;

    vector<ll> isCut;

    vector<pair<ll, ll>> edges;

    Tarjan(vector<vector<ll>> &G) {

        n = G.size();

        g = G;

        dfn.resize(n + 1);

        low.resize(n + 1);

        isCut.resize(n + 1);

    }

    void vecc(ll u, ll fa) {

        tot += 1;

        dfn[u] = low[u] = tot;

        ll son = 0;

        for(auto v : g[u]) {

            if(dfn[v] == 0) {

                son += 1;

                vecc(v, u);

                low[u] = lmin(low[u], low[v]);

                if(low[v] >= dfn[u] && u != root) {

                    isCut[u] = 1;

                }

                if(low[v] > dfn[u]) {

                    edges.pb(mr(u, v));

                }

            } else if(v != fa) {

                low[u] = lmin(low[u], dfn[v]);

            }

        }

        if(son >= 2 && u == root) {

            isCut[u] = 1;

        }

    }

};