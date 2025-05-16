class FunctionalGraph {
    public:
        ll loopCnt;
        ll n;
        vector<ll> d;
        vector<ll> pos;
        vector<ll> dist;
        vector<ll> eachLoopSize;
        vector<ll> joinPoint;
    FunctionalGraph(vector<ll> a) {
        loopCnt = 0;
        d = a;
        n = d.size();
        pos.resize(n, -1);
        dist.resize(n, 0);
        joinPoint.resize(n);
        findLoop();
    }
    bool localLoop(int x) {
        return dist[x] == 0;
    }
    void findLoop() {
        vector<ll> f;
        for(int i = 0; i < n; i += 1) {
            if(pos[i] != -1) continue;
            int cur = i;
            while(pos[cur] == -1) {
                pos[cur] = loopCnt;
                f.pb(cur);
                cur = d[cur];
            }
            if(pos[cur] < loopCnt) {
                // cout << cur << " " << loopCnt << endl;
                // 没构成新环
                int jp = cur;
                for(int j = 0; j < f.size(); j += 1) {
                    // cout << f[j] << " " << loopCnt << " " << 888 << endl;
                    pos[f[j]] = pos[cur];
                    joinPoint[f[j]] = cur;
                    dist[f[j]] = f.size() - j + dist[cur];
                }
                f.clear();
            } else {
                // cout << cur << " " << loopCnt << " 999" << endl;
                // 构成新环
                int ok = 0;
                int id = 0;
                for(int j = 0; j < f.size(); j += 1) {
                    if(f[j] == cur) {
                        ok = 1;
                        id = j;
                        eachLoopSize.pb(f.size() - j);
                    }
                    pos[f[j]] = loopCnt;
                    if(ok) {
                        joinPoint[f[j]] = f[j];
                        dist[f[j]] = 0;
                    } else {
                        joinPoint[f[j]] = cur;
                        // dist[f[j]] = 
                    }
                }
                for(int j = 0; j < id; j += 1) {
                    dist[f[j]] = id - j;
                }
                f.clear();
                loopCnt += 1;
            }
        }
    }
    void display() {
        cout << "loopCnt = " << loopCnt << endl;
        for(int i = 0; i < loopCnt; i += 1) {
            cout << eachLoopSize[i] << " ";
        }
        cout << endl;
        cout << "-------" << endl;
        for(int i = 0; i < n; i += 1) {
            cout << "i = " << i << " joinPoint = " << joinPoint[i] << " pos[i] = " << pos[i] << " dist[i] = " << dist[i] << endl;
        }
    }
};