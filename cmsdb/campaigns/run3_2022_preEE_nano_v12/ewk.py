# coding: utf-8

"""
Electroweak datasets for the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn


#
# Drell-Yan
#

# aMC@NLO (inclusive)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2L-2Jets_MLL-50&nanoaod_version=v12  # noqa  # noqa
cpn.add_dataset(
    name="dy_lep_m50_amcatnlo",
    id=14796042,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=115,
    n_events=65997137,
)

# aMC@NLO (n-jet binned)
# GrASP: https://cms-pdmv-prod.web.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2L-2Jets_MLL-50_.J&nanoaod_version=v12  # noqa
cpn.add_dataset(
    name="dy_lep_m50_0j_amcatnlo",
    id=14791297,
    is_data=False,
    processes=[procs.dy_lep_0j],
    keys=[
        "/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=173,
    n_events=105230672,
)

cpn.add_dataset(
    name="dy_lep_m50_1j_amcatnlo",
    id=14791387,
    is_data=False,
    processes=[procs.dy_lep_1j],
    keys=[
        "/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=196,
    n_events=99076102,
)

cpn.add_dataset(
    name="dy_lep_m50_2j_amcatnlo",
    id=14790870,
    is_data=False,
    processes=[procs.dy_lep_2j],
    keys=[
        "/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=177,
    n_events=75705368,
)

# MadGraph (inclusive)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYJetsToLL_M-50&nanoaod_version=v12  # noqa
cpn.add_dataset(
    name="dy_lep_m50_madgraph",
    id=14791369,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=157,
    n_events=74397637,
)

cpn.add_dataset(
    name="dy_lep_m50_forPOG_madgraph",
    id=14802794,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22NanoAODv12-forPOG_130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=27096229,
)

# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2L-4  # noqa
cpn.add_dataset(
    name="dy_lep_m50_1j_madgraph",
    id=14801226,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=[
        "/DYto2L-4Jets_MLL-50_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=67,
    n_events=14777208,
)

cpn.add_dataset(
    name="dy_lep_m50_2j_madgraph",
    id=14791072,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=[
        "/DYto2L-4Jets_MLL-50_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=84,
    n_events=14552563,
)

cpn.add_dataset(
    name="dy_lep_m50_3j_madgraph",
    id=14791492,
    is_data=False,
    processes=[procs.dy_lep_m50_3j],
    keys=[
        "/DYto2L-4Jets_MLL-50_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=72,
    n_events=8672888,
)

cpn.add_dataset(
    name="dy_lep_m50_4j_madgraph",
    id=14792386,
    is_data=False,
    processes=[procs.dy_lep_m50_4j],
    keys=[
        "/DYto2L-4Jets_MLL-50_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=71,
    n_events=3278755,
)


# POWHEG (decay to muons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2Mu  # noqa
cpn.add_dataset(
    name="dy_mm_m10to50_powheg",
    id=14803660,
    is_data=False,
    processes=[procs.dy_mm_m10to50],
    keys=[
        "/DYto2Mu_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=1433695,
)

cpn.add_dataset(
    name="dy_mm_m50to120_powheg",
    id=14798792,
    is_data=False,
    processes=[procs.dy_mm_m50to120],
    keys=[
        "/DYto2Mu_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=2820937,
)

cpn.add_dataset(
    name="dy_mm_m120to200_powheg",
    id=14796178,
    is_data=False,
    processes=[procs.dy_mm_m120to200],
    keys=[
        "/DYto2Mu_MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=50,
    n_events=1453748,
)

cpn.add_dataset(
    name="dy_mm_m200to400_powheg",
    id=14792678,
    is_data=False,
    processes=[procs.dy_mm_m200to400],
    keys=[
        "/DYto2Mu_MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=853443,
)

cpn.add_dataset(
    name="dy_mm_m400to800_powheg",
    id=14792665,
    is_data=False,
    processes=[procs.dy_mm_m400to800],
    keys=[
        "/DYto2Mu_MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=874240,
)

cpn.add_dataset(
    name="dy_mm_m800to1500_powheg",
    id=14796123,
    is_data=False,
    processes=[procs.dy_mm_m800to1500],
    keys=[
        "/DYto2Mu_MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=579560,
)

cpn.add_dataset(
    name="dy_mm_m1500to2500_powheg",
    id=14800333,
    is_data=False,
    processes=[procs.dy_mm_m1500to2500],
    keys=[
        "/DYto2Mu_MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=590523,
)

cpn.add_dataset(
    name="dy_mm_m2500to4000_powheg",
    id=14807764,
    is_data=False,
    processes=[procs.dy_mm_m2500to4000],
    keys=[
        "/DYto2Mu_MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=299278,
)

cpn.add_dataset(
    name="dy_mm_m4000to6000_powheg",
    id=14798202,
    is_data=False,
    processes=[procs.dy_mm_m4000to6000],
    keys=[
        "/DYto2Mu_MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=289200,
)

cpn.add_dataset(
    name="dy_mm_m6000_powheg",
    id=14799634,
    is_data=False,
    processes=[procs.dy_mm_m6000],
    keys=[
        "/DYto2Mu_MLL-6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=145002,
)

# POWHEG (decay to electrons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2E_MLL  # noqa
cpn.add_dataset(
    name="dy_ee_m10to50_powheg",
    id=14794265,
    is_data=False,
    processes=[procs.dy_ee_m10to50],
    keys=[
        "/DYto2E_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=1477950,
)

cpn.add_dataset(
    name="dy_ee_m50to120_powheg",
    id=14792284,
    is_data=False,
    processes=[procs.dy_ee_m50to120],
    keys=[
        "/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=61,
    n_events=2892300,
)

cpn.add_dataset(
    name="dy_ee_m120to200_powheg",
    id=14793845,
    is_data=False,
    processes=[procs.dy_ee_m120to200],
    keys=[
        "/DYto2E_MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=1497870,
)

cpn.add_dataset(
    name="dy_ee_m200to400_powheg",
    id=14792660,
    is_data=False,
    processes=[procs.dy_ee_m200to400],
    keys=[
        "/DYto2E_MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=874584,
)

cpn.add_dataset(
    name="dy_ee_m400to800_powheg",
    id=14794296,
    is_data=False,
    processes=[procs.dy_ee_m400to800],
    keys=[
        "/DYto2E_MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=39,
    n_events=1074165,
)

cpn.add_dataset(
    name="dy_ee_m800to1500_powheg",
    id=14796566,
    is_data=False,
    processes=[procs.dy_ee_m800to1500],
    keys=[
        "/DYto2E_MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=610464,
)

cpn.add_dataset(
    name="dy_ee_m1500to2500_powheg",
    id=14793558,
    is_data=False,
    processes=[procs.dy_ee_m1500to2500],
    keys=[
        "/DYto2E_MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=586690,
)

cpn.add_dataset(
    name="dy_ee_m2500to4000_powheg",
    id=14792074,
    is_data=False,
    processes=[procs.dy_ee_m2500to4000],
    keys=[
        "/DYto2E_MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=290480,
)

cpn.add_dataset(
    name="dy_ee_m4000to6000_powheg",
    id=14793360,
    is_data=False,
    processes=[procs.dy_ee_m4000to6000],
    keys=[
        "/DYto2E_MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=298948,
)

cpn.add_dataset(
    name="dy_ee_m6000_powheg",
    id=14792558,
    is_data=False,
    processes=[procs.dy_ee_m6000],
    keys=[
        "/DYto2E_MLL-6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=145094,
)


#
# W boson production
#

# aMC@NLO (inclusive)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=WtoLNu-2Jets&nanoaod_version=v12  # noqa  # noqa
cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14803995,
    is_data=False,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=148,
    n_events=84739011,
)

# Madgraph (inclusive)
cpn.add_dataset(
    name="w_lnu_madgraph",
    id=14792147,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=[
        "/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=197,
    n_events=85018912,
)

# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=WtoLNu-4Jets_%281%7C2%7C3%7C4%29J&nanoaod_version=v12  # noqa  # noqa
cpn.add_dataset(
    name="w_lnu_1j_madgraph",
    id=14811293,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=[
        "/WtoLNu-4Jets_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=9871448,
)

cpn.add_dataset(
    name="w_lnu_2j_madgraph",
    id=14811284,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=[
        "/WtoLNu-4Jets_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=9184457,
)

cpn.add_dataset(
    name="w_lnu_3j_madgraph",
    id=14804462,
    is_data=False,
    processes=[procs.w_lnu_3j],
    keys=[
        "/WtoLNu-4Jets_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=78,
    n_events=7804738,
)

cpn.add_dataset(
    name="w_lnu_4j_madgraph",
    id=14794281,
    is_data=False,
    processes=[procs.w_lnu_4j],
    keys=[
        "/WtoLNu-4Jets_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=64,
    n_events=1463885,
)


#
# Diboson
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22GS&nanoaod_version=v12&short_name=VV  # noqa

cpn.add_dataset(
    name="zz_pythia",
    id=14808010,
    is_data=False,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=1181750,
)

cpn.add_dataset(
    name="wz_pythia",
    id=14803901,
    is_data=False,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=7527043,
)

cpn.add_dataset(
    name="ww_pythia",
    id=14800098,
    is_data=False,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=63,
    n_events=15357390,
)
