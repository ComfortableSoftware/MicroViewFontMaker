

#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of CF.setup.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


from setuptools import find_packages
from setuptools import setup


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="SparkFunMicroViewFontMaker",
  url="https://github.com/ComfortableSoftware/MicroViewFontMaker",
  version="0.1.0",
  package_dir={"SparkFunMicroViewFontMaker": "SparkFunMicroViewFontMaker"},
  package_data={
      "SparkFunMicroViewFontMaker": [
          "../doc/*",
          "../fonts/*",
          "../images/*",
      ]
  },
  packages=["SparkFunMicroViewFontMaker"],
  install_requires=[
      "CF",
  ],
  extras_require={
  },
  scripts=["scripts/fontMaker"],
)
