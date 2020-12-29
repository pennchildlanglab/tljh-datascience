from setuptools import setup

setup(
  name="tljh-rjulia",
  author="KatieSchuler",
  version="0.1",
  license="MIT",
  url="https://github.com/pennchildlanglab/tljh-rjulia",
  entry_points = {"tljh": ["rjulia = "tljh_rjulia"]},
  py_modules=["tljh_rjulia"],
)
