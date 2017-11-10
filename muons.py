#!/usr/bin/env python

from ROOT import TChain, TLorentzVector, TH1F

def four_momentum(i_lepton, tree):
    pt = tree.lep_pt[i_lepton]
    eta = tree.lep_eta[i_lepton]
    phi = tree.lep_phi[i_lepton]
    E = tree.lep_E[i_lepton]
    p = TLorentzVector()
    p.SetPtEtaPhiE(pt,eta,phi,E)
    return p

def leptons_from_event(tree):
    '''
    Gets list of leptons as particle objects
    '''
    leptons = []
    n_leptons = data.lep_n
    for i_lepton in range(n_leptons):
        p = four_momentum(i_lepton, tree)
        q = tree.lep_charge[i_lepton]
        particle = Particle(p, q)
        leptons.append(particle)
    return leptons

def pairs_from_particles(particles):
    pairs = []
    n_particles = len(particles)
    for i in range(n_particles-1):
        charge_i = particles[i].q
        for j in range(i+1, n_particles):
            charge_j = particles[j].q
            pair = (particles[i], particles[j])
            if charge_i != charge_j:
                pairs.append(pair)
    return pairs

def mass_of_pairs(pair):
    p1 = pair[0].p
    p2 = pair[1].p
    ppair = p1 + p2
    return ppair.M()

class Particle:
    def __init__(self, p, q):
        self.p = p
        self.q = q

if __name__ == '__main__':
    data = TChain("mini")
    data.Add("http://opendata.atlas.cern/release/samples/Data/DataMuons.root")    

    h_mpair = TH1F("mpair", "Invariant mass of lepton pairs", 50, 0, 200)

    number_events_to_process = 10000   # Number of events to process
    for i_event in range(number_events_to_process):
        data.GetEntry(i_event)
        n_leptons = data.lep_n
        if n_leptons >= 2:  # Looking for pairs
            leptons = leptons_from_event(data)
            pairs = pairs_from_particles(leptons)
            # Calculates mass of lepton pair
            for pair in pairs:
                mpair = mass_of_pairs(pair) / 1000 # convert from MeV to GeV
                h_mpair.Fill(mpair)

    h_mpair.Draw()
    print()
    raw_input("Press return to end program")
