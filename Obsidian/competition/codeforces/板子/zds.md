struct node {
    vector<node*> son;
    vector<ll> cnt;
    node() {
        son.resize(2);
        cnt.resize(2);
        son[0] = son[1] = nullptr;
        cnt[0] = cnt[1] = 0;
    }
};
class Trie {
    public:
    node* root;
    int tot;
    Trie() {
        root = new node();
        tot = 0;
    }
    void insert(ll x) {
        tot += 1;
        node* cur = root;
        for(int i = 33; i >= 0; i -= 1) {
            int bit = (x >> i) & 1;
            if(cur -> son[bit] == nullptr) {
                cur -> son[bit] = new node();
            }
            cur -> cnt[bit] += 1;
            cur = cur -> son[bit];
        }
    }
    void erase(ll x) {
        tot -= 1;
        node* cur = root;
        for(int i = 33; i >= 0; i -= 1) {
            int bit = (x >> i) & 1;
            cur -> cnt[bit] -= 1;
            cur = cur -> son[bit];
        }
    }
    ll query(ll x) {
        if(tot == 0) return 0;
        node* cur = root;
        ll res = 0;
        for(int i = 33; i >= 0; i -= 1) {
            int bit = (x >> i) & 1;
            // 找 0 
            if(bit) {
                if(cur -> son[0] == nullptr || cur -> cnt[0] == 0) {
                    res = res * 2;
                    cur = cur -> son[1];
                } else {
                    res = res * 2 + 1;
                    cur = cur -> son[0];
                }
            } else {
                if(cur -> son[1] == nullptr || cur -> cnt[1] == 0) {
                    res = res * 2;
                    cur = cur -> son[0];
                } else {
                    res = res * 2 + 1;
                    cur = cur -> son[1];
                }
            }
        }
        return res;
    }
};