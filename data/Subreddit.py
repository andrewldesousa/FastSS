class ClassEnum:
        EXPLAIN_SOMETHING = 'explain_something'
        SCIENCE = 'science'
        POLITICS = 'politics'
        COMPUTER_SCIENCE = 'computerscience'
        ECONOMICS = 'economics'
        MONEY = 'money'
        GENERAL = 'general'
        PHILOSOPHY = 'philosophy'
        LIFE = 'life'
        EDUCATION = 'education'
        ART_AND_CULTURE = 'art_and_culture'
        HAPPY = 'happy'
        SAD = 'sad'
        NEWS = 'news'
        PHILOSOPHY = 'philosophy'


class Subreddits:
    # Subreddits mapped to a list of topics
    subreddits_and_topics = [
        ('politics', [ClassEnum.POLITICS]),
        ('science', [ClassEnum.SCIENCE]),
        ('learnpython', [ClassEnum.COMPUTER_SCIENCE, ClassEnum.EDUCATION]),
        ('datascience', [ClassEnum.COMPUTER_SCIENCE]),
        ('compsci', [ClassEnum.COMPUTER_SCIENCE]),
        ('machinelearning', [ClassEnum.COMPUTER_SCIENCE]),
        ('personalfinance', [ClassEnum.MONEY, ClassEnum.LIFE]),
        ('cscareerquestions', [ClassEnum.MONEY, ClassEnum.COMPUTER_SCIENCE]),
        ('Economics', [ClassEnum.ECONOMICS, ClassEnum.MONEY, ClassEnum.NEWS]),
        ('todayilearned', [ClassEnum.GENERAL]),
        ('movies', [ClassEnum.ART_AND_CULTURE]),
        ('explainlikeimfive', [ClassEnum.EXPLAIN_SOMETHING]),
        ('UpliftingNews', [ClassEnum.NEWS]),
        ('philosophy', [ClassEnum.PHILOSOPHY]),
        ('Parenting', [ClassEnum.LIFE]),
        ('lifehacks', [ClassEnum.LIFE]),
        ('blog', [ClassEnum.GENERAL]),
        ('gametheory', [ClassEnum.ECONOMICS, ClassEnum.COMPUTER_SCIENCE]),
        ('askscience', [ClassEnum.SCIENCE]),
    ]

    def list_subreddits(self):
        return [i[0] for i in self.subreddits_and_topics]