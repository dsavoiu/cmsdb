# coding: utf-8

"""
HH -> bbtautau datasets for the 2022 postEE data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_uhh_v12 import campaign_run3_2022_postEE_nano_uhh_v12 as cpn  # noqa


#
# ggF -> H -> HH
#

# SM
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_powheg",
    id=14853029,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=3_047_884,
    aux={
        "merging_factors": {
            "nominal": 54,
        },
    },
)

# different couplings, keeping c2 = 0

#cpn.add_dataset(
#    name="hh_ggf_hbb_htt_kl0_kt1_powheg",
#    # MISSING
#)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl2p45_kt1_powheg",
    id=14952632,
    processes=[procs.hh_ggf_hbb_htt_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=3_435_020,
    aux={
        "merging_factors": {
            "nominal": 61,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl5_kt1_powheg",
    id=15050396,
    processes=[procs.hh_ggf_hbb_htt_kl5_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=3_074_020,
    aux={
        "merging_factors": {
            "nominal": 39,
        },
    },
)

# different bsm couplings, with c2 != 0
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl0_kt1_c21_powheg",
    id=14791033,
    processes=[procs.hh_ggf_hbb_htt_kl0_kt1_c21],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100_000,
    aux={
        "merging_factors": {
            "nominal": 3,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c20p10_powheg",
    id=14800226,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c20p10],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p10_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=95_965,
    aux={
        "merging_factors": {
            "nominal": 3,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c20p35_powheg",
    id=14793318,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c20p35],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p35_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=99_650,
    aux={
        "merging_factors": {
            "nominal": 4,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c23_powheg",
    id=14807766,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c23],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-3p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=99_068,
    aux={
        "merging_factors": {
            "nominal": 4,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c2m2_powheg",
    id=14804196,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c2m2],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-m2p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=96_178,
    aux={
        "merging_factors": {
            "nominal": 4,
        },
    },
)

#
# VBF -> H -> HH
#

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm2p12_k2v3p87_klm5p96_madgraph",
    id=14877436,
    processes=[procs.hh_vbf_hbb_htt_kvm2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2B2Tau_CV-m2p12_C2V-3p87_C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=3_493_673,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14885040,
    processes=[procs.hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2Tau_CV-m1p83_C2V-3p57_C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=777_936,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14874151,
    processes=[procs.hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2Tau_CV-m1p60_C2V-2p72_C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=3_487_094,
    aux={
        "merging_factors": {
            "nominal": 26,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14877442,
    processes=[procs.hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2Tau_CV-m0p962_C2V-0p959_C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=3_485_405,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14877324,
    processes=[procs.hh_vbf_hbb_htt_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2B2Tau_CV-m0p758_C2V-1p44_C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=3_469_986,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14876526,
    processes=[procs.hh_vbf_hbb_htt_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2B2Tau_CV-m0p012_C2V-0p030_C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=3_479_700,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v2_kl1_madgraph",
    id=14797775,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v2_kl1],
    keys=[
        "/VBFHHto2B2Tau_CV-1_C2V-2_C3-1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=97_000,
    aux={
        "merging_factors": {
            "nominal": 4,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v1_kl2_madgraph",
    id=14801364,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v1_kl2],
    keys=[
        "/VBFHHto2B2Tau_CV-1_C2V-1_C3-2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100_000,
    aux={
        "merging_factors": {
            "nominal": 3,
        },
    },
)
cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v1_kl1_madgraph",
    id=14800905,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=3_432_100,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v0_kl1_madgraph",
    id=14801279,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=3_434_450,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14875979,
    processes=[procs.hh_vbf_hbb_htt_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2B2Tau_CV-1p74_C2V-1p37_C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=3_490_926,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14875975,
    processes=[procs.hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2Tau_CV-m1p21_C2V-1p94_C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=3_487_274,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

#
# ggf -> graviton -> HH
#

#
# ggf -> radion -> HH
#
