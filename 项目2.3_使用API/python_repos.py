import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort-stars'
data = requests.get(url)
print("status code:", data.status_code)

response_dict = data.json()
print("Total repositories: ", response_dict['total_count'])

repo_dicts = response_dict['items']
print('Repostitories returned: ', len(repo_dicts))

repo_dict = repo_dicts[0]
print('\nKeys:', len(repo_dict))
for key in repo_dict.keys():
    print(key)

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, xlabel_rotation=45, show_legend=False)
chart._title = "Most_Strred Python Projects on GitHub"
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')