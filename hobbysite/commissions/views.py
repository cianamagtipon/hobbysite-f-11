from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CommissionForm, CommissionUpdateForm, JobForm, inlineformset_factory
from .models import Commission, Job, JobApplication
from django.contrib import messages


def commission_list(request):
    commissions = Commission.objects.order_by('-status', '-created_on').all()
    user_commissions = None
    applied_commissions = None

    if request.user.is_authenticated:
        user_commissions = commissions.filter(author=request.user)
        job_applications = JobApplication.objects.filter(applicant=request.user).select_related('job')
        applied_commissions = {application.job.commission for application in job_applications}

    context = {
        'commissions': commissions,
        'user_commissions': user_commissions,
        'applied_commissions': applied_commissions
    }
    return render(request, 'commissions/commission_list.html', context)


def commission_detail(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    jobs = commission.jobs.order_by('status', '-manpower_required', 'role').all()
    jobs_data = []

    for job in jobs:
        has_applied = False
        is_full = job.applications.filter(status='Accepted').count() >= job.manpower_required
        if request.user.is_authenticated:
            has_applied = JobApplication.objects.filter(job=job, applicant=request.user).exists()
        jobs_data.append({
            'job': job,
            'has_applied': has_applied,
            'is_full': is_full
        })

    if request.method == 'POST' and request.user.is_authenticated:
        job_id = request.POST.get('job_id')
        job = get_object_or_404(Job, id=job_id)
        if not JobApplication.objects.filter(job=job, applicant=request.user).exists():
            if not is_full:
                job_application = JobApplication(job=job, applicant=request.user, status='Pending')
                job_application.save()
                messages.success(request, 'Application submitted successfully!')
                return redirect('commissions:detail', pk=pk)
            else:
                messages.error(request, 'This job is already full.')
        else:
            messages.error(request, 'You have already applied for this job.')

    context = {'commission': commission, 'jobs_data': jobs_data}
    return render(request, 'commissions/commission_detail.html', context)


@login_required
def commission_create(request):
    JobFormSet = inlineformset_factory(
        Commission,
        Job,
        form=JobForm,
        fields=['role', 'manpower_required', 'status'],
        extra=1,
        can_delete=False  # Changed from True to False
    )

    if request.method == 'POST':
        form = CommissionForm(request.POST)
        formset = JobFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            commission = form.save(commit=False)
            commission.author = request.user
            commission.save()
            formset.instance = commission
            formset.save()
            return redirect(reverse('commissions:list'))
    else:
        form = CommissionForm()
        formset = JobFormSet()
    return render(request, 'commissions/commission_form.html', {'form': form, 'formset': formset})


@login_required
def commission_update(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    if request.method == 'POST':
        form = CommissionUpdateForm(request.POST, instance=commission)
        formset = JobFormSet(request.POST, instance=commission)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect(reverse('commissions:detail', args=[commission.pk]))
    else:
        form = CommissionUpdateForm(instance=commission)
        formset = JobFormSet(instance=commission)
    return render(request, 'commissions/commission_update_form.html', {'form': form, 'formset': formset, 'commission': commission})


def commission_home(request):
    return render(request, 'commissions_home.html')
