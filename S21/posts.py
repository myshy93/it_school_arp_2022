import pathlib
import json

root_dir = pathlib.Path(__file__).parent
posts_file = root_dir.joinpath("files/posts.json")

try:
    with open(posts_file) as fin:
        posts = json.load(fin)
except Exception as err:
    print(err)
else:
    for i in posts:
        if i['userId'] == 7:
            print(f"{i['title'].title():=^60}")
            print("-" * 30)
            print(i['body'].capitalize())
            print()