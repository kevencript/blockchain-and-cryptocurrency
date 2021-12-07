#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import hashlib
import json
from flask import Flask, jsonify


class Blockchain:
    def __init__(self):
        self.chain = []
        self.createBlock(proof=1, previous_hash='0')

    def createBlock(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }

        self.chain.append(block)
        return block

    def getPreviusBlock(self):
        return self.chain[-1]

    def proofOfWork(self, previous_proof):
        newProof = 1
        checkProof = False

        while checkProof == False:
            hashOperation = hashlib.sha256(
                str(newProof**2 - previous_proof**2).enconde()).hexdigest()
            if hashOperation[:4] == '0000':
                checkProof = True
            else:
                newProof += 1

        return newProof
