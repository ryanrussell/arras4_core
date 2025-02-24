# Copyright 2023 DreamWorks Animation LLC and Intel Corporation
# SPDX-License-Identifier: Apache-2.0

# -*- coding: utf-8 -*-
import sys

name = 'arras4_core'

@early()
def version():
    """
    Increment the build in the version.
    """
    _version = '4.10.2'
    from rezbuild import earlybind
    return earlybind.version(this, _version)

description = 'Arras Core'

authors = ['Dreamworks Animation R&D - JoSE Team',
           'psw-jose@dreamworks.com',
           'rob.wilson@dreamworks.com']

help = ('For assistance, '
        "please contact the folio's owner at: psw-jose@dreamworks.com")

if 'cmake' in sys.argv:
    build_system = 'cmake'
    build_system_pbr = 'cmake_modules'
else:
    build_system = 'scons'
    build_system_pbr = 'bart_scons-10'

variants = [
    ['os-CentOS-7', 'refplat-vfx2019.3'],
    ['os-CentOS-7', 'refplat-vfx2020.3'],
    ['os-CentOS-7', 'refplat-vfx2021.0'],
    ['os-CentOS-7', 'refplat-vfx2022.0']
]

sconsTargets = {}
for variant in variants:
    sconsTargets[variant[0]] = ['@install', '@doxygen']

requires = [
    'uuid-1.0.0',
    'boost',
    'curl_no_ldap-7.49.1',
    'jsoncpp-0.6.0',
    'libmicrohttpd-0.9.37.x.0'
]

private_build_requires = [
    build_system_pbr,
    'cppunit', 
    'gcc'
]

if build_system is 'cmake':
    def commands():
        prependenv('CMAKE_MODULE_PATH', '{root}/lib64/cmake')
        prependenv('LD_LIBRARY_PATH', '{root}/lib64')
        prependenv('PATH', '{root}/bin')
        prependenv('ARRAS_SESSION_PATH', '{root}/sessions')
else:
    def commands():
        prependenv('LD_LIBRARY_PATH', '{root}/lib')
        prependenv('PATH', '{root}/bin')
        prependenv('ARRAS_SESSION_PATH', '{root}/sessions')

uuid = '2625d822-f8b4-4e3d-8106-007c2b9f42c2'

config_version = 0
