import random
from pymongo import MongoClient


def wipe_db(db):
    for collection in db.collection_names():
        db[collection].delete_many({})


def random_id():
    return u''.join(random.choice(u"abcdefghijklmnopqrstuvwxyz") for _ in xrange(random.randint(7, 15)))


def generate_blockchain(db, n):
    prev_id = None
    for i in xrange(n):
        print "Inserting block %d..." % (i,)

        new_id = random_id()
        db.blocks.insert_one({'_id': new_id, 'prev_id': prev_id})

        for j in xrange(random.choice([0, 0, 0, 1, 1, 2, 5, 10])):
            major = random.choice([0, 0, 0, 0, 1])
            db.transactions.insert_one({
                '_id': random_id(),
                'on_block_id': new_id,
                'foo': random.randint(0, 100000) + (random.randint(999999999, 9999999999) if major else 0),
            })

        prev_id = new_id


def regenerate_test_db(db):
    wipe_db(db)

    db.blocks.create_index('prev_id')
    db.transactions.create_index('on_block_id')
    db.transactions.create_index('foo')

    random.seed(100)  # keep the same!! so tests have same results!!
    generate_blockchain(db, 100)


if __name__ == '__main__':
    cli = MongoClient('localhost')
    db = cli.testdb

    regenerate_test_db(db)