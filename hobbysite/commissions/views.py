from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CommissionForm, CommissionUpdateForm
from .models import Commission, Job, JobApplication

@login_required
def commission_list(request):
    commissions = Commission.objects.order_by('-created_on').all()
    return render(request, 'commissions/commission_list.html', {'commissions': commissions})

@login_required
def commission_detail(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    jobs = commission.jobs.order_by('status', '-manpower_required', 'role').all()
    return render(request, 'commissions/commission_detail.html', {
        'commission': commission,
        'jobs': jobs
    })

@login_required
def commission_create(request):
    if request.method == 'POST':
        form = CommissionForm(request.POST)
        if form.is_valid():
            commission = form.save(commit=False)
            commission.author = request.user
            commission.save()
            return redirect(reverse('commissions:list'))
    else:
        form = CommissionForm()
    return render(request, 'commissions/commission_form.html', {'form': form})

@login_required
def commission_update(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    if request.method == 'POST':
        form = CommissionUpdateForm(request.POST, instance=commission)
        if form.is_valid():
            form.save()
            return redirect(reverse('commissions:detail', args=[commission.pk]))
    else:
        form = CommissionUpdateForm(instance=commission)
    return render(request, 'commissions/commission_update_form.html', {'form': form, 'commission': commission})

def commission_home(request):
    return render(request, 'commissions_home.html')
