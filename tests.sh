set -e
rm -rf dist
rm -rf venv
python -m venv venv
venv/bin/pip install wheel
find snake* -maxdepth 0 -type d -exec bash -c "cd {} && ../venv/bin/python setup.py bdist_wheel --universal" \;
mkdir dist
cp snake*/dist/*.whl dist/
venv/bin/pip install --find-links=./dist snake_e
venv/bin/python entrypoint.py