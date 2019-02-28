import snap
from math import floor
from itertools import islice
#Problem 1
g = snap.LoadEdgeList(snap.PNGraph,"p2p-Gnutella08.txt",0,1)
#1.a-e
info_filename = "gnutella_info.txt"
snap.PrintInfo(g,'Gnutella P2P network 2008',info_filename,False)
with open(info_filename,'r') as inf:
    for line in inf:
        print(line)
#Below addresses 1.f,g
g_outdeg = snap.TFltPr64V()
g_indeg = snap.TFltPr64V()
snap.GetOutDegCnt(g,g_outdeg)
snap.GetInDegCnt(g,g_indeg)
#g_outdeg is a vector of pairs of floats. Each pair is addressed like (Val1,Val2)
outdeg_gt_10 = list(filter(lambda x:x.GetVal2() > 10,g_outdeg))
indeg_gt_10 = list(filter(lambda x:x.GetVal2() > 10,g_indeg))
print(f'Nodes with outdegree > 10: {len(outdeg_gt_10)}')
print(f'Nodes with indegree > 10: {len(indeg_gt_10)}')
#Problem 2
so = snap.LoadEdgeList(snap.PNGraph,"stackoverflow-Java.txt")
#2.1
so_wcc = snap.TCnComV()
snap.GetWccs(so,so_wcc)
print(f'# of connected components: {len(so_wcc)}')
#2.2
so_mx_wcc = snap.GetMxWcc(so)
snap.PrintInfo(so_mx_wcc,"Largest connected component of StackOverflow-Java")
#2.3
so_pr = snap.TIntFlt64H()
snap.GetPageRank(so,so_pr)
so_pr.SortByDat(False)#Ascending=False
#The code below might be a naive way to do it 
#Mb try GetKeyV() for hashtable types then just grab top 3 elements
so_pr_ordered = []
so_pr_iter = so_pr.BegI()
while not so_pr_iter.IsEnd():
    so_pr_ordered.append((so_pr_iter.GetKey(),so_pr_iter.GetDat(),))
    so_pr_iter.Next()
print("Top 3 nodes by PageRank (nodeId,PageRank):")
for kv_pair in so_pr_ordered[0:3]:
    print(kv_pair)
#3
#Closeness, and degree centrality take single nodes as input
#Betweenness,Eigenvector and Page rank take a whole graph and return a hashtable
#top5% only
seed = snap.TRnd(1988)
exponent=3
n=400
g_rnd = snap.GenRndPowerLaw(n,exponent)
def all_node_centrality(g,centralityFunc):
    centralities = snap.TIntFlt64H()
    for node in g.Nodes():
        centralities[node.GetId()] = centralityFunc(g,node.GetId())
    return centralities

def iter_kv_pairs(hasht):
    it = hasht.BegI()
    while not it.IsEnd():
        yield it.GetKey(),it.GetDat()
        it.Next()

def build_color_map(hasht,color_name,pct=0.05):
    hasht.SortByDat(False)#sort descending
    keyV = snap.TInt64V()
    num_to_take = floor(hasht.Len()*pct)
    cmap = snap.TIntStrH()
    #islice slices a generator like an array
    for key,val in islice(iter_kv_pairs(hasht),num_to_take):
        cmap[key] = color_name
    return cmap

#draw the graph
#snap.DrawGViz(g_rnd,snap.gvlNeato,"rnd_test.png","Random Network")
deg_centr = all_node_centrality(g_rnd,snap.GetDegreeCentr)
close_centr = all_node_centrality(g_rnd,snap.GetClosenessCentr)
