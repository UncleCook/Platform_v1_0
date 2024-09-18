"""
Definition of form - only needed for uploading to databases
"""

from pyexpat import model
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

from app.models import Bids, Financials

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class BidForm(forms.ModelForm):
    
    class Meta:
        model = Bids
        fields = ['volume', 'bid_value']


class FinancialsForm(forms.ModelForm):

    class Meta:
        model = Financials
        fields = ['company', 'year', 'turnover', 'total_assets', 'total_liabilities', 'operating_profit', 'net_income', 'free_cash_flow', 'shareholder_funds', 'interest_expense', 'long_term_debt', 'equity', 'operating_margin', 'net_profit_margin', 'free_cash_flow_margin', 'interest_cover', 'return_on_assets', 'solvency_ratio', 'gearing', 'solvency_ratio']