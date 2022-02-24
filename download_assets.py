import requests
import yaml

yml_file_names = [
    'age_pyramid_1901_2020.yml',
    'age_pyramid_2021.yml',
    'deaths_1962_2020.yml'
]


def download_file(url=None, filename=None):
    r = requests.get(url, stream=True)
    with open(f'assets/download/{filename}', 'wb') as f:
        print(f"Downloading {filename}...")
        f.write(r.content)


if __name__ == '__main__':
    for yml_file_name in yml_file_names:
        with open(f'assets/{yml_file_name}') as f:
            yml = yaml.safe_load(f)
            download_file(url=yml['direct_link'], filename=yml['file_name'])
