# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2023 Intel Corporation
#                    Mariusz Zaborski <oshogbo@invisiblethingslab.com>

import click

from ..common.builder import GramineBuilder
from ...utils import gramine_option_prompt

class JavaBuilder(GramineBuilder):
    def __init__(self, project_dir, sgx, sgx_key, jar, main_class):
        super().__init__(project_dir, sgx, sgx_key)
        self.jar = jar
        self.main_class = main_class

    def get_framework_name(self):
        return 'java'

    def get_templates_extras_vars(self):
        return {
            'jar': self.jar,
            'main_class': self.main_class,
        }

    @staticmethod
    def cmdline_setup_parser(project_dir, sgx, sgx_key):
        @click.command()
        @gramine_option_prompt('--jar', required=True, type=str,
            prompt="JAR filename (found in target/)")
        @gramine_option_prompt('--main_class', required=True, type=str,
            prompt="Main class name")
        def click_parser(jar, main_class):
            return JavaBuilder(project_dir, sgx, sgx_key, jar, main_class)
        return click_parser

def builder_java():
    return JavaBuilder
