import json

import psaw


def download_subreddit_comments(subreddit, start, count, destination):
    api = psaw.PushshiftAPI()

    fields = [
        'author',
        'author_flair_text',
        'body',
        'created_utc',
        'gildings',
        'id',
        'parent_id',
        'permalink',
        'score',
        'subreddit',
        'subreddit_id',
    ]
    start_epoch = int(start.timestamp())

    gen = api.search_comments(subreddit=subreddit, filter=fields, after=start)

    output_path = destination / subreddit
    if not output_path.exists():
        print("creating output directory: {}".format(output_path))
        output_path.mkdir()

    comments_saved = 0
    while comments_saved < count:
        comment = next(gen)

        if comments_saved % 50 == 0:
            print("comment {}: {}".format(comments_saved, comment.body))

        output_file = output_path / "{}.json".format(comment.id)
        json.dump(comment.d_, output_file.open('w', encoding='utf8'))
        comments_saved += 1






