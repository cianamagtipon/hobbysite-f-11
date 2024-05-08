from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Commission, Job, JobApplication

def commission_list(request):
    commissions = Commission.objects.all()
    return render(request, 'commissions/commission_list.html', {'commissions': commissions})

@login_required
def commission_detail(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    jobs = commission.jobs.all()
    return render(request, 'commissions/commission_detail.html', {
        'commission': commission,
        'jobs': jobs
    })

@login_required
def create_commission(request):
    if request.method == 'POST':
        # Form handling logic
        pass
    return render(request, 'commissions/commission_form.html')

@login_required
def update_commission(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    if request.method == 'POST':
        # Form handling logic
        pass
    return render(request, 'commissions/commission_update_form.html', {'commission': commission})
