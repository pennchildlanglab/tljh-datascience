from setuptools import setup

setup(
  name="tljh-datascience",
  author="KatieSchuler",
  version="0.1",
  license="MIT",
  url="https://github.com/pennchildlanglab/tljh-datascience",
  entry_points = {"tljh": ["rjulia = tljh_datascience"]},
  py_modules=["tljh_datascience"],
  install_requires=["sh"],
)
