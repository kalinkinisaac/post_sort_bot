from app import communities_analyzer

print('Type keyword, count of groups, count of posts in each group')
keyword, groups_count, posts_count = input().split()

communities_analyzer.analise(keyword=keyword, groups_count=int(groups_count), posts_count=int(posts_count))
