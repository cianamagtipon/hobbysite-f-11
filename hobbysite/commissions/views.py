from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CommissionForm, CommissionUpdateForm, JobFormSet
from .models import Commission, Job, JobApplication

@login_required
def commission_list(request):
    commissions = Commission.objects.order_by('-created_on').all()
    return render(request, 'commissions/comission_list.html', {'commissions': commissions})


@login_required
def commission_detail(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    jobs = commission.jobs.order_by('status', '-manpower_required', 'role').all()

    if request.method == 'POST' and 'job_id' in request.POST:
        job_id = request.POST['job_id']
        job = get_object_or_404(Job, id=job_id)
        # Check if job is open and not full, and user has not already applied
        if job.status == 'Open' and not JobApplication.objects.filter(job=job, applicant=request.user).exists():
            if job.applications.filter(status='Accepted').count() < job.manpower_required:
                job_application = JobApplication(job=job, applicant=request.user, status='Pending')
                job_application.save()
                messages.success(request, 'Application submitted successfully!')
                return redirect('commissions:detail', pk=pk)
            else:
                messages.error(request, 'This job is already full.')
        else:
            messages.error(request, 'You cannot apply to this job.')

    return render(request, 'commissions/commission_detail.html', {
        'commission': commission,
        'jobs': jobs
    })


@login_required
def commission_create(request):
    JobFormSet = inlineformset_factory(
        Commission,
        Job,
        form=JobForm,
        fields=['role', 'manpower_required', 'status'],
        extra=1,
        can_delete=True
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
