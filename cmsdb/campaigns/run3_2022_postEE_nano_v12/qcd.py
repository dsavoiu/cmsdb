# coding: utf-8

"""
QCD datasets for the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v12 import campaign_run3_2022_postEE_nano_v12 as cpn


#
# QCD flat samples
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEGS&nanoaod_version=v12&dataset=QCD_PT-15*Flat2018&chained_request=EpsilonPU  # noqa
cpn.add_dataset(
    name="qcd_flat2018_epsilon_pu_pythia",
    id=14789169,
    is_data=False,
    processes=[procs.qcd_flat],
    keys=[
        "/QCD_PT-15to7000_TuneCP5_Flat2018_13p6TeV_pythia8/Run3Summer22EENanoAODv12-EpsilonPU_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=499399,
)


#
# QCD (MadGraph HT-binned)
#

# missing as of 2023-07-01


#
# QCD (Pythia pT-binned)
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEGS&nanoaod_version=v12&dataset=QCD_PT-*%28to*%29%3F0_TuneCP5&chained_request=Premix  # noqa

cpn.add_dataset(
    name="qcd_pt50to80_pythia",
    id=14810698,
    is_data=False,
    processes=[procs.qcd_pt50to80],
    keys=[
        "/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=19734680,
)

cpn.add_dataset(
    name="qcd_pt80to120_pythia",
    id=14803293,
    is_data=False,
    processes=[procs.qcd_pt80to120],
    keys=[
        "/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=59,
    n_events=29570284,
)

cpn.add_dataset(
    name="qcd_pt120to170_pythia",
    id=14791903,
    is_data=False,
    processes=[procs.qcd_pt120to170],
    keys=[
        "/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=86,
    n_events=27570720,
)

cpn.add_dataset(
    name="qcd_pt170to300_pythia",
    id=14791655,
    is_data=False,
    processes=[procs.qcd_pt170to300],
    keys=[
        "/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=84,
    n_events=27512595,
)

cpn.add_dataset(
    name="qcd_pt300to470_pythia",
    id=14805103,
    is_data=False,
    processes=[procs.qcd_pt300to470],
    keys=[
        "/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=114,
    n_events=55587009,
)

cpn.add_dataset(
    name="qcd_pt470to600_pythia",
    id=14810679,
    is_data=False,
    processes=[procs.qcd_pt470to600],
    keys=[
        "/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=58,
    n_events=26324412,
)

cpn.add_dataset(
    name="qcd_pt600to800_pythia",
    id=14791962,
    is_data=False,
    processes=[procs.qcd_pt600to800],
    keys=[
        "/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=163,
    n_events=63833775,
)

cpn.add_dataset(
    name="qcd_pt800to1000_pythia",
    id=14792078,
    is_data=False,
    processes=[procs.qcd_pt800to1000],
    keys=[
        "/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=137,
    n_events=37957120,
)

cpn.add_dataset(
    name="qcd_pt1000to1400_pythia",
    id=14805250,
    is_data=False,
    processes=[procs.qcd_pt1000to1400],
    keys=[
        "/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=65,
    n_events=19209425,
)

cpn.add_dataset(
    name="qcd_pt1400to1800_pythia",
    id=14795350,
    is_data=False,
    processes=[procs.qcd_pt1400to1800],
    keys=[
        "/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=5670888,
)

cpn.add_dataset(
    name="qcd_pt1800to2400_pythia",
    id=14805098,
    is_data=False,
    processes=[procs.qcd_pt1800to2400],
    keys=[
        "/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=41,
    n_events=2914410,
)

cpn.add_dataset(
    name="qcd_pt2400to3200_pythia",
    id=14804218,
    is_data=False,
    processes=[procs.qcd_pt2400to3200],
    keys=[
        "/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=55,
    n_events=1900526,
)

cpn.add_dataset(
    name="qcd_pt3200_pythia",
    id=14804049,
    is_data=False,
    processes=[procs.qcd_pt3200],
    keys=[
        "/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=841736,
)


#
# QCD (Pythia pT-binned, muon-enriched)
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEGS&nanoaod_version=v12&dataset=QCD_PT-*%28to*%29%3F_MuEnrichedPt5_TuneCP5&chained_request=Premix  # noqa

cpn.add_dataset(
    name="qcd_mu_pt15to20_pythia",
    id=14805741,
    is_data=False,
    processes=[procs.qcd_mu_pt15to20],
    keys=[
        "/QCD_PT-15to20_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=16022411,
)

cpn.add_dataset(
    name="qcd_mu_pt20to30_pythia",
    id=14791836,
    is_data=False,
    processes=[procs.qcd_mu_pt20to30],
    keys=[
        "/QCD_PT-20to30_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=156,
    n_events=111483708,
)

cpn.add_dataset(
    name="qcd_mu_pt30to50_pythia",
    id=14790872,
    is_data=False,
    processes=[procs.qcd_mu_pt30to50],
    keys=[
        "/QCD_PT-30to50_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=221,
    n_events=102351102,
)

cpn.add_dataset(
    name="qcd_mu_pt50to80_pythia",
    id=14790975,
    is_data=False,
    processes=[procs.qcd_mu_pt50to80],
    keys=[
        "/QCD_PT-50to80_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=89,
    n_events=39665709,
)

cpn.add_dataset(
    name="qcd_mu_pt80to120_pythia",
    id=14808161,
    is_data=False,
    processes=[procs.qcd_mu_pt80to120],
    keys=[
        "/QCD_PT-80to120_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=159,
    n_events=98693572,
)

cpn.add_dataset(
    name="qcd_mu_pt120to170_pythia",
    id=14805262,
    is_data=False,
    processes=[procs.qcd_mu_pt120to170],
    keys=[
        "/QCD_PT-120to170_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=171,
    n_events=71463810,
)

cpn.add_dataset(
    name="qcd_mu_pt170to300_pythia",
    id=14797549,
    is_data=False,
    processes=[procs.qcd_mu_pt170to300],
    keys=[
        "/QCD_PT-170to300_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=264,
    n_events=109991815,
)

cpn.add_dataset(
    name="qcd_mu_pt300to470_pythia",
    id=14792096,
    is_data=False,
    processes=[procs.qcd_mu_pt300to470],
    keys=[
        "/QCD_PT-300to470_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=300,
    n_events=104186366,
)

cpn.add_dataset(
    name="qcd_mu_pt470to600_pythia",
    id=14801374,
    is_data=False,
    processes=[procs.qcd_mu_pt470to600],
    keys=[
        "/QCD_PT-470to600_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=222,
    n_events=71895522,
)

cpn.add_dataset(
    name="qcd_mu_pt600to800_pythia",
    id=14805693,
    is_data=False,
    processes=[procs.qcd_mu_pt600to800],
    keys=[
        "/QCD_PT-600to800_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=150,
    n_events=72668622,
)

cpn.add_dataset(
    name="qcd_mu_pt800to1000_pythia",
    id=14802178,
    is_data=False,
    processes=[procs.qcd_mu_pt800to1000],
    keys=[
        "/QCD_PT-800to1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=375,
    n_events=132056316,
)

cpn.add_dataset(
    name="qcd_mu_pt1000_pythia",
    id=14791859,
    is_data=False,
    processes=[procs.qcd_mu_pt1000],
    keys=[
        "/QCD_PT-1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=129,
    n_events=45523614,
)


#
# QCD (Pythia pT-binned, double EM-enriched)
#

# GrASP: https://cms-pdmv-prod.web.cern.ch/grasp/samples?campaign=Run3Summer22EEGS&nanoaod_version=v12&dataset=QCD*EMEnriched&chained_request=Premix  # noqa

cpn.add_dataset(
    name="qcd_double_em_pt30to40_pythia",
    id=14798807,
    is_data=False,
    processes=[procs.qcd_double_em_pt30to40],
    keys=[
        "/QCD_PT-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=118,
    n_events=4581753,
)

cpn.add_dataset(
    name="qcd_double_em_pt30_pythia",
    id=14797413,
    is_data=False,
    processes=[procs.qcd_double_em_pt30],
    keys=[
        "/QCD_PT-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=82,
    n_events=9929160,
)

cpn.add_dataset(
    name="qcd_double_em_pt40_pythia",
    id=14810606,
    is_data=False,
    processes=[procs.qcd_double_em_pt40],
    keys=[
        "/QCD_PT-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=10278008,
)
