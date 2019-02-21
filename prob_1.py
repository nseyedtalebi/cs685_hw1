import snap
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
