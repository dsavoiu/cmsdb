# coding: utf-8

"""
Electroweak datasets for the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v11 import campaign_run3_2022_preEE_nano_v11 as cpn


#
# Drell-Yan
#

# aMC@NLO (inclusive)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2L-2Jets_MLL-50&nanoaod_version=v11  # noqa  # noqa
cpn.add_dataset(
    name="dy_lep_m50_amcatnlo",
    id=14637757,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=44,
    n_events=71028905,
)

# aMC@NLO (n-jet binned)
# GrASP: https://cms-pdmv-prod.web.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2L-2Jets_MLL-50_.J&nanoaod_version=v11  # noqa
cpn.add_dataset(
    name="dy_lep_m50_0j_amcatnlo",
    id=14753715,
    is_data=False,
    processes=[procs.dy_lep_0j],
    keys=[
        "/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=554,
    n_events=99104104,
)

cpn.add_dataset(
    name="dy_lep_m50_1j_amcatnlo",
    id=14760704,
    is_data=False,
    processes=[procs.dy_lep_1j],
    keys=[
        "/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=580,
    n_events=101347537,
)

cpn.add_dataset(
    name="dy_lep_m50_2j_amcatnlo",
    id=14760787,
    is_data=False,
    processes=[procs.dy_lep_2j],
    keys=[
        "/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=493,
    n_events=76384157,
)

# MadGraph (inclusive)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYJetsToLL_M-50&nanoaod_version=v11  # noqa
cpn.add_dataset(
    name="dy_lep_m50_madgraph",
    id=14747813,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=478,
    n_events=73815961,
)

cpn.add_dataset(
    name="dy_lep_m50_forPOG_madgraph",
    id=14679260,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22NanoAODv11-forPOG_126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=26047237,
)

# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2L-4  # noqa
cpn.add_dataset(
    name="dy_lep_m50_1j_madgraph",
    id=14752052,
    is_data=False,
    processes=[procs.dy_lep_m50_1j],
    keys=[
        "/DYto2L-4Jets_MLL-50_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=189,
    n_events=15037614,
)

cpn.add_dataset(
    name="dy_lep_m50_2j_madgraph",
    id=14753884,
    is_data=False,
    processes=[procs.dy_lep_m50_2j],
    keys=[
        "/DYto2L-4Jets_MLL-50_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=181,
    n_events=14770353,
)

cpn.add_dataset(
    name="dy_lep_m50_3j_madgraph",
    id=14754183,
    is_data=False,
    processes=[procs.dy_lep_m50_3j],
    keys=[
        "/DYto2L-4Jets_MLL-50_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=141,
    n_events=8701712,
)

cpn.add_dataset(
    name="dy_lep_m50_4j_madgraph",
    id=14750269,
    is_data=False,
    processes=[procs.dy_lep_m50_4j],
    keys=[
        "/DYto2L-4Jets_MLL-50_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=59,
    n_events=3259821,
)


# POWHEG (decay to muons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2Mu  # noqa
cpn.add_dataset(
    name="dy_mm_m10to50_powheg",
    id=14688278,
    is_data=False,
    processes=[procs.dy_mm_m10to50],
    keys=[
        "/DYto2Mu_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=39,
    n_events=1453810,
)

cpn.add_dataset(
    name="dy_mm_m50to120_powheg",
    id=14689259,
    is_data=False,
    processes=[procs.dy_mm_m50to120],
    keys=[
        "/DYto2Mu_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=52,
    n_events=2924957,
)

cpn.add_dataset(
    name="dy_mm_m120to200_powheg",
    id=14688251,
    is_data=False,
    processes=[procs.dy_mm_m120to200],
    keys=[
        "/DYto2Mu_MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=65,
    n_events=1444050,
)

cpn.add_dataset(
    name="dy_mm_m200to400_powheg",
    id=14689208,
    is_data=False,
    processes=[procs.dy_mm_m200to400],
    keys=[
        "/DYto2Mu_MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=43,
    n_events=859355,
)

cpn.add_dataset(
    name="dy_mm_m400to800_powheg",
    id=14689272,
    is_data=False,
    processes=[procs.dy_mm_m400to800],
    keys=[
        "/DYto2Mu_MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=50,
    n_events=868352,
)

cpn.add_dataset(
    name="dy_mm_m800to1500_powheg",
    id=14688780,
    is_data=False,
    processes=[procs.dy_mm_m800to1500],
    keys=[
        "/DYto2Mu_MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=579560,
)

cpn.add_dataset(
    name="dy_mm_m1500to2500_powheg",
    id=14689999,
    is_data=False,
    processes=[procs.dy_mm_m1500to2500],
    keys=[
        "/DYto2Mu_MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=590523,
)

cpn.add_dataset(
    name="dy_mm_m2500to4000_powheg",
    id=14688526,
    is_data=False,
    processes=[procs.dy_mm_m2500to4000],
    keys=[
        "/DYto2Mu_MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=299278,
)

cpn.add_dataset(
    name="dy_mm_m4000to6000_powheg",
    id=14688511,
    is_data=False,
    processes=[procs.dy_mm_m4000to6000],
    keys=[
        "/DYto2Mu_MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=289200,
)

cpn.add_dataset(
    name="dy_mm_m6000_powheg",
    id=14688280,
    is_data=False,
    processes=[procs.dy_mm_m6000],
    keys=[
        "/DYto2Mu_MLL-6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=145002,
)

# POWHEG (decay to electrons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2E_MLL  # noqa
cpn.add_dataset(
    name="dy_ee_m10to50_powheg",
    id=14719362,
    is_data=False,
    processes=[procs.dy_ee_m10to50],
    keys=[
        "/DYto2E_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=57,
    n_events=1477950,
)

cpn.add_dataset(
    name="dy_ee_m50to120_powheg",
    id=14720581,
    is_data=False,
    processes=[procs.dy_ee_m50to120],
    keys=[
        "/DYto2E_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=103,
    n_events=2980614,
)

cpn.add_dataset(
    name="dy_ee_m120to200_powheg",
    id=14721306,
    is_data=False,
    processes=[procs.dy_ee_m120to200],
    keys=[
        "/DYto2E_MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=59,
    n_events=1490770,
)

cpn.add_dataset(
    name="dy_ee_m200to400_powheg",
    id=14720607,
    is_data=False,
    processes=[procs.dy_ee_m200to400],
    keys=[
        "/DYto2E_MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=55,
    n_events=899294,
)

cpn.add_dataset(
    name="dy_ee_m400to800_powheg",
    id=14720747,
    is_data=False,
    processes=[procs.dy_ee_m400to800],
    keys=[
        "/DYto2E_MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=62,
    n_events=893170,
)

cpn.add_dataset(
    name="dy_ee_m800to1500_powheg",
    id=14721411,
    is_data=False,
    processes=[procs.dy_ee_m800to1500],
    keys=[
        "/DYto2E_MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=599346,
)

cpn.add_dataset(
    name="dy_ee_m1500to2500_powheg",
    id=14719062,
    is_data=False,
    processes=[procs.dy_ee_m1500to2500],
    keys=[
        "/DYto2E_MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=586690,
)

cpn.add_dataset(
    name="dy_ee_m2500to4000_powheg",
    id=14720229,
    is_data=False,
    processes=[procs.dy_ee_m2500to4000],
    keys=[
        "/DYto2E_MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=290480,
)

cpn.add_dataset(
    name="dy_ee_m4000to6000_powheg",
    id=14721431,
    is_data=False,
    processes=[procs.dy_ee_m4000to6000],
    keys=[
        "/DYto2E_MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=298948,
)

cpn.add_dataset(
    name="dy_ee_m6000_powheg",
    id=14721416,
    is_data=False,
    processes=[procs.dy_ee_m6000],
    keys=[
        "/DYto2E_MLL-6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=149108,
)


#
# W boson production
#

# aMC@NLO (inclusive)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=WtoLNu-2Jets&nanoaod_version=v11  # noqa  # noqa
cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14611721,
    is_data=False,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=80257100,
)

# Madgraph (inclusive)
cpn.add_dataset(
    name="w_lnu_madgraph",
    id=14709629,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=[
        "/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=619,
    n_events=80355942,
)

# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=WtoLNu-4Jets_%281%7C2%7C3%7C4%29J&nanoaod_version=v11  # noqa  # noqa
cpn.add_dataset(
    name="w_lnu_1j_madgraph",
    id=14719206,
    is_data=False,
    processes=[procs.w_lnu_1j],
    keys=[
        "/WtoLNu-4Jets_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=160,
    n_events=10616726,
)

cpn.add_dataset(
    name="w_lnu_2j_madgraph",
    id=14719142,
    is_data=False,
    processes=[procs.w_lnu_2j],
    keys=[
        "/WtoLNu-4Jets_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=137,
    n_events=8765302,
)

cpn.add_dataset(
    name="w_lnu_3j_madgraph",
    id=14719158,
    is_data=False,
    processes=[procs.w_lnu_3j],
    keys=[
        "/WtoLNu-4Jets_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=127,
    n_events=7296665,
)

cpn.add_dataset(
    name="w_lnu_4j_madgraph",
    id=14746835,
    is_data=False,
    processes=[procs.w_lnu_4j],
    keys=[
        "/WtoLNu-4Jets_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=60,
    n_events=1460780,
)


#
# Diboson
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22GS&nanoaod_version=v11&short_name=VV  # noqa

cpn.add_dataset(
    name="zz_pythia",
    id=14587173,
    is_data=False,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=1186860,
)

cpn.add_dataset(
    name="wz_pythia",
    id=14596611,
    is_data=False,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=7744881,
)

cpn.add_dataset(
    name="ww_pythia",
    id=14694767,
    is_data=False,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=15474424,
)
