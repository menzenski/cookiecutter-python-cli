import json
import os
import os.path
import subprocess


def test_cookiecuttering(tmpdir):
    root_dir = os.path.join(os.path.dirname(__file__), os.pardir)

    with open(os.path.join(root_dir, 'cookiecutter.json')) as config_file:
        config_data = json.load(config_file)
        repo_name = config_data['repo_name']
        package_name = config_data['package_name']
    assert package_name and isinstance(package_name, str)

    output_dir = tmpdir.mkdir()

    subprocess.check_call([
        'cookiecutter',
        'https://github.com/menzenski/cookiecutter-python-cli',
        '--checkout',
        'pipfile',
        '--no-input',
        '--overwrite-if-exists',
        '--output-dir',
        # h/t https://gist.github.com/bryder/d11537e82c3487e310ed
        output_dir.strpath,
        # str(output_dir),
    ])

    repo_dir = output_dir.join(repo_name)

    subprocess.check_call([
        'make',
        '-C',
        repo_dir.strpath,
        # str(output_dir),
        'setup',
    ])

    subprocess.check_call([
        'make',
        '-C',
        repo_dir.strpath,
        # str(output_dir),
        'test',
    ])
