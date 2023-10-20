# coding: utf-8

"""
CMS datasets from the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn


#
# Muon
#

cpn.add_dataset(
    name="data_mu_c",
    id=14784127,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=124,
    n_events=138427345,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=14783357,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022D-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=82,
    n_events=75468381,
    aux={
        "era": "D",
    },
)

#
# E/Gamma
#

cpn.add_dataset(
    name="data_egamma_c",
    id=14784140,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=313,
    n_events=263689151,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_egamma_d",
    id=14783299,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022D-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=109,
    n_events=89134996,
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
    id=14784098,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=25,
    n_events=15620904,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_jetmet_c",
    id=14784135,
    is_data=True,
    processes=[procs.data_jetmet],
    keys=[
        "/JetMET/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=206,
    n_events=169187457,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_jetmet_d",
    id=14809508,
    is_data=True,
    processes=[procs.data_jetmet],
    keys=[
        "/JetMET/Run2022D-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=100,
    n_events=100853361,
    aux={
        "era": "D",
    },
)
