import uuid

import factory.fuzzy
import factory.django


class FuzzyEmail(factory.fuzzy.FuzzyText):

    def fuzz(self):
        return super(FuzzyEmail, self).fuzz() + "@example.com"


class FuzzyUUID(factory.fuzzy.BaseFuzzyAttribute):

    def fuzz(self):
        return uuid.uuid4()


class SmartModelFactory(factory.django.DjangoModelFactory):
    created_by = factory.SubFactory("tracpro.test.factories.User")
    modified_by = factory.SubFactory("tracpro.test.factories.User")

    class Meta:
        abstract = True
