import configparser
import re


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        envs = self.config['tox']['envlist'].strip()
        return [env.strip() for env in
                re.split(r'\n|,', envs) if env]

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        py_versions = set()
        for items in self.config.values():
            basepy = items.get('basepython')
            if basepy:
                py_versions.add(basepy)
        return list(py_versions)