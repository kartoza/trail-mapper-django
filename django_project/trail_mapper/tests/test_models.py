# coding=utf-8
"""Test for models."""

from django.test import TestCase
from .model_factories import (
    CategoryFactory,
    GradeFactory,
    PointOfInterestFactory,
    TrailFactory,
    TrailSectionFactory,
    TrailSectionsFactory
    )

class TestCategory(TestCase):
    """Test category model."""

    def setUp(self):
        """Set up before each test."""

        pass

    def test_category_create(self):
        """Test category model creation."""

        model = CategoryFactory.create()

        # check if primary key exists.
        self.assertTrue(model.pk is not None)

        # check if model name exists.
        self.assertTrue(model.name is not None)

    def test_category_delete(self):
        """Test category model deletion."""

        # noinspection PyArgumentList
        model = CategoryFactory._create()
        model.delete()

        # check if deleted
        self.assertTrue(model.pk is None)

    def test_category_read(self):
        """Test category model read."""

        # noinspection PyArgumentList
        model = CategoryFactory._create(
            name=u'Category update'
        )

        self.assertTrue(model.name == 'Category update')

    def test_category_update(self):
        """Test category update."""

        # noinspection PyArgumentList
        model = CategoryFactory._create()
        new_model_data = {
            'guid' : u'34ebcde5-91c4-4b6b-b98e-da7e7942e46c',
            'name' : u'new category name',
            'image' : u'',
        }

        model.__dict__.update(new_model_data)
        model.save()

        # check if updated
        # noinspection PyCompatibility,PyTypeChecker
        for key, val in new_model_data.iteritems():
            self.assertEqual(model.__dict__.get(key), val)


class TestGrade(TestCase):
    """Test Grade model."""

    def setUp(self):
        """Set up before test."""

        pass

    def test_grade_create(self):
        """Test grade model creation."""

        model = GradeFactory.create()

        # check if primary key exists
        self.assertTrue(model.pk is not None)

        # check if model name exists
        self.assertTrue(model.name is not None)

    def test_grade_delete(self):
        """Test for model deletion"""

        # noinspection PyArgumentList
        model = GradeFactory._create()
        model.delete()

        # check if deleted
        self.assertTrue(model.pk is None)

    def test_grade_read(self):
        """Check for grade model read."""

        model = GradeFactory.create(
            guid=u'34ebcde5-91c4-4b6b-b98e-da7e7942e46c'
        )

        # check if guid exists
        self.assertTrue(model.guid == '34ebcde5-91c4-4b6b-b98e-da7e7942e46c')

    def test_grade_update(self):
        """Test grade update."""

        model = GradeFactory.create()
        new_model_data = {
            'guid': u'34ebcde5-91c4-4b6b-b98e-da7e7942e46c',
            'name': u'new category name',
            'image': u'',
        }
        model.__dict__.update(new_model_data)
        model.save()

        # check if updated
        # noinspection PyCompatibility,PyTypeChecker
        for key, val in new_model_data.iteritems():
            self.assertEqual(model.__dict__.get(key), val)


class TestPointOfIntersection(TestCase):
    """Test point of intersection model."""

    def setUp(self):
        """Set up before tests."""

        pass

    def test_point_of_intersection_create(self):
        """Test for point of intersection creation."""

        model = PointOfInterestFactory.create()

        # check if primary key exists
        self.assertTrue(model.pk is not None)

        # check if model guid exists
        self.assertTrue(model.guid is not None)

    def test_point_of_intersection_delete(self):
        """Test for point of intersection deletion."""

        model = PointOfInterestFactory.create()
        model.delete()

        # check if deleted
        self.assertTrue(model.pk is None)

    def test_point_of_intersection_read(self):
        """Test for point of intersection read."""

        model = PointOfInterestFactory.create(
            guid=u'34ebcde5-91c4-4b6b-b98e-da7e7942e46c'
        )

        # check if guid was created
        # noinspection PyArgumentList
        self.assertEqual(
            model.guid == '34ebcde5-91c4-4b6b-b98e-da7e7942e46c'
        )


    def test_point_of_intersection_update(self):
        """Test for point of intersection update."""

        model = PointOfInterestFactory.create()
        new_model_data = {
            'guid': u'34ebcde5-91c4-4b6b-b98e-da7e7942e46c',
            'name': u'new category name',
            'notes': u'test notes',
            'image': u'',
        }

        # save model instance
        model.__dict__.update(new_model_data)
        model.save()

        # check if updated
        # noinspection PyCompatibility,PyTypeChecker
        for key, val in new_model_data.iteritems():
            self.assertEqual(model.__dict__.get(key), val)


class TestTrail(TestCase):
    """Test Trail Model."""

    def setUp(self):
        """Set up before tests."""

        pass

    def test_trail_create(self):
        """Test trail creation."""

        model = TrailFactory.create()
        model.save()

        # check if primary key exists
        self.assertTrue(model.pk is not None)

    def test_trail_delete(self):
        """Test trail deletion."""

        model = TrailFactory.create()
        model.delete()

        # check if deleted
        self.assertTrue(model.pk is None)

    def test_trail_read(self):
        """Test trail read."""

        model = TrailFactory.create(
            guid=u'34ebcde5-91c4-4b6b-b98e-da7e7942e46c'
        )

        # check if guid exists
        # noinspection PyArgumentList
        self.assertEqual(
            model.guid == '34ebcde5-91c4-4b6b-b98e-da7e7942e46c'
        )

    def test_trail_update(self):
        """Test trail update."""

        model = TrailFactory.create()
        new_model_data = {
            'guid': u'34ebcde5-91c4-4b6b-b98e-da7e7942e46c',
            'name': u'new category name',
            'notes': u'test notes',
            'image': u'',
            'colour': u'',
            'offset': u'',
        }

        # save model instance
        model.__dict__.update(new_model_data)
        model.save()

        # check if updated
        # noinspection PyCompatibility,PyTypeChecker
        for key, val in new_model_data.iteritems():
            self.assertEqual(model.__dict__.get(key), val)


class TestTrailSection(TestCase):
    """Test trail section model."""

    def setUp(self):
        """Set up before tests."""

        pass

    def test_trail_section_create(self):
        """Test trail section creation."""

        model = TrailSectionFactory.create()
        model.save()

        # check if primary key exists
        self.assertTrue(model.pk is not None)

    def test_trail_section_delete(self):
        """Test trail section deletion."""

        model = TrailSectionFactory.create()
        model.delete()

        # check if deleted
        self.assertTrue(model.pk is None)

    def test_trail_section_read(self):
        """Test trail section read."""

        model = TrailSectionFactory.create(
            guid=u'34ebcde5-91c4-4b6b-b98e-da7e7942e46c'
        )

        # check if guid was read
        # noinspection PyArgumentList
        self.assertEqual(
            model.guid == '34ebcde5-91c4-4b6b-b98e-da7e7942e46c'
        )

    def test_trail_section_update(self):
        """Test trail section deletion."""

        model = TrailSectionFactory.create()
        new_model_data = {
            'guid': u'34ebcde5-91c4-4b6b-b98e-da7e7942e46c',
            'name': u'new category name',
            'notes': u'test notes',
            'image': u'',
        }

        # save model instance
        model.__dict__.update(new_model_data)
        model.save()

        # check if updated
        # noinspection PyCompatibility,PyTypeChecker
        for key, val in new_model_data.iteritems():
            self.assertEqual(model.__dict__.get(key), val)


class TestTrailSections(TestCase):
    """Test trail sections model."""

    def setUp(self):
        """Set up before tests."""

        pass

    def test_trail_sections_create(self):
        """Test for trail sections creation."""

        model = TrailSectionsFactory.create()
        model.save()

        # check if created and primary key exists
        self.assertTrue(model.pk is not None)

    def test_trail_sections_delete(self):
        """Test for trail sections deletion."""

        model = TrailSectionsFactory.create()
        model.delete()

        # check if deleted
        self.assertTrue(model.pk is None)

    def test_trail_sections_read(self):
        """Test trial sections read."""

        model = TrailSectionsFactory.create(
            order=u'test odering'
        )

        # check if order was read
        # noinspection PyArgumentList
        self.assertEqual(model.order == 'test ordering')

    def test_trail_sections_update(self):
        """Test trail sections update."""

        model = TrailSectionsFactory.create()
        new_model_date = {
            'order': u'test ordering',
        }

        # save model data
        model.__dict__.update(new_model_date)
        model.save()

        # check if updated
        # noinspection PyCompatibility,PyTypeChecker
        for key, val in new_model_date.iteritems():
            self.assertEqual(model.__dict__.get(key), val)
