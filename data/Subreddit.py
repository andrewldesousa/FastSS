from enum import Enum


class ClassEnum(Enum):
        EXPLAIN_SOMETHING = 0
        SCIENCE = 1
        POLITICS = 2
        COMPUTER_SCIENCE = 3
        ECONOMICS = 4
        MONEY = 5
        GENERAL = 6
        PHILOSOPHY = 7
        LIFE = 8
        EDUCATION = 9
        NEWS = 10


class Subreddits:
    # Subreddits mapped to a list of topics
    subreddits_and_topics = [
        ('politics', [ClassEnum.POLITICS, ClassEnum.NEWS]),
        ('science', [ClassEnum.SCIENCE, ClassEnum.EXPLAIN_SOMETHING]),
        ('learnpython', [ClassEnum.COMPUTER_SCIENCE, ClassEnum.EDUCATION]),
        ('datascience', [ClassEnum.COMPUTER_SCIENCE]),
        ('compsci', [ClassEnum.COMPUTER_SCIENCE]),
        ('personalfinance', [ClassEnum.MONEY, ClassEnum.LIFE]),
        ('cscareerquestions', [ClassEnum.LIFE, ClassEnum.COMPUTER_SCIENCE]),
        ('Economics', [ClassEnum.ECONOMICS, ClassEnum.MONEY, ClassEnum.NEWS]),
        ('todayilearned', [ClassEnum.GENERAL]),
        ('explainlikeimfive', [ClassEnum.EXPLAIN_SOMETHING]),
        ('UpliftingNews', [ClassEnum.NEWS]),
        ('Parenting', [ClassEnum.LIFE]),
        ('lifehacks', [ClassEnum.LIFE, ClassEnum.GENERAL]),
        ('blog', [ClassEnum.GENERAL]),
        ('gametheory', [ClassEnum.ECONOMICS, ClassEnum.COMPUTER_SCIENCE]),
        ('askscience', [ClassEnum.SCIENCE]),
    ]

    @classmethod
    def list_subreddits(cls):
        return [i[0] for i in cls.subreddits_and_topics]