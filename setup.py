from setuptools import setup

setup(
    name='forkfeed',
    version='0.1.2',
    description='Utility do build atom feeds for all commits in all forks of your projects on GitHub.',
    author='Alexander Artemenko',
    author_email='svetlyak.40wt@gmail.com',
    scripts=['forkfeed'],
    install_requires=[
        'github2>=0.2.0',
        'feedgenerator>=1.2.1',
        'opster>=2.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Version Control',
    ],
    keywords='git github fork forks atom rss feed',
)

