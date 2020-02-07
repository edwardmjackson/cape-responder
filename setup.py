# Copyright 2018 BLEMUNDSBURY AI LIMITED
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from package_settings import NAME, VERSION, PACKAGES, DESCRIPTION
from setuptools import setup
from pathlib import Path 

setup(
    name=NAME,
    version=VERSION,
    long_description=DESCRIPTION,
    author='Bloomsbury AI',
    author_email='contact@bloomsbury.ai',
    packages=PACKAGES,
    include_package_data=True,
    install_requires=['dask==0.15.4',
                      'distributed==1.19.2',
                      'numpy==1.15.0',
                      'pytest==3.6.4',
                      'cape_machine_reader @ git+https://github.com/edwardmjackson/cape-machine-reader',
                      'cape_document_manager @ git+https://github.com/edwardmjackson/cape-document-manager',
                      'cape_document_qa @ git+https://github.com/edwardmjackson/cape-document-qa'
    ],
    package_data={
        '': ['*.*'],
    },
)
