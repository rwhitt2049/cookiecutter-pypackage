# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

import pathlib

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"


with pathlib.Path(__file__).parent.joinpath("..", "..", "VERSION").open() as version_file:
    __version__ = version_file.read().strip()
