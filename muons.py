#!/usr/bin/env python

from ROOT import TChain, TLorentzVector, TH1F

data = TChain("mini")
data.Add("http://opendata.atlas.cern/release/samples/Data/DataMuons.root")

num_events = data.GetEntries()
print("Number of events = "+str(num_events))

h_mpair = TH1F("mpair", "Invariant mass of lepton pairs", 50, 0, 200)

number_events_to_process = 10000   # Number of events to process
for i_event in range(number_events_to_process):
    data.GetEntry(i_event)
    n_leptons = data.lep_n
    if n_leptons == 2:  # Looking for pairs
        print("Number of leptons = "+str(n_leptons))
        assert(n_leptons==2)
        pt1=data.lep_pt[0]
        eta1 = data.lep_eta[0]
        phi1 = data.lep_phi[0]
        e1 = data.lep_E[0]
        pt2=data.lep_pt[1]
        eta2 = data.lep_eta[1]
        phi2 = data.lep_phi[1]
        e2 = data.lep_E[1]
        p1 = TLorentzVector()
        p2 = TLorentzVector()
        p1.SetPtEtaPhiE(pt1,eta1,phi1,e1)
        p2.SetPtEtaPhiE(pt2,eta2,phi2,e2)
        # Calculates mass of lepton pair
        ppair = p1+p2
        mpair = ppair.M() / 1000 # convert from MeV to GeV
        h_mpair.Fill(mpair)

h_mpair.Draw()
print()
raw_input("Press return to end program")
