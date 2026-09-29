from django import forms


class LoanApplicationForm(forms.Form):

    revenue = forms.FloatField(
        label="Annual Income",
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-input",
                "placeholder": "e.g. 60000",
                "step": "1000"
            }
        )
    )

    dti_n = forms.FloatField(
        label="Debt-to-Income Ratio",
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-input",
                "placeholder": "e.g. 20",
                "step": "0.1"
            }
        )
    )