from django.shortcuts import render, HttpResponse
from django.db.models import Sum, Count
from .models import Policy

# Create your views here.
def summary_report(request, batch_id):
    # Calculate summary report for a specific batch_id
    policies = Policy.objects.filter(batch_id=batch_id)
    total_premium = policies.aggregate(total_premium=Sum('premium'))['total_premium'] or 0
    total_sum_assured = policies.aggregate(total_sum_assured=Sum('sum_assured'))['total_sum_assured'] or 0
    total_policy_count = policies.count()
    total_rider_premium = 0  # Placeholder for rider premium

    context = {
        'batch_id': batch_id,
        'total_premium': total_premium,
        'total_sum_assured': total_sum_assured,
        'total_policy_count': total_policy_count,
        'total_rider_premium': total_rider_premium,
    }
    return render(request, 'summary_report.html', context)

def detail_report(request):
    # Fetch all policies for detailed report
    policies = Policy.objects.all()

    context = {
        'policies': policies,
    }
    return render(request, 'detail_report.html', context)

def dashboard(request):
    # Calculate totals for dashboard
    total_premium = Policy.objects.aggregate(total_premium=Sum('premium'))['total_premium'] or 0
    total_sum_assured = Policy.objects.aggregate(total_sum_assured=Sum('sum_assured'))['total_sum_assured'] or 0
    agent_codes = Policy.objects.values('agent_code').distinct()

    context = {
        'total_premium': total_premium,
        'total_sum_assured': total_sum_assured,
        'agent_codes': agent_codes,
    }
    return render(request, 'dashboard.html', context)

def home(request):
        return HttpResponse("hello")
