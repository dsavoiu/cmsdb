# coding: utf-8

"""
Electroweak datasets for the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v12 import campaign_run3_2022_postEE_nano_v12 as cpn


#
# Drell-Yan
#

# aMC@NLO (inclusive)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2L-2Jets_MLL-50&nanoaod_version=v12  # noqa
cpn.add_dataset(
    name="dy_lep_m50_amcatnlo",
    id=14791972,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=286,
    n_events=213436879,
)

# aMC@NLO (n-jet binned)
# GrASP: https://cms-pdmv-prod.web.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2L-2Jets_MLL-50_.J&nanoaod_version=v12  # noqa
cpn.add_dataset(
    name="dy_lep_m50_0j_amcatnlo",
    id=14791116,
    is_data=False,
    processes=[procs.dy_lep_0j],
    keys=[
        "/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=452,
    n_events=346950546,
)

cpn.add_dataset(
    name="dy_lep_m50_1j_amcatnlo",
    id=14790681,
    is_data=False,
    processes=[procs.dy_lep_1j],
    keys=[
        "/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=454,
    n_events=322623183,
)

cpn.add_dataset(
    name="dy_lep_m50_2j_amcatnlo",
    id=14801013,
    is_data=False,
    processes=[procs.dy_lep_2j],
    keys=[
        "/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=386,
    n_events=277437970,
)

# MadGraph (inclusive)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYJetsToLL_M-50&nanoaod_version=v12  # noqa
cpn.add_dataset(
    name="dy_lep_m50_madgraph",
    id=14810676,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=236,
    n_events=240872023,
)

cpn.add_dataset(
    name="dy_lep_m50_forPOG_madgraph",
    id=14791423,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22EENanoAODv12-forPOG_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=127,
    n_events=94947242,
)

# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2L-4  # noqa
cpn.add_dataset(
    name="dy_lep_m50_1j_madgraph",
    id=14790810,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=[
        "/DYto2L-4Jets_MLL-50_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=187,
    n_events=57771603,
)

cpn.add_dataset(
    name="dy_lep_m50_2j_madgraph",
    id=14794042,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=[
        "/DYto2L-4Jets_MLL-50_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=147,
    n_events=50007544,
)

cpn.add_dataset(
    name="dy_lep_m50_3j_madgraph",
    id=14791238,
    is_data=False,
    processes=[procs.dy_lep_m50_3j],
    keys=[
        "/DYto2L-4Jets_MLL-50_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=109,
    n_events=28997825,
)

cpn.add_dataset(
    name="dy_lep_m50_4j_madgraph",
    id=14794840,
    is_data=False,
    processes=[procs.dy_lep_m50_4j],
    keys=[
        "/DYto2L-4Jets_MLL-50_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=140,
    n_events=9490226,
)


# POWHEG (decay to muons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2Mu  # noqa
cpn.add_dataset(
    name="dy_mm_m10to50_powheg",
    id=14793725,
    is_data=False,
    processes=[procs.dy_mm_m10to50],
    keys=[
        "/DYto2Mu_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=108,
    n_events=5030672,
)

cpn.add_dataset(
    name="dy_mm_m50to120_powheg",
    id=14791206,
    is_data=False,
    processes=[procs.dy_mm_m50to120],
    keys=[
        "/DYto2Mu_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=106,
    n_events=10150330,
)

cpn.add_dataset(
    name="dy_mm_m120to200_powheg",
    id=14796418,
    is_data=False,
    processes=[procs.dy_mm_m120to200],
    keys=[
        "/DYto2Mu_MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=91,
    n_events=5050710,
)

cpn.add_dataset(
    name="dy_mm_m200to400_powheg",
    id=14794168,
    is_data=False,
    processes=[procs.dy_mm_m200to400],
    keys=[
        "/DYto2Mu_MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=75,
    n_events=2972383,
)

cpn.add_dataset(
    name="dy_mm_m400to800_powheg",
    id=14793726,
    is_data=False,
    processes=[procs.dy_mm_m400to800],
    keys=[
        "/DYto2Mu_MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=2930748,
)

cpn.add_dataset(
    name="dy_mm_m800to1500_powheg",
    id=14807688,
    is_data=False,
    processes=[procs.dy_mm_m800to1500],
    keys=[
        "/DYto2Mu_MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=2093529,
)

cpn.add_dataset(
    name="dy_mm_m1500to2500_powheg",
    id=14796179,
    is_data=False,
    processes=[procs.dy_mm_m1500to2500],
    keys=[
        "/DYto2Mu_MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=59,
    n_events=2008146,
)

cpn.add_dataset(
    name="dy_mm_m2500to4000_powheg",
    id=14797656,
    is_data=False,
    processes=[procs.dy_mm_m2500to4000],
    keys=[
        "/DYto2Mu_MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=1003792,
)

cpn.add_dataset(
    name="dy_mm_m4000to6000_powheg",
    id=14794113,
    is_data=False,
    processes=[procs.dy_mm_m4000to6000],
    keys=[
        "/DYto2Mu_MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=41,
    n_events=994900,
)

cpn.add_dataset(
    name="dy_mm_m6000_powheg",
    id=14803945,
    is_data=False,
    processes=[procs.dy_mm_m6000],
    keys=[
        "/DYto2Mu_MLL-6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=503888,
)

# POWHEG (decay to electrons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2E_MLL  # noqa
cpn.add_dataset(
    name="dy_ee_m10to50_powheg",
    id=14791813,
    is_data=False,
    processes=[procs.dy_ee_m10to50],
    keys=[
        "/DYto2E_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=58,
    n_events=5333106,
)

cpn.add_dataset(
    name="dy_ee_m50to120_powheg",
    id=14795549,
    is_data=False,
    processes=[procs.dy_ee_m50to120],
    keys=[
        "/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=98,
    n_events=10403118,
)

cpn.add_dataset(
    name="dy_ee_m120to200_powheg",
    id=14793844,
    is_data=False,
    processes=[procs.dy_ee_m120to200],
    keys=[
        "/DYto2E_MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=5238528,
)

cpn.add_dataset(
    name="dy_ee_m200to400_powheg",
    id=14795467,
    is_data=False,
    processes=[procs.dy_ee_m200to400],
    keys=[
        "/DYto2E_MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=3147891,
)

cpn.add_dataset(
    name="dy_ee_m400to800_powheg",
    id=14794992,
    is_data=False,
    processes=[procs.dy_ee_m400to800],
    keys=[
        "/DYto2E_MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=3044700,
)

cpn.add_dataset(
    name="dy_ee_m800to1500_powheg",
    id=14793846,
    is_data=False,
    processes=[procs.dy_ee_m800to1500],
    keys=[
        "/DYto2E_MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=2004300,
)

cpn.add_dataset(
    name="dy_ee_m1500to2500_powheg",
    id=14793671,
    is_data=False,
    processes=[procs.dy_ee_m1500to2500],
    keys=[
        "/DYto2E_MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=72,
    n_events=2053944,
)

cpn.add_dataset(
    name="dy_ee_m2500to4000_powheg",
    id=14797458,
    is_data=False,
    processes=[procs.dy_ee_m2500to4000],
    keys=[
        "/DYto2E_MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=986496,
)

cpn.add_dataset(
    name="dy_ee_m4000to6000_powheg",
    id=14794112,
    is_data=False,
    processes=[procs.dy_ee_m4000to6000],
    keys=[
        "/DYto2E_MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=1027656,
)

cpn.add_dataset(
    name="dy_ee_m6000_powheg",
    id=14795328,
    is_data=False,
    processes=[procs.dy_ee_m6000],
    keys=[
        "/DYto2E_MLL-6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=550816,
)


#
# W boson production
#

# aMC@NLO (inclusive)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=WtoLNu-2Jets&nanoaod_version=v12  # noqa
cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14796394,
    is_data=False,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=381,
    n_events=281543551,
)

# Madgraph (inclusive)
cpn.add_dataset(
    name="w_lnu_madgraph",
    id=14791608,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=[
        "/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=445,
    n_events=340358887,
)

# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=WtoLNu-4Jets_%281%7C2%7C3%7C4%29J&nanoaod_version=v12  # noqa
cpn.add_dataset(
    name="w_lnu_1j_madgraph",
    id=14794225,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=[
        "/WtoLNu-4Jets_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=133,
    n_events=40329821,
)

cpn.add_dataset(
    name="w_lnu_2j_madgraph",
    id=14791212,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=[
        "/WtoLNu-4Jets_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=105,
    n_events=33044336,
)

cpn.add_dataset(
    name="w_lnu_3j_madgraph",
    id=14800652,
    is_data=False,
    processes=[procs.w_lnu_3j],
    keys=[
        "/WtoLNu-4Jets_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=104,
    n_events=26832656,
)

cpn.add_dataset(
    name="w_lnu_4j_madgraph",
    id=14794226,
    is_data=False,
    processes=[procs.w_lnu_4j],
    keys=[
        "/WtoLNu-4Jets_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=123,
    n_events=4908700,
)


#
# Diboson
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEGS&nanoaod_version=v12&short_name=VV  # noqa

cpn.add_dataset(
    name="zz_pythia",
    id=14800856,
    is_data=False,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=3890400,
)

cpn.add_dataset(
    name="wz_pythia",
    id=14799680,
    is_data=False,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=90,
    n_events=26840468,
)

cpn.add_dataset(
    name="ww_pythia",
    id=14801288,
    is_data=False,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=117,
    n_events=53190560,
)
