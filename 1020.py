class Solution:

    def return_cand(self, seed, ly, lx):
        cand = []
        c = (seed[0] - 1, seed[1])
        if c[0] != -1 and c[1] != -1 and c[0] != ly and c[1] != lx:
            cand.append(c)
        c = (seed[0] + 1, seed[1])
        if c[0] != -1 and c[1] != -1 and c[0] != ly and c[1] != lx:
            cand.append(c)
        c = (seed[0],  seed[1] - 1)
        if c[0] != -1 and c[1] != -1 and c[0] != ly and c[1] != lx:
            cand.append(c)
        c = (seed[0],  seed[1] + 1)
        if c[0] != -1 and c[1] != -1 and c[0] != ly and c[1] != lx:
            cand.append(c)
        return cand

    def numEnclaves(self, grid: List[List[int]]) -> int:
        land = set()
        edge_land = set()
        ly, lx = len(grid), len(grid[0])
        for i in range(ly):
            for j in range(lx):
                if grid[i][j] == 1:
                    land.add((i, j))
                    if i == 0 or j == 0 or i == ly - 1 or j == lx - 1:
                        edge_land.add((i, j))
                        land.remove((i,j))

        #print(land, edge_land)

        seeds = list(edge_land)

        while seeds != []:
            sd = self.return_cand(seeds.pop(), ly, lx)
            for i in sd:
                #print(i)
                if i in edge_land or grid[i[0]][i[1]] == 0:
                    continue
                #print("made it")
                land.remove(i)
                edge_land.add(i)
                seeds.append(i)
            if land == set():
                return len(land)
        return len(land)