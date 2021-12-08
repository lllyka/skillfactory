from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment

import random


def zadany():

    #пользователи
    milva_user = User.objects.create_user(username='milva', email='milva@mail.ru', password='milva_password')
    melifaro_user = User.objects.create_user(username='melifaro', email='melifaro@mail.ru', password='melifaro_password')

    #объекты авторов
    milva = Author.objects.create(user=milva_user)
    melifaro = Author.objects.create(user=melifaro_user)

    #категории
    cat_sport = Category.objects.create(name="Спорт")
    cat_music = Category.objects.create(name="Музыка")
    cat_cinema = Category.objects.create(name="Кино")
    cat_polycy = Category.objects.create(name="Политика")

    #текст статей\новостей
    text_article_sport_cinema = """статья_спорт_кино_Мильва__статья_спорт_кино_Мильва__статья_спорт_кино_Мильва_
                                   _статья_спорт_кино_Мильва__статья_спорт_кино_Мильва__"""

    text_article_music = """статья_музыка_Мелифаро__статья_музыка_Мелифаро__статья_музыка_Мелифаро_
                            _статья_музыка_Мелифаро__статья_музыка_Мелифаро__"""

    text_news_polycy = """новость_Политика_Мелифаро__новость_Политика_Мелифаро__новость_Политика_Мелифаро__новость_Политика_Мелифаро__
                    новость_Политика_Мелифаро__новость_Политика_Мелифаро__новость_Политика_Мелифаро__новость_Политика_Мелифаро__"""

    #две статьи и новость
    article_milva = Post.objects.create(author=milva, post_type=Post.stat, title="статья_спорт_кино_Мильва",
                                        text=text_article_sport_cinema)
    article_melifaro = Post.objects.create(author=melifaro, post_type=Post.stat, title="статья_музыка_Мелифаро",
                                        text=text_article_music)
    news_melifaro = Post.objects.create(author=melifaro, post_type=Post.new, title="новость_Политика_Мелифаро", text=text_news_polycy)

    # присваивание категорий этим объектам
    PostCategory.objects.create(post=article_milva, category=cat_sport)
    PostCategory.objects.create(post=article_milva, category=cat_cinema)
    PostCategory.objects.create(post=article_melifaro, category=cat_music)
    PostCategory.objects.create(post=news_melifaro, category=cat_polycy)

    # создание комментариев
    comment1 = Comment.objects.create(post=article_milva, user=melifaro.user, text="коммент Мелифаро №1 к статье Мильва")
    comment2 = Comment.objects.create(post=article_melifaro, user=milva.user, text="коммент Мильва №2 к статье Мелифаро")
    comment3 = Comment.objects.create(post=news_melifaro, user=melifaro.user, text="коммент Мелифаро №3 к новости Мелифаро")
    comment4 = Comment.objects.create(post=news_melifaro, user=milva.user, text="коммент Мильва №4 к новости Мелифаро")


    # список всех объектов, которые можно лайкать
    list_for_like = [article_milva,
                     article_melifaro,
                     news_melifaro,
                     comment1,
                     comment2,
                     comment3,
                     comment4]

    # 100 рандомных лайков/дислайков (по четности счетчика)
    for i in range(100):
        random_obj = random.choice(list_for_like)
        if i % 2:
            random_obj.like()
        else:
            random_obj.dislike()

    # подсчет рейтинга Мильва
    rating_milva = (sum([post.rating * 3 for post in Post.objects.filter(author=milva)])
                    + sum([comment.rating for comment in Comment.objects.filter(user=milva.user)])
                    + sum([comment.rating for comment in Comment.objects.filter(post__author=milva)]))
    milva.update_rating(rating_milva)  # и обновление

    # подсчет рейтинга Мелифаро
    rating_melifaro = (sum([post.rating * 3 for post in Post.objects.filter(author=melifaro)])
                    + sum([comment.rating for comment in Comment.objects.filter(user=melifaro.user)])
                    + sum([comment.rating for comment in Comment.objects.filter(post__author=melifaro)]))
    melifaro.update_rating(rating_melifaro)  # и обновление

    # лучший автор
    best_author = Author.objects.all().order_by('-rating')[0]

    print("Лучший автор")
    print("username:", best_author.user.username)
    print("Рейтинг:", best_author.rating)
    print("")

    # лучшая статья
    best_article = Post.objects.filter(post_type=Post.article).order_by('-rating')[0]
    print("Лучшая статья")
    print("Дата:", best_article.created)
    print("Автор:", best_article.author.user.username)
    print("Рейтинг:", best_article.rating)
    print("Заголовок:", best_article.title)
    print("Превью:", best_article.preview())
    print("")
    print("Комментарии к ней")
    for comment in Comment.objects.filter(post=best_article):
        print("Дата:", comment.created)
        print("Автор:", comment.user.username)
        print("Рейтинг:", comment.rating)
        print("Комментарий:", comment.text)
        print("")
