import os.path as osp
import yaml


ROOT = osp.dirname(osp.dirname(osp.abspath(__file__)))
CFG_FILE = osp.join(ROOT, "defaults.yaml")


def load_cfg(cfg_file=None):
    """
    Load the config file.

    :param cfg_file: the path to the config file containing default overrides
    :return: the config dictionary
    """
    # load the default config file
    with open(CFG_FILE) as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)

    # load the config file if it exists
    if cfg_file is not None:
        if not osp.exists(cfg_file):
            raise ValueError(f"Config file '{cfg_file}' does not exist.")
        with open(cfg_file) as f:
            cfg.update(yaml.load(f, Loader=yaml.FullLoader))

    # user, format, style
    user = cfg.get("user")
    fmts = cfg.get("format")
    style = cfg.get("style")

    return user, fmts, style
