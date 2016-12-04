#!/usr/bin/python
# -*- coding: utf-8 -*-
from .base import Base
from transaction import Transaction
__author__ = '@elinaldosoft'


class Block(Base):
    _id = str
    prev_id = str

    def transactions(self, query=dict):
        pipe = [
            {'$match': query},
            {'$lookup': {
                'from': 'transactions',
                'localField': '_id',
                'foreignField': 'on_block_id',
                'as': 'transactions'
                }
            }
        ]
        return self.collection.aggregate(pipeline=pipe)

    def get_biggest_foo_on_block(self, block_id=str):
        transactions = [x for x in self.transactions({'_id': block_id})]
        if transactions:
            lst_transactions = [t.get('foo') for t in transactions[0].get('transactions')]
            return max(lst_transactions)
        else:
            raise ValueError('Not exist block or transactions to key %s' % block_id)

    def count_transactions_until_end(self, block_id=str):
        count = 0
        transactions = [x for x in self.transactions({'_id': block_id})]
        if transactions:
            prev_id = transactions[0].get('prev_id')
            NEXT = True
            count += len(transactions[0].get('transactions'))

            while NEXT:
                _id = self.find_by({'_id': prev_id})

                if _id and _id.get('prev_id'):
                    result = [x for x in self.transactions({'_id': _id.get('prev_id')})]
                    prev_id = result[0].get('prev_id')
                    count += len(result[0].get('transactions'))
                else:
                    NEXT = False

            return count
        else:
            raise ValueError('Not exist block or transactions to key %s' % block_id)