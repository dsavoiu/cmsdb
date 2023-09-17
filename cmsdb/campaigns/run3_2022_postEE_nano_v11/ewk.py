# coding: utf-8

"""
Electroweak datasets for the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v11 import campaign_run3_2022_postEE_nano_v11 as cpn


#
# Drell-Yan
#

# aMC@NLO (inclusive)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2L-2Jets_MLL-50&nanoaod_version=v11  # noqa
cpn.add_dataset(
    name="dy_lep_m50_amcatnlo",
    id=14615268,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=125,
    n_events=215543566,
)

# aMC@NLO (n-jet binned)
# GrASP: https://cms-pdmv-prod.web.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2L-2Jets_MLL-50_.J&nanoaod_version=v11  # noqa
cpn.add_dataset(
    name="dy_lep_m50_0j_amcatnlo",
    id=14748386,
    is_data=False,
    processes=[procs.dy_lep_0j],
    keys=[
        "/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1727,
    n_events=349861843,
)

cpn.add_dataset(
    name="dy_lep_m50_1j_amcatnlo",
    id=14758296,
    is_data=False,
    processes=[procs.dy_lep_1j],
    keys=[
        "/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1727,
    n_events=327883411,
)

cpn.add_dataset(
    name="dy_lep_m50_2j_amcatnlo",
    id=14753958,
    is_data=False,
    processes=[procs.dy_lep_2j],
    keys=[
        "/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1634,
    n_events=278827295,
)

# MadGraph (inclusive)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYJetsToLL_M-50&nanoaod_version=v11  # noqa
cpn.add_dataset(
    name="dy_lep_m50_madgraph",
    id=14750274,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1345,
    n_events=244155203,
)

cpn.add_dataset(
    name="dy_lep_m50_forPOG_madgraph",
    id=14679709,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22EENanoAODv11-forPOG_126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=55,
    n_events=96296977,
)

# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2L-4  # noqa
cpn.add_dataset(
    name="dy_lep_m50_1j_madgraph",
    id=14753925,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=[
        "/DYto2L-4Jets_MLL-50_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=382,
    n_events=50011918,
)

cpn.add_dataset(
    name="dy_lep_m50_2j_madgraph",
    id=14747611,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=[
        "/DYto2L-4Jets_MLL-50_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=363,
    n_events=49313209,
)

cpn.add_dataset(
    name="dy_lep_m50_3j_madgraph",
    id=14754714,
    is_data=False,
    processes=[procs.dy_lep_m50_3j],
    keys=[
        "/DYto2L-4Jets_MLL-50_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=295,
    n_events=28666329,
)

cpn.add_dataset(
    name="dy_lep_m50_4j_madgraph",
    id=14758733,
    is_data=False,
    processes=[procs.dy_lep_m50_4j],
    keys=[
        "/DYto2L-4Jets_MLL-50_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=124,
    n_events=9330351,
)


# POWHEG (decay to muons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2Mu  # noqa
cpn.add_dataset(
    name="dy_mm_m10to50_powheg",
    id=14689096,
    is_data=False,
    processes=[procs.dy_mm_m10to50],
    keys=[
        "/DYto2Mu_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=161,
    n_events=5091024,
)

cpn.add_dataset(
    name="dy_mm_m50to120_powheg",
    id=14688586,
    is_data=False,
    processes=[procs.dy_mm_m50to120],
    keys=[
        "/DYto2Mu_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=171,
    n_events=10153980,
)

cpn.add_dataset(
    name="dy_mm_m120to200_powheg",
    id=14689227,
    is_data=False,
    processes=[procs.dy_mm_m120to200],
    keys=[
        "/DYto2Mu_MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=140,
    n_events=5077720,
)

cpn.add_dataset(
    name="dy_mm_m200to400_powheg",
    id=14688233,
    is_data=False,
    processes=[procs.dy_mm_m200to400],
    keys=[
        "/DYto2Mu_MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=111,
    n_events=3054927,
)

cpn.add_dataset(
    name="dy_mm_m400to800_powheg",
    id=14689146,
    is_data=False,
    processes=[procs.dy_mm_m400to800],
    keys=[
        "/DYto2Mu_MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=114,
    n_events=3030210,
)

cpn.add_dataset(
    name="dy_mm_m800to1500_powheg",
    id=14689253,
    is_data=False,
    processes=[procs.dy_mm_m800to1500],
    keys=[
        "/DYto2Mu_MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=77,
    n_events=2093529,
)

cpn.add_dataset(
    name="dy_mm_m1500to2500_powheg",
    id=14689388,
    is_data=False,
    processes=[procs.dy_mm_m1500to2500],
    keys=[
        "/DYto2Mu_MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=83,
    n_events=2013249,
)

cpn.add_dataset(
    name="dy_mm_m2500to4000_powheg",
    id=14688300,
    is_data=False,
    processes=[procs.dy_mm_m2500to4000],
    keys=[
        "/DYto2Mu_MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=1005958,
)

cpn.add_dataset(
    name="dy_mm_m4000to6000_powheg",
    id=14689523,
    is_data=False,
    processes=[procs.dy_mm_m4000to6000],
    keys=[
        "/DYto2Mu_MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=53,
    n_events=1026075,
)

cpn.add_dataset(
    name="dy_mm_m6000_powheg",
    id=14689404,
    is_data=False,
    processes=[procs.dy_mm_m6000],
    keys=[
        "/DYto2Mu_MLL-6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=503888,
)

# POWHEG (decay to electrons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2E_MLL  # noqa
cpn.add_dataset(
    name="dy_ee_m10to50_powheg",
    id=14720604,
    is_data=False,
    processes=[procs.dy_ee_m10to50],
    keys=[
        "/DYto2E_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=136,
    n_events=5219382,
)

cpn.add_dataset(
    name="dy_ee_m50to120_powheg",
    id=14720875,
    is_data=False,
    processes=[procs.dy_ee_m50to120],
    keys=[
        "/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=180,
    n_events=10411794,
)

cpn.add_dataset(
    name="dy_ee_m120to200_powheg",
    id=14719094,
    is_data=False,
    processes=[procs.dy_ee_m120to200],
    keys=[
        "/DYto2E_MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=153,
    n_events=5231358,
)

cpn.add_dataset(
    name="dy_ee_m200to400_powheg",
    id=14721197,
    is_data=False,
    processes=[procs.dy_ee_m200to400],
    keys=[
        "/DYto2E_MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=67,
    n_events=3146485,
)

cpn.add_dataset(
    name="dy_ee_m400to800_powheg",
    id=14719128,
    is_data=False,
    processes=[procs.dy_ee_m400to800],
    keys=[
        "/DYto2E_MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=88,
    n_events=3035250,
)

cpn.add_dataset(
    name="dy_ee_m800to1500_powheg",
    id=14721236,
    is_data=False,
    processes=[procs.dy_ee_m800to1500],
    keys=[
        "/DYto2E_MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=56,
    n_events=2093400,
)

cpn.add_dataset(
    name="dy_ee_m1500to2500_powheg",
    id=14720587,
    is_data=False,
    processes=[procs.dy_ee_m1500to2500],
    keys=[
        "/DYto2E_MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=88,
    n_events=2085456,
)

cpn.add_dataset(
    name="dy_ee_m2500to4000_powheg",
    id=14721213,
    is_data=False,
    processes=[procs.dy_ee_m2500to4000],
    keys=[
        "/DYto2E_MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=1050000,
)

cpn.add_dataset(
    name="dy_ee_m4000to6000_powheg",
    id=14721108,
    is_data=False,
    processes=[procs.dy_ee_m4000to6000],
    keys=[
        "/DYto2E_MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=59,
    n_events=1048936,
)

cpn.add_dataset(
    name="dy_ee_m6000_powheg",
    id=14721446,
    is_data=False,
    processes=[procs.dy_ee_m6000],
    keys=[
        "/DYto2E_MLL-6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=474751,
)


#
# W boson production
#

# aMC@NLO (inclusive)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=WtoLNu-2Jets&nanoaod_version=v11  # noqa
cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14716346,
    is_data=False,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=161,
    n_events=291650146,
)

# Madgraph (inclusive)
cpn.add_dataset(
    name="w_lnu_madgraph",
    id=14736960,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=[
        "/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1695,
    n_events=347826137,
)

# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=WtoLNu-4Jets_%281%7C2%7C3%7C4%29J&nanoaod_version=v11  # noqa
cpn.add_dataset(
    name="w_lnu_1j_madgraph",
    id=14720058,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=[
        "/WtoLNu-4Jets_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=289,
    n_events=41185459,
)

cpn.add_dataset(
    name="w_lnu_2j_madgraph",
    id=14719854,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=[
        "/WtoLNu-4Jets_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=297,
    n_events=33969082,
)

cpn.add_dataset(
    name="w_lnu_3j_madgraph",
    id=14719643,
    is_data=False,
    processes=[procs.w_lnu_3j],
    keys=[
        "/WtoLNu-4Jets_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=243,
    n_events=26808463,
)

cpn.add_dataset(
    name="w_lnu_4j_madgraph",
    id=14747345,
    is_data=False,
    processes=[procs.w_lnu_4j],
    keys=[
        "/WtoLNu-4Jets_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=126,
    n_events=4861057,
)


#
# Diboson
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEGS&nanoaod_version=v11&short_name=VV  # noqa

cpn.add_dataset(
    name="zz_pythia",
    id=14683232,
    is_data=False,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=3871680,
)

cpn.add_dataset(
    name="wz_pythia",
    id=14597897,
    is_data=False,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=27291718,
)

cpn.add_dataset(
    name="ww_pythia",
    id=14596976,
    is_data=False,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=54649280,
)
