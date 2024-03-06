# coding: utf-8

"""
top quark datasets for the 2022 pre-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v11 import campaign_run3_2022_preEE_nano_v11 as cpn

#
# ttbar
#

# semileptonic decay
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TTtoLNu2Q%28_Hdamp-*%7C_MT-17%281%7C3%29p5%29%3F_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="tt_sl_powheg",
    id=14707480,
    is_data=False,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=67,
            n_events=80484415,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=32259560,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=32703000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=31147944,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=31624817,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=32268860,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=31853547,
        ),
        erd_on=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=31958682,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=31396674,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=32741700,
        ),
    ),
)


# dileptonic decay
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TTto2L2Nu%28_Hdamp-*%7C_MT-17%281%7C3%29p5%29%3F_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="tt_dl_powheg",
    id=14707644,
    is_data=False,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=23765566,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=9621248,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=9943000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=12,
            n_events=9824455,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=9943673,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=12,
            n_events=9831244,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=9730000,
        ),
        erd_on=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=9840000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=9372436,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=9728070,
        ),
    ),
)


# fully hadronic decay
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TTto4Q%28_Hdamp-*%7C_MT-17%281%7C3%29p5%29%3F_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="tt_fh_powheg",
    id=14708054,
    is_data=False,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=46,
            n_events=53419472,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=22548206,
        ),
        # missing as of 2023-09-16
        tune_down=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=0,
            n_events=0,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=21658498,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=23430687,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=21873176,
        ),
        # missing as of 2023-09-16
        cr_2=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=0,
            n_events=0,
        ),
        # missing as of 2023-09-16
        erd_on=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=0,
            n_events=0,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=22905616,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=22353000,
        ),
    ),
)

#
# single top (t-channel)
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=%28TBbar%7CTbarB%29Q_t-channel&chained_request=Premix  # noqa

# t-channel (top)
cpn.add_dataset(
    name="st_tchannel_t_powheg",
    id=14635077,
    is_data=False,
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=2,
            n_events=2973675,
        ),
    ),
)

# t-channel (anti-top)
cpn.add_dataset(
    name="st_tchannel_tbar_powheg",
    id=14619151,
    is_data=False,
    processes=[procs.st_tchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=2,
            n_events=1488752,
        ),
    ),
)

#
# single-top (tW-channel)
#

# semileptonic decay (top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TWminustoLNu2Q*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="st_twchannel_t_sl_powheg",
    id=14733244,
    is_data=False,
    processes=[procs.st_twchannel_t_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=4755380,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=4943120,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=4587700,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=4593174,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=4676221,
        ),
        erd_on=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=4679353,
        ),
    ),
)

# semileptonic decay (anti-top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TbarWplustoLNu2Q*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="st_twchannel_tbar_sl_powheg",
    id=14728350,
    is_data=False,
    processes=[procs.st_twchannel_tbar_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=4490791,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=4758099,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=4701783,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=4728679,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=4633416,
        ),
        erd_on=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=4680566,
        ),
    ),
)

# dileptonic decay (top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TWminusto2L2Nu*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="st_twchannel_t_dl_powheg",
    id=14678180,
    is_data=False,
    processes=[procs.st_twchannel_t_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=2435564,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=2375416,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=2385737,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=2492355,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=2497224,
        ),
        erd_on=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=2414112,
        ),
    ),
)

# dileptonic decay (anti-top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TbarWplusto2L2Nu*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="st_twchannel_tbar_dl_powheg",
    id=14690995,
    is_data=False,
    processes=[procs.st_twchannel_tbar_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=2401536,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=2395750,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=2,
            n_events=2422160,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=2425480,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=2496520,
        ),
        erd_on=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=2463496,
        ),
    ),
)


# fully hadronic decay (top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TWminusto4Q*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="st_twchannel_t_fh_powheg",
    id=14691168,
    is_data=False,
    processes=[procs.st_twchannel_t_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=3924210,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=3853959,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=3822520,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=3800301,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=3862996,
        ),
        erd_on=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=3819100,
        ),
    ),
)


# fully hadronic decay (anti-top)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&nanoaod_version=v11&dataset=TbarWplusto4Q*_TuneCP5%28%7CUp%7CDown%7CCR1%7CCR2%29_13p6TeV&chained_request=Premix  # noqa
cpn.add_dataset(
    name="st_twchannel_tbar_fh_powheg",
    id=14691156,
    is_data=False,
    processes=[procs.st_twchannel_tbar_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=3957160,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=3986080,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=3971608,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=3823795,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=3862163,
        ),
        erd_on=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=3897400,
        ),
    ),
)
