from django.urls import path
from .views import (
    MembershipSelectView,
    payment_view,
    updateTransactions,
    profile_view,
    cancel_subscription
)

app_name = 'memberships'

urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select'),
    path('payment/', payment_view, name='payment'),
    path('update-transactions/<str:subscription_id>', updateTransactions, name='update-transactions'),
    path('profile/', profile_view, name='profile'),
    path('cancel/', cancel_subscription, name='cancel')
]
