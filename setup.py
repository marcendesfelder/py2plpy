import setuptools

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(name='py2plpy',
                version='0.2.1',
                description='Convert python function to postgresql plpython functions',
                long_description=long_description,
                long_description_content_type='text/markdown',
                url='',
                author='Marc Endesfelder',
                author_email='marc@endesfelder.de',
                license='MIT',
                packages=setuptools.find_packages(),
                entry_points = {
                    'console_scripts': ['py2plpy=py2plpy.command_line:main'],
                },
                classifiers=[
                    'Development Status :: 4 - Beta',
                    'Programming Language :: Python :: 3',
                    'License :: OSI Approved :: MIT License',
                    'Operating System :: OS Independent',
                    'Intended Audience :: Developers',
                    'Programming Language :: PL/SQL',
                    'Topic :: Database :: Database Engines/Servers',
                    'Topic :: Database',
                    'Topic :: Software Development :: Code Generators'
                ],
                install_requires=[],)
