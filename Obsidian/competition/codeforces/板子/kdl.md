struct node {
    ll l, r;
    mutable ll v;
    node(ll L, ll R, ll V) {
        l = L, r = R, v = V;
    }
    bool operator < (const node& o) const {
        return l < o.l;
    }
};
set<node> s;
set<node>::iterator split(ll x) {
    auto it = s.lower_bound(node(x, 0, 0));
    if(it != s.end() && it -> l == x) {
        return it;
    }
    it--;
    ll l = it -> l, r = it -> r, v = it -> v;
    s.erase(it);
    s.insert(node(l, x - 1, v));
    return s.insert(node(x, r, v)).first;
}
void tp(ll l, ll r, ll v) {
    auto itr = split(r + 1);
    auto itl = split(l);
    s.erase(itl, itr);
    s.insert(node(l, r, v));
}