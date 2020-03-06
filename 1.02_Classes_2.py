''' Code orriginal qui import MODEL
    Il y a un probleme avec l imporation
    '''

import datetime
from pymodel import *

class Country(Model):
    name = Property(unicode)    # any Python type; default is unicode

    def __unicode__(self):
        return self.name

    class Meta:
        must_have = {'type': 'country'}

class Person(Model):
    first_name = Property(required=True)
    last_name = Property(required=True)
    gender = Property()
    birth_date = Date()
    birth_place = Property(Country)    # reference to another model

    def __unicode__(self):
        return self.full_name    # full_name is a dynamic attr, see below

    @property
    def age(self):
        return (datetime.datetime.now().date() - self.birth_date).days / 365

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        must_have = {'first_name__exists': True, 'last_name__exists': True}
