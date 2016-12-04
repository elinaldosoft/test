#!/usr/bin/python
# -*- coding: utf-8 -*-
from .base import Base

__author__ = '@elinaldosoft'


class Transaction(Base):
    _id = str
    on_block_id = str
    foo = str
