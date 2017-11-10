#!/usr/bin/env python

from ROOT import TChain
from ROOT import TLorentzVector
data = TChain("mini")
data.Add("http://opendata.atlas.cern/release/samples/Data/DataMuons.root")

num_events = data.GetEntries()
print("Number of events = "+str(num_events))

number_events_to_process = 1000   # Number of events to process
for i_event in range(number_events_to_process):
    data.GetEntry(i_event)
    n_leptons = data.lep_n
    if n_leptons >= 2:  # Looking for pairs
        print("Number of leptons = "+str(n_leptons))
        assert(n_leptons==2)
        pt1=data.lep_pt[0]
        eta1 = data.lep_eta[0]
        phi1 = data.lep_phi[0]
        e1 = data.lep_E[0]
        pt2=data.lep_pt[1]
        print("Lepton Pts are: "+str(pt1)+", "+str(pt2))
        p1 = TLorentzVector()
        p1.SetPtEtaPhiE(pt1,eta1,phi1,e1)
        print ("First lepton Pt from vector = "+str(p1.Pt()))
