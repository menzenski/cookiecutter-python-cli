import json
import os
import os.path
import subprocess


def test_cookiecuttering(tempdir):
    root_dir = os.path.join(os.path.dirname(__file__), os.pardir)
    with open(os.path.join(root_dir, 'cookiecutter.json')) as config_file:
        config_data = json.load(config_file)
        package_name = config_data['package_name']
    assert package_name and isinstance(package_name, str)

    output_dir = tempdir.mkdir(package_name)
    subprocess.check_call([
        'cookiecutter',
        'https://github.com/menzenski/cookiecutter-python-cli',
        '--checkout',
        'pipfile',
        '--no-input',
        '--overwrite-if-exists',
        '--output-dir',
        output_dir,
    ])

    subprocess.check_call([
        'make',
        '-C',
        output_dir,
        'setup',
    ])

    subprocess.check_call([
        'make',
        '-C',
        output_dir,
        'test',
    ])
