from setuptools import setup, find_packages

setup(
    name="getpaid.yoma.batching",
    version="0.2.2-getpaid",
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['getpaid'],
    package_data={
        '': ['*.txt', '*.zcml', '*.gif', '*.js', '*.pt'],
    },
    zip_safe=False,
    author='',
    author_email='',
    description="""\
Batching Tools
""",
    license='ZPL',
    keywords="zope zope3",
    install_requires=['setuptools'],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
