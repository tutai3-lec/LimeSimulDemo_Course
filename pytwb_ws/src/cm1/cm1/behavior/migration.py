import time

from lib.actor_bt import ActorBT
from pytwb.common import behavior

import py_trees
from threading import Semaphore

@behavior
class Approach(ActorBT):
    desc = 'approach target by visual feedback'

    def __init__(self, name, node, target=0.20):
        super().__init__(name, 'approach', target)
    
    def initialise(self):
        time.sleep(1)
        super().initialise()

@behavior
class Mini_Walk(ActorBT):
    desc = 'approach target by specified time'

    def __init__(self, name, node, target=1):
        super().__init__(name, 'mini_walk', target)

@behavior
class Shift(ActorBT):
    desc = 'approach target by specified len'

    def __init__(self, name, node, target=0.006):
        super().__init__(name, 'shift', target)

@behavior
class ReachCoke(ActorBT):
    desc = 'approach cola can'

    def __init__(self, name, node):
        super().__init__(name, 'reach_coke')

@behavior
class Face(ActorBT):
    desc = 'direct face to the coke can'

    def __init__(self, name, node):
        super().__init__(name, 'face')

@behavior
class CheckCoke(ActorBT):
    desc = 'check whether coke exists'

    def __init__(self, name, node):
        super().__init__(name, 'check_coke')
    
    def initialise(self):
        super().initialise()

@behavior
class SetDetector(ActorBT):
    desc = 'approach target by specified len'

    def __init__(self, name, node, func_name):
        super().__init__(name, 'set_detector', func_name)