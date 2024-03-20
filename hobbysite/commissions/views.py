from django.shortcuts import render, get_object_or_404
from .models import Commission

def commission_list(request):
    commissions = Commission.objects.all()
    return render(request, 'commission_list.html', {'commissions': commissions})

def commission_detail(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    return render(request, 'commission_detail.html', {'commission': commission})
