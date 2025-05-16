struct node {
    ll l, r;
    ll cnt[21] = {0};
    ll tag;
    ll ok;
    node() {
        tag = 0;
        ok = 0;
    };
} tree[N << 2];

class Segtree {
public:
    vector<node> tree;
    vector<ll> nums;
    ll n;

    Segtree(vector<ll> &nums) {
        n = nums.size() - 1;
        tree.resize(4 * n + 9);
        this -> nums = nums;
    }

    node op(node v1, node v2) {
        node v;
        for(ll i = 0; i <= 20; i += 1) {
            v.cnt[i] = v1.cnt[i] + v2.cnt[i];
        }
        return v;
    }

    void build(ll p, ll pl, ll pr) {
        tree[p].l = pl;
        tree[p].r = pr;
        if(pl == pr) {
            for(ll i = 0; i <= 20; i += 1) {
                tree[p].cnt[i] = (nums[pl] >> i & 1);
            }
            return;
        }
        ll mid = (pl + pr) / 2;
        build(p + p, pl, mid);
        build(p + p + 1, mid + 1, pr);
        node v = op(tree[p + p], tree[p + p + 1]);
        for(int i = 0; i <= 20; i += 1) {
            tree[p].cnt[i] = v.cnt[i];
        }
    }

    void addtag(ll p, ll v) {
        for(ll i = 0; i <= 20; i += 1) {
            if(v >> i & 1) {
                tree[p].cnt[i] = tree[p].r - tree[p].l + 1 - tree[p].cnt[i];
            }
        }
        tree[p].tag ^= v;
        tree[p].ok = 1;
    }

    void push_down(ll p) {
        if(tree[p].ok) {
            addtag(p + p, tree[p].tag);
            addtag(p + p + 1, tree[p].tag);
            tree[p].tag = 0;
            tree[p].ok = 0;
        }
    }

    node query(ll p, ll l, ll r) {
        if(l <= tree[p].l && tree[p].r <= r) {
            return tree[p];
        }
        push_down(p);
        node v;
        ll mid = (tree[p].l + tree[p].r) / 2;
        if(l <= mid) {
            v = op(v, query(p + p, l, r));
        }
        if(mid + 1 <= r) {
            v = op(v, query(p + p + 1, l, r));
        }
        return v;
    }

    void update(ll p, ll l, ll r, ll v) {
        if(l <= tree[p].l && tree[p].r <= r) {
            addtag(p, v);
            return;
        }
        push_down(p);
        ll mid = (tree[p].l + tree[p].r) / 2;
        if(l <= mid) {
            update(p + p, l, r, v);
        }
        if(mid + 1 <= r) {
            update(p + p + 1, l, r, v);
        }
        node vv = op(tree[p + p], tree[p + p + 1]);
        for(ll i = 0; i <= 20; i += 1) {
            tree[p].cnt[i] = vv.cnt[i];
        }
    }
};