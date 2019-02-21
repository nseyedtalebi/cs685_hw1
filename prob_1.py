import snap
g = snap.LoadEdgeList(snap.PNGraph,"p2p-Gnutella08.txt",0,1)
#1.a
node_cnt = len(list(g.Nodes()))
#1.b

g_outdeg = snap.TFltPr64V()
g_indeg = snap.TFltPr64V()
snap.GetOutDegCnt(g,g_outdeg)
snap.GetInDegCnt(g,g_indeg)