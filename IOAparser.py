#!/usr/bin/python3.5


import argparse
import logging
import sys
import io
import itertools as IT
import xml.etree.ElementTree as ET

class Variable(object):
    def __init__(self, varname, datatype, initial_value, possible_values):
        self.varname = varname
        self.datatype = datatype
        self.initial_value = initial_value
        self.possible_values = possible_values

    def set_varname(self, varname):
        self.varname = varname

    def set_datatype(self, datatype='boolean'):
        self.datatype = datatype

class Element(object):
    def __init__(self, ename, datatype, initial_value, possible_values):
        self.ename = ename
        self.datatype = datatype
        self.initial_value = initial_value
        self.possible_values = possible_values

    def set_varname(self, ename):
        self.ename = ename

    def set_datatype(self, datatype='boolean'):
        self.datatype = datatype

class Message(object):
    def __init__(self,message_label,elements):
        self.messagename = message_label
        elements = []
        for element in elements:
            self.elements.append(element)

    def set_elements(self,elements):
        elements = []
        for element in elements:
            self.elements.append(element)

    def add_element(self,element):
        self.elements.append(element)


class Action(object):
    def __init__(self, action_label, content):
        self.action_label = action_label
        self.content = content

class Transition(object):
    def __init__(self, transition_label, start, end, condition, actions):
        self.transition_label = transition_label
        self.start = start
        self.end = end
        self.condition = condition
        self.actions = actions
        self.contending_transitions = []
    def set_contending_transitions(self, contending_transitions):
        self.contending_transitions = contending_transitions


class Automaton(object):
    def __init__(self, name, signature, state, transitions):
        self.name = name
        self.state = state
        self.signature = signature
        self.transitions = transitions

    def set_states(self,states):
        states = []
        for state in states:
            self.states.append(state)

    def add_state(self,state):
        self.states.append(state)

def parseIOA(ioafile):
    tree = ET.parse(ioafile)
    # get root element
    root = tree.getroot()

    # store the parsing results
    msgs = []
    automata = []

    # parse messages
    for msg in root.iter('Message'):
        msg_name = str(msg.attrib['label']).strip()

        # parse elements
        msg_elements = []
        elements = msg.find('Elements')
        if (msg.find('Elements')):
            for element in elements:
                msg_element = Element(element)
                msg_elements.append(msg_element)

        new_msg = Message(msg_name, elements)
        msgs.append(new_msg)

    # parse FSMs
    for ioa in root.iter('Automaton'):
        ioa_name = str(ioa.attrib['label']).strip()
        # parse signatures
        inputs = ioa.find('Inputs')
        ioa_signatures = []

        for input in inputs:
            action_label = str(input.attrib['label']).strip()
            content = input.text
            action = Action(action_label, content)
            ioa_signatures.append(action)

        outputs = ioa.find('Outputs')

        for output in outputs:
            action_label = str(output.attrib['label']).strip()
            content = output.text
            action = Action(action_label, content)
            ioa_signatures.append(action)

        # parse states
        ioa_states = []

        # parse transitions
        transitions = ioa.find('Transitions')
        ioa_transitions = []
        if (ioa.find('transitions')):
            for transition in transitions:
                action = transition.find('Action')
                precondition = transition.find('Precondition')
                effect = transition.find('Effect')

        new_ioa = Automaton(ioa_name,ioa_signatures,ioa_states,ioa_transitions)
        automata.append(new_ioa)

