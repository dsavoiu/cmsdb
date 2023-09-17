# coding: utf-8

"""
CMS datasets from the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v11 import campaign_run3_2022_preEE_nano_v11 as cpn


#
# Muon
#

cpn.add_dataset(
    name="data_mu_c",
    id=14670816,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022C-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=85,
    n_events=138018846,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=14665037,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022D-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=55,
    n_events=75494657,
    aux={
        "era": "D",
    },
)

#
# E/Gamma
#

cpn.add_dataset(
    name="data_egamma_c",
    id=14665314,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022C-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=164,
    n_events=263336263,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_egamma_d",
    id=14665654,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022D-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=62,
    n_events=88530905,
    aux={
        "era": "D",
    },
)

#
# JetHT/JetMET
# note: primary dataset JetHT only available for first part of run C,
# then changed to JetMET
#

cpn.add_dataset(
    name="data_jetht_c",
    id=14665445,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2022C-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=17,
    n_events=15620904,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_jetmet_c",
    id=14668015,
    is_data=True,
    processes=[procs.data_jetmet],
    keys=[
        "/JetMET/Run2022C-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=126,
    n_events=169949259,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_jetmet_d",
    id=14665614,
    is_data=True,
    processes=[procs.data_jetmet],
    keys=[
        "/JetMET/Run2022D-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=78,
    n_events=101352671,
    aux={
        "era": "D",
    },
)
