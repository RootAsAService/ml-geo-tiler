
import os

from setuptools import setup, find_packages

with open('base_tiler/__init__.py') as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue


with open('README.MD') as f:
    readme = f.read()

# Runtime requirements.
inst_reqs = ["shapely", "mercantile", "numpy"]

extra_reqs = {
    'test': ['mock', 'pytest', 'pytest-cov', 'codecov']}

setup(name='ml_geo_tiler',
      version=version,
      description=u"""Export Tools for Transforming ML Models into Maps""",
      long_description=readme,
      classifiers=[
          'Intended Audience :: Information Technology',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering :: GIS'],
      keywords='raster aws tiler gdal rasterio spacenet machinelearning hotosm cog',
      author=u"David Lindenbaum",
      author_email='David.Lindenbaum@gmail.com',
      url='https://github.com/makushka/ml-geo-tiler',
      license='Apache',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      zip_safe=False,
      install_requires=inst_reqs,
      extras_require=extra_reqs)
