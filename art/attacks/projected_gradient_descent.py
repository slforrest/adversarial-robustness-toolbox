from __future__ import absolute_import, division, print_function, unicode_literals

import logging

import numpy as np

from art.attacks import BasicIterativeMethod

logger = logging.getLogger(__name__)


class ProjectedGradientDescent(BasicIterativeMethod):
    """
    The Projected Gradient Descent attack is a variant of the Basic Iterative Method in which,
    after each iteration, the perturbation is projected on an lp-ball of specified radius (in
    addition to clipping the values of the adversarial sample so that it lies in the permitted
    data range). This is the attack proposed by Madry et al. for adversarial training.
    Paper link: https://arxiv.org/abs/1706.06083
    """
    attack_params = BasicIterativeMethod.attack_params


    def __init__(self, classifier, expectation_over_transformations=None, norm=np.inf, eps=.3, eps_step=0.1, 
                 max_iter=20, targeted=False, random_init=False, batch_size=128):
        """
        Create a :class:`ProjectedGradientDescent` instance.

        :param classifier: A trained model.
        :type classifier: :class:`Classifier`
        :param expectation_over_transformations: An expectation over transformations to be applied when computing 
                                                 classifier gradients.
        :type expectation_over_transformations: :class:`ExpectationOverTransformations`
        :param norm: Order of the norm. Possible values: np.inf, 1 or 2.
        :type norm: `int`
        :param eps: Maximum perturbation that the attacker can introduce.
        :type eps: `float`
        :param eps_step: Attack step size (input variation) at each iteration.
        :type eps_step: `float`
        :param targeted: Should the attack target one specific class
        :type targeted: `bool`
        :param random_init: Whether to start at the original input or a random point within the epsilon ball
        :type random_init: `bool`
        :param batch_size: Batch size
        :type batch_size: `int`
        """
        super(ProjectedGradientDescent, self).__init__(classifier, norm=norm, eps=eps, eps_step=eps_step,
                                                       max_iter=max_iter, targeted=targeted, random_init=random_init,
                                                       batch_size=batch_size)

        self._project = True
