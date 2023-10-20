# coding: utf-8

"""
QCD datasets for the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn


#
# QCD flat samples
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22GS&nanoaod_version=v12&dataset=QCD_PT-15*Flat2018&chained_request=Premix  # noqa
cpn.add_dataset(
    name="qcd_flat2018_pythia",
    id=14797825,
    is_data=False,
    processes=[procs.qcd_flat],
    keys=[
        "/QCD_PT-15_TuneCP5_Flat2018_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=41,
    n_events=9475994,
)

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22GS&nanoaod_version=v12&dataset=QCD_PT-15*Flat2018&chained_request=EpsilonPU  # noqa
cpn.add_dataset(
    name="qcd_flat2018_epsilon_pu_pythia",
    id=14789616,
    is_data=False,
    processes=[procs.qcd_flat],
    keys=[
        "/QCD_PT-15to7000_TuneCP5_Flat2018_13p6TeV_pythia8/Run3Summer22NanoAODv12-EpsilonPU_130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=499387,
)


#
# QCD (MadGraph HT-binned)
#

# missing as of 2023-07-01


#
# QCD (Pythia pT-binned)
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22GS&nanoaod_version=v12&dataset=QCD_PT-*%28to*%29%3F0_TuneCP5&chained_request=Premix  # noqa

cpn.add_dataset(
    name="qcd_pt50to80_pythia",
    id=14791076,
    is_data=False,
    processes=[procs.qcd_pt50to80],
    keys=[
        "/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=64,
    n_events=19617716,
)

cpn.add_dataset(
    name="qcd_pt80to120_pythia",
    id=14790893,
    is_data=False,
    processes=[procs.qcd_pt80to120],
    keys=[
        "/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=84,
    n_events=29759904,
)

cpn.add_dataset(
    name="qcd_pt120to170_pythia",
    id=14796484,
    is_data=False,
    processes=[procs.qcd_pt120to170],
    keys=[
        "/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=64,
    n_events=29178417,
)

cpn.add_dataset(
    name="qcd_pt170to300_pythia",
    id=14791190,
    is_data=False,
    processes=[procs.qcd_pt170to300],
    keys=[
        "/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=94,
    n_events=28570060,
)

cpn.add_dataset(
    name="qcd_pt300to470_pythia",
    id=14806680,
    is_data=False,
    processes=[procs.qcd_pt300to470],
    keys=[
        "/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=99,
    n_events=56638371,
)

cpn.add_dataset(
    name="qcd_pt470to600_pythia",
    id=14801238,
    is_data=False,
    processes=[procs.qcd_pt470to600],
    keys=[
        "/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=80,
    n_events=27468864,
)

cpn.add_dataset(
    name="qcd_pt600to800_pythia",
    id=14803683,
    is_data=False,
    processes=[procs.qcd_pt600to800],
    keys=[
        "/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=130,
    n_events=65122631,
)

cpn.add_dataset(
    name="qcd_pt800to1000_pythia",
    id=14790778,
    is_data=False,
    processes=[procs.qcd_pt800to1000],
    keys=[
        "/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=108,
    n_events=39198266,
)

cpn.add_dataset(
    name="qcd_pt1000to1400_pythia",
    id=14791407,
    is_data=False,
    processes=[procs.qcd_pt1000to1400],
    keys=[
        "/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=60,
    n_events=19615910,
)

cpn.add_dataset(
    name="qcd_pt1400to1800_pythia",
    id=14801434,
    is_data=False,
    processes=[procs.qcd_pt1400to1800],
    keys=[
        "/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=5901990,
)

cpn.add_dataset(
    name="qcd_pt1800to2400_pythia",
    id=14805711,
    is_data=False,
    processes=[procs.qcd_pt1800to2400],
    keys=[
        "/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=2961265,
)

cpn.add_dataset(
    name="qcd_pt2400to3200_pythia",
    id=14791649,
    is_data=False,
    processes=[procs.qcd_pt2400to3200],
    keys=[
        "/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=1900172,
)

cpn.add_dataset(
    name="qcd_pt3200_pythia",
    id=14800342,
    is_data=False,
    processes=[procs.qcd_pt3200],
    keys=[
        "/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=699375,
)


#
# QCD (Pythia pT-binned, muon-enriched)
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22GS&nanoaod_version=v12&dataset=QCD_PT-*%28to*%29%3F_MuEnrichedPt5_TuneCP5&chained_request=Premix  # noqa

cpn.add_dataset(
    name="qcd_mu_pt15to20_pythia",
    id=14800053,
    is_data=False,
    processes=[procs.qcd_mu_pt15to20],
    keys=[
        "/QCD_PT-15to20_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=4417909,
)

cpn.add_dataset(
    name="qcd_mu_pt20to30_pythia",
    id=14809799,
    is_data=False,
    processes=[procs.qcd_mu_pt20to30],
    keys=[
        "/QCD_PT-20to30_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=71,
    n_events=30200859,
)

cpn.add_dataset(
    name="qcd_mu_pt30to50_pythia",
    id=14805426,
    is_data=False,
    processes=[procs.qcd_mu_pt30to50],
    keys=[
        "/QCD_PT-30to50_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=82,
    n_events=33440507,
)

cpn.add_dataset(
    name="qcd_mu_pt50to80_pythia",
    id=14791064,
    is_data=False,
    processes=[procs.qcd_mu_pt50to80],
    keys=[
        "/QCD_PT-50to80_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=86,
    n_events=40107069,
)

cpn.add_dataset(
    name="qcd_mu_pt80to120_pythia",
    id=14797620,
    is_data=False,
    processes=[procs.qcd_mu_pt80to120],
    keys=[
        "/QCD_PT-80to120_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=84,
    n_events=24614026,
)

cpn.add_dataset(
    name="qcd_mu_pt120to170_pythia",
    id=14791498,
    is_data=False,
    processes=[procs.qcd_mu_pt120to170],
    keys=[
        "/QCD_PT-120to170_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=88,
    n_events=18555616,
)

cpn.add_dataset(
    name="qcd_mu_pt170to300_pythia",
    id=14798613,
    is_data=False,
    processes=[procs.qcd_mu_pt170to300],
    keys=[
        "/QCD_PT-170to300_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=193,
    n_events=36864921,
)

cpn.add_dataset(
    name="qcd_mu_pt300to470_pythia",
    id=14792060,
    is_data=False,
    processes=[procs.qcd_mu_pt300to470],
    keys=[
        "/QCD_PT-300to470_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=64,
    n_events=30226277,
)

cpn.add_dataset(
    name="qcd_mu_pt470to600_pythia",
    id=14791997,
    is_data=False,
    processes=[procs.qcd_mu_pt470to600],
    keys=[
        "/QCD_PT-470to600_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=58,
    n_events=18567007,
)

cpn.add_dataset(
    name="qcd_mu_pt600to800_pythia",
    id=14800405,
    is_data=False,
    processes=[procs.qcd_mu_pt600to800],
    keys=[
        "/QCD_PT-600to800_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=107,
    n_events=19723745,
)

cpn.add_dataset(
    name="qcd_mu_pt800to1000_pythia",
    id=14808237,
    is_data=False,
    processes=[procs.qcd_mu_pt800to1000],
    keys=[
        "/QCD_PT-800to1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=86,
    n_events=39316355,
)

cpn.add_dataset(
    name="qcd_mu_pt1000_pythia",
    id=14796004,
    is_data=False,
    processes=[procs.qcd_mu_pt1000],
    keys=[
        "/QCD_PT-1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=64,
    n_events=13705539,
)


#
# QCD (Pythia pT-binned, double EM-enriched)
#

# GrASP: https://cms-pdmv-prod.web.cern.ch/grasp/samples?campaign=Run3Summer22GS&nanoaod_version=v12&dataset=QCD*EMEnriched&chained_request=Premix  # noqa

cpn.add_dataset(
    name="qcd_double_em_pt30to40_pythia",
    id=14801752,
    is_data=False,
    processes=[procs.qcd_double_em_pt30to40],
    keys=[
        "/QCD_PT-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=54,
    n_events=1425413,
)

cpn.add_dataset(
    name="qcd_double_em_pt30_pythia",
    id=14807962,
    is_data=False,
    processes=[procs.qcd_double_em_pt30],
    keys=[
        "/QCD_PT-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=2875029,
)

cpn.add_dataset(
    name="qcd_double_em_pt40_pythia",
    id=14803826,
    is_data=False,
    processes=[procs.qcd_double_em_pt40],
    keys=[
        "/QCD_PT-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=2947774,
)
