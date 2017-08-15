import json
import os
import os.path
import subprocess


def test_cookiecuttering(monkeypatch, tmpdir):
    root_dir = os.path.join(os.path.dirname(__file__), os.pardir)

    with open(os.path.join(root_dir, 'cookiecutter.json')) as config_file:
        config_data = json.load(config_file)
        repo_name = config_data['repo_name']
        package_name = config_data['package_name']
    assert package_name and isinstance(package_name, str)

    monkeypatch.chdir(root_dir)

    subprocess.check_call([
        'cookiecutter',
        'https://github.com/menzenski/cookiecutter-python-cli',
        '--checkout',
        'pipfile',
        '--no-input',
        '--overwrite-if-exists',
    ])

    repo_dir = tmpdir.join(repo_name)

    monkeypatch.chdir(repo_dir)

    subprocess.check_call([
        'make',
        'setup',
    ])

    subprocess.check_call([
        'make',
        'test',
    ])
