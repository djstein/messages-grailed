from django.db import models


class Channel(models.Model):
    users = models.ManyToManyField('auth.User', blank=False)
    subject = models.CharField(max_length=100)
    
    def __str__(self):
        return '%s' % (self.subject)


class Message(models.Model):
    channel = models.ForeignKey(Channel, related_name='messages', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User')
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return '%s: %s' % (self.owner.username, self.text)