from django.db import models

# Create your models here.
class Policy(models.Model):
    batch_id = models.CharField(max_length=20)
    agent_code = models.CharField(max_length=20)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    sum_assured = models.DecimalField(max_digits=10, decimal_places=2)
    policy_issued_date = models.DateField()

    def __str__(self):
        return f"{self.batch_id} - {self.agent_code} - {self.policy_issued_date}"
