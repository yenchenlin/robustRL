"""
    Add the environment you wish to train here
"""

import gym
import numpy as np
from rllab.envs.gym_env import GymEnv


def make_train_MDP():
    return _make_standard_MDP()


def make_test_MDP():
    return _make_heavy_MDP()


def make_custom_MDP():
    return _draw_random_MDP()


def _make_standard_MDP():
    e = GymEnv('Hopper-v1')
    return e


def _make_heavy_MDP():
    e = GymEnv("Hopper-v1")
    bm = np.array(e.env.model.body_mass)
    gs = np.array(e.env.model.geom_size)
    bm[1] = 7; gs[1][0] = 0.1;
    e.env.model.body_mass = bm; e.env.model.geom_size = gs;
    return e


def _make_random_MDP():
    e = GymEnv("UncertainHopper-v0")

    return e


# =======================================================================================
# Generate environment corresponding to the given mode

def get_environment(env_mode):

    modes = ['train', 'test', 'custom', 'standard', 'heavy', 'random']    

    if env_mode == 'train':
        env = make_train_MDP()
    elif env_mode == 'test':
        env = make_test_MDP()
    elif env_mode == 'custom':
        env = make_custom_MDP()
    elif env_mode == 'standard':
        env = _make_standard_MDP()
    elif env_mode == 'heavy':
        env = _make_heavy_MDP()
    elif env_mode == 'random':
        env = _make_random_MDP()
    else:
        print "ERROR: Unknown environment mode specified. Allowed modes are ", modes

    return env
