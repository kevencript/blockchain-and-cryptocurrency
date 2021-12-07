#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import hashlib
import json
from flask import Flask, jsonify


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }

        self.chain.append(block)
        return block

    def get_previus_block(self):
        return self.chain[-1]

    def hash_operation(self, previous_proof, new_proof):
        return hashlib.sha256(
            str(new_proof**2 - previous_proof**2).enconde()).hexdigest()

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof == False:
            hashed = self.hash_operation(previous_proof, new_proof)

            if hashed[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1

        return new_proof

    def hash(self, block):
        encoded = json.dumps(block, sort_keys=True).enconde()
        return hashlib.sha256(encoded).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False

            previous_proof = previous_block['proof']
            proof = block['proof']
            hashed = self.hash_operation(previous_proof, proof)
            if hashed[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
