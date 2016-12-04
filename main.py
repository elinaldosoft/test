#!/usr/bin/python
# -*- coding: utf-8 -*-
from models.block import Block

__author__ = '@elinaldosoft'

block = Block()

#Question 01
assert block.get_biggest_foo_on_block('zudaqyoeifkhxf') == 87496
assert block.get_biggest_foo_on_block('cwuongmqavu') == 83106
assert block.get_biggest_foo_on_block('upqbtjs') == 4242560329

try:
    print block.get_biggest_foo_on_block('tlunclbyyiitf')
    raise RuntimeError("Should have thrown value error")
except ValueError:
    pass


#Question 02
# assert block.count_transactions_until_end('jdezobkfbyeohh') == 24 #83
# assert block.count_transactions_until_end('imdgclrljvhqrhg') == 12 #90
# assert block.count_transactions_until_end('mocexgqtln') == 1 #106

assert block.count_transactions_until_end('qljwzrt') == 24
assert block.count_transactions_until_end('mtvxqgwxst') == 1

try:
    print block.count_transactions_until_end('not a block id')
    raise RuntimeError("Should have thrown value error")
except ValueError:
    pass