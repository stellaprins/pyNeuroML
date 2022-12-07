#!/usr/bin/env python3
"""
Tests for pyneuroml.archive module

File: test_archive.py

Copyright 2022 NeuroML contributors
"""


import unittest
import logging
import pathlib

from pyneuroml.archive import (
    get_model_file_list,
    create_combine_archive,
    create_combine_archive_manifest,
)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class TestArchiveModule(unittest.TestCase):

    """Test the pyneuroml.archive module."""

    def test_get_model_file_list(self):
        """Test get_model_file_list."""
        # a NeuroML file in the tests directory
        thispath = pathlib.Path(__file__)
        dirname = str(thispath.parent.parent)
        filelist = []
        get_model_file_list("HH_example_cell.nml", filelist, dirname)
        self.assertEqual(4, len(filelist))

        # a LEMS file in the examples directory
        dirname = str(thispath.parent.parent.parent)
        filelist = []
        get_model_file_list(
            "LEMS_NML2_Ex5_DetCell.xml", filelist, dirname + "/examples"
        )
        self.assertEqual(5, len(filelist))

        # NeuroML file in examples directory
        dirname = str(thispath.parent.parent.parent)
        filelist = []
        get_model_file_list(
            "NML2_SingleCompHHCell.nml", filelist, dirname + "/examples"
        )
        self.assertEqual(4, len(filelist))

    def test_create_combine_archive_manifest(self):
        """Test create_combine_archive_manifest function."""
        thispath = pathlib.Path(__file__)
        dirname = str(thispath.parent.parent)
        filelist = []
        get_model_file_list("HH_example_cell.nml", filelist, dirname)
        create_combine_archive_manifest("HH_example_cell.nml", filelist, dirname)
        self.assertTrue(pathlib.Path(dirname + "/manifest.xml").exists())

        # a LEMS file in the examples directory
        dirname = str(thispath.parent.parent.parent)
        filelist = []
        get_model_file_list(
            "LEMS_NML2_Ex5_DetCell.xml", filelist, dirname + "/examples"
        )
        create_combine_archive_manifest(
            "LEMS_NML2_Ex5_DetCell.xml", filelist, dirname + "/examples"
        )
        self.assertTrue(pathlib.Path(dirname + "/examples/manifest.xml").exists())

        # NeuroML file in examples directory
        dirname = str(thispath.parent.parent.parent)
        filelist = []
        get_model_file_list(
            "NML2_SingleCompHHCell.nml", filelist, dirname + "/examples"
        )
        create_combine_archive_manifest(
            "NML2_SingleCompHHCell.nml", filelist, dirname + "/examples"
        )
        self.assertTrue(pathlib.Path(dirname + "/examples/manifest.xml").exists())

    def test_create_combine_archive(self):
        """Test create_combine_archive."""

        thispath = pathlib.Path(__file__)
        filelist = []
        dirname = str(thispath.parent.parent)
        create_combine_archive("HH_example", dirname + "/HH_example_cell.nml",
                               filelist=filelist)
        self.assertTrue(pathlib.Path(dirname + "/HH_example.neux").exists())

        dirname = str(thispath.parent.parent.parent)
        filelist = []
        create_combine_archive(
            "LEMS_NML2_Ex5_DetCell", dirname + "/examples/LEMS_NML2_Ex5_DetCell.xml", filelist=filelist
        )
        self.assertTrue(
            pathlib.Path(dirname + "/examples/LEMS_NML2_Ex5_DetCell.neux").exists()
        )

        dirname = str(thispath.parent.parent.parent)
        filelist = []
        create_combine_archive(
            "NML2_SingleCompHHCell", dirname + "/examples/NML2_SingleCompHHCell.nml",
            filelist=filelist
        )
        self.assertTrue(
            pathlib.Path(dirname + "/examples/NML2_SingleCompHHCell.neux").exists()
        )
