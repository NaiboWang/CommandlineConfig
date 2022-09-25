rm -r dist
rm -r build
rm -r commandline_config.egg-info
python setup.py sdist bdist_wheel
twine upload dist/*