from django import forms
from django.forms import inlineformset_factory
from .models import Commission, Job

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'cols': 40, 'rows': 10}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role', 'manpower_required', 'status']
        widgets = {
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'manpower_required': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

# Define a formset for Jobs linked to the Commission
JobFormSet = inlineformset_factory(
    Commission,  # Parent model
    Job,         # Base model
    form=JobForm,
    fields=['role', 'manpower_required', 'status'],
    extra=1,     # Number of extra forms to display
    can_delete=True  # Allow the deletion of jobs
)

class CommissionUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommissionUpdateForm, self).__init__(*args, **kwargs)
        self.fields['title'].disabled = True  # Making the title field read-only
        # Automatically set status to 'Full' if all jobs are full
        commission_instance = kwargs.get('instance')
        if commission_instance:
            jobs = Job.objects.filter(commission=commission_instance)
            if jobs.exists() and all(job.status == 'Full' for job in jobs):
                self.fields['status'].initial = 'Full'
                # Optionally make the status field read-only if all jobs are full
                self.fields['status'].disabled = True

    class Meta:
        model = Commission
        fields = ['title', 'description', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'cols': 40, 'rows': 10}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_status(self):
        # Ensure that the status changes are valid based on job statuses
        status = self.cleaned_data.get('status')
        commission_instance = self.instance
        jobs = Job.objects.filter(commission=commission_instance)
        if jobs.exists() and any(job.status != 'Full' for job in jobs) and status == 'Full':
            raise forms.ValidationError("Cannot set commission to 'Full' unless all jobs are full.")
        return status
