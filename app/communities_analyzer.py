from app import Vk
import json
import time

max_posts_count = 99


def get_groups(key_word, com_type='group', sort_type=0, offset=0, count=5):
    groups = Vk.user_api.groups.search(
        q=key_word,
        type=com_type,
        sort=sort_type,
        offset=offset,
        count=count
    )
    return groups['items']


def sort_group_posts(groups, post_sort_key, count=20, offset=0):
    posts = list()
    for group in groups:
        posts += get_group_posts(group['id'], count=count, offset=offset)
    posts = sorted(posts, key=post_sort_key)

    return posts


def get_group_posts(group_id, count=20, offset=0):

    posts = list()

    for shift in range(0, count, max_posts_count):

        # Done flag
        done = False

        # How many times can bot try to request
        fail_timer = 10

        while not done and fail_timer > 0:
            try:
                time.sleep(0.34)
                # Get current posts
                new_posts = Vk.user_api.wall.get(
                    owner_id='-{}'.format(group_id),
                    count=min(max_posts_count, count-shift),
                    offset=shift+offset
                )
                posts += new_posts['items']
                # Set flag to done
                done = True

            except:

                # Error
                done = False
                fail_timer -= 1

        return posts


def get_info(group_id):
    group_info = Vk.user_api.groups.getById(group_id=str(group_id))
    time.sleep(0.34)
    return group_info[0]


def render_group_desc(group):
    return 'Name of group : {}\nDirect link : vk.com/{}'.format(group['name'], group['screen_name'])


def render_post_desc( post):
    return 'Direct link : https://vk.com/{}?w=wall{}_{}\nLikes : {}\nReposts : {}\nComments : {}\nViews : {}'.format(
        get_info(abs(int(post['owner_id'])))['screen_name'],
        post['owner_id'],
        post['id'],
        post['likes']['count'],
        post['reposts']['count'],
        post['comments']['count'],
        (post['views']['count'] if 'views' in post else 'null')
    )


def json_beauty(raw_json):
    return json.dumps(raw_json, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)


def analise():
    print("Requesting groups...\n")

    # KEYWORD HERE!
    groups = get_groups('4ch', 5)

    posts = list()
    for group in groups:
        group_info = get_info(group['id'])
        if group_info['is_closed'] == 0:
            posts += get_group_posts(group['id'], count=5, offset=1)

    posts = sorted(posts, key=lambda post: -post['likes']['count'])

    for post in posts:
        print(render_post_desc(post) + '\n')
    # print(json.dumps(get_info(best['id']), sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))


analise()
