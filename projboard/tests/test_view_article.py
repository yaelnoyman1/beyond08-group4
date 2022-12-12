import pytest
from projboard.models.user import User
from projboard.models.article import Article, View_Article
from projboard.models.subject import Subject


TITLE = "Article Test"
CONTENT = "Anas not gonna write all that!"
NAME = "Amit"


@pytest.mark.django_db
class TestViewModel:

    @pytest.fixture
    @pytest.mark.django_db
    def create_subjects(self):
        subject = Subject(name='N')
        subject.save()
        return subject

    @pytest.fixture
    @pytest.mark.django_db
    def create_user(self):
        user = User(name=NAME, nickname="A98", email="Amit@gmail.com", password="Amit")
        user.save()
        return user

    @pytest.fixture
    @pytest.mark.django_db
    def create_articles(self, create_user, create_subjects):
        article = Article(user_id=create_user, title=TITLE, content=CONTENT, subject_id=create_subjects)
        article.save()
        return article

    @pytest.fixture
    @pytest.mark.django_db
    def create_view(self, create_user, create_articles):
        view_article = View_Article(user_id=create_user, article_id=create_articles)
        view_article.save()
        return view_article

    @pytest.mark.django_db
    def test_create_view(self, create_view):
        assert create_view in View_Article.objects.all()

    @pytest.mark.django_db
    def test_amount_of_views_article(self, create_view):
        amount_views = View_Article.amount_of_views_article(create_view.article_id)
        assert View_Article.objects.filter(article_id=create_view.article_id).count() == amount_views