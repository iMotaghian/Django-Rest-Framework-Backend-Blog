# 9-1 [reformat code] -> https://pypi.org/project/black/ & https://github.com/psf/black
docker-compose exec backend sh
pip install black
# add "black" to requirements.txt
docker-compose exec backend sh
python -m black {source_file_or_directory}
# all code reformating
black -l 78 # ech line should be 78 char


# 9-2 [flake8] review codes and find code issue or problem -> https://pypi.org/project/flake8/
docker-compose exec backend sh
pip install flake8
# add "flake8" to requirements.txt /// it can check a file or all folders -> https://flake8.pycqa.org/en/latest/
flake8 path/to/code/to/check.py
# or
flake8 path/to/code/
# or
flake8 .
# resend command that where is on code line has problem


# 9-3 [flake8 config] -> https://deku.posstree.com/en/django/flake8/
# make file in core - ".fake8"
# ignore file -> "exclude ="




