from django.db import models


class Place(models.Model):
    address = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        null=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.place}'


class Waiter(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class NewsAgency(Place):
    website = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Reporter(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    news_agency = models.ForeignKey(NewsAgency, on_delete=models.CASCADE, null=True, related_name='test')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    publications = models.ManyToManyField(Publication)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.headline}'