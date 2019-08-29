# coding=utf-8
"""Factories for building model instances for testing."""

import datetime
import factory.fuzzy
import factory

from ..models import (
    Category,
    Grade,
    Trail,
    TrailSection,
    TrailSections,
    PointOfInterest
)


class CategoryFactory(factory.django.DjangoModelFactory):
    """Category model factory."""

    class Meta:
        model = Category

    guid = factory.sequence(lambda n:'f23edf34-0530-4973-b094-a42f4e596a2b %s' % n)
    name = factory.sequence(lambda n:'Test category name %s' % n)
    image = factory.django.ImageField(colour='green')


class GradeFactory(factory.django.DjangoModelFactory):
    """Grade model factory."""

    class Meta:
        model = Grade

    guid = factory.sequence(lambda n:'f23edf34-0530-4973-b094-a42f4e596a2b %s' % n)
    name = factory.sequence(lambda n:'Test grade name %s' % n)
    image = factory.django.ImageField(colour='green')


class PointOfInterestFactory(factory.django.DjangoModelFactory):
    """PointOfInterest model factory."""

    class Meta:
        model = PointOfInterest

    guid = factory.sequence(lambda n:'f23edf34-0530-4973-b094-a42f4e596a2b %s' % n)
    name = factory.sequence(lambda n:'Test point of interest name %s' % n)
    notes = u'This is a description just for testing'
    image = factory.django.ImageField(colour='green')
    category = factory.SubFactory(Category)
    trail_section = factory.SubFactory(TrailSection)


class TrailFactory(factory.django.DjangoModelFactory):
    """Trail model factory."""

    class Meta:
        model = Trail

    guid = factory.sequence(lambda n:'f23edf34-0530-4973-b094-a42f4e596a2b %s' % n)
    name = factory.sequence(lambda n:'Test trail name %s' % n)
    image = factory.django.ImageField(colour='green')
    notes = u'This is a description just for testing'
    colour = factory.sequence(lambda n:'#00FF00 %s' % n)


class TrailSectionFactory(factory.django.DjangoModelFactory):
    """TrailSection model factory."""

    class Meta:
        model = TrailSection

    guid = factory.sequence(lambda n:'f23edf34-0530-4973-b094-a42f4e596a2b %s' % n)
    name = factory.sequence(lambda n:'Test trail section name %s' % n)
    notes = u'This is a description just for testing'
    image = factory.django.ImageField(colour='green')
    grade = factory.SubFactory(Grade)
    start_date = factory.fuzzy.FuzzyDate(datetime.date(2014, 1, 1))
    end_date = factory.fuzzy.FuzzyDate(datetime.date(2015, 1, 1))


class TrailSectionsFactory(factory.django.DjangoModelFactory):
    """TrailSections model factory."""

    class Meta:
        model = TrailSections

    order = factory.sequence(lambda n:'Test order name %s' % n)
    trail = factory.SubFactory(Trail)
    trail_section = factory.SubFactory(TrailSection)
