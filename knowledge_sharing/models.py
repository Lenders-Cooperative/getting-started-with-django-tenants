from django.db import models
from django.contrib.auth.models import User
from organizations.models import OrganizationModel


class KnowledgeArticles(OrganizationModel):
    article_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Questions(OrganizationModel):
    question = models.CharField(max_length=100)
    article = models.ForeignKey(
        KnowledgeArticles, related_name="questions", on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Answers(OrganizationModel):
    question = models.ForeignKey(
        Questions, related_name="answers", on_delete=models.CASCADE
    )
    answer_text = models.CharField(max_length=100)
