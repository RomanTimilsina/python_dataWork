import pandas as pd
from django.core.management.base import BaseCommand
from policies.models import Policy

class Command(BaseCommand):
    help = 'Import data from data1.xlsx into Policy model'

    def handle(self, *args, **kwargs):
        try:
            df = pd.read_excel(r'C:\Users\ME\Desktop\django\insurance_project\policies\management\commands\data1.xlsx', usecols=['BatchId', 'AgentCode', 'Premium', 'SumAssured', 'PolicyIssuedDate'])            
            df = df.sort_values(by='BatchId')  # Sort by BatchID if needed

            for index, row in df.iterrows():
                policy = Policy(
                    batch_id=row['BatchId'],
                    agent_code=row['AgentCode'],
                    premium=row['Premium'],
                    sum_assured=row['SumAssured'],
                    policy_issued_date=row['PolicyIssuedDate'].date()  # Assuming 'PolicyIssuedDate' is a date field
                )
                policy.save()
            self.stdout.write(self.style.SUCCESS('Successfully imported data from data1.xlsx'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing data: {str(e)}'))
