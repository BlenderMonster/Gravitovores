'''
mbge.context
============

This module provides access to the context
the current code is running in.
'''
import types
import sys
import bge

@property
def controller(self):
    'the current controller (readonly)'
    return bge.logic.getCurrentController()

@property
def owner(self):
    'the current controller''s owner (readonly)'
    return bge.logic.getCurrentController().owner

@property
def scene(self):
    'the current scene (readonly)'
    return bge.logic.getCurrentScene()

@property
def scenes(self):
    'the current scenes (readonly)'
    return bge.logic.getSceneList()

import mprop; mprop.init()