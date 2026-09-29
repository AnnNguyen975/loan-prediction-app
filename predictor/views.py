from django.shortcuts import render

from .forms import LoanApplicationForm

from .services.prediction_service import (
    LoanPredictionService
)


def home(request):

    result = None

    if request.method == "POST":

        form = LoanApplicationForm(
            request.POST
        )

        if form.is_valid():

            revenue = (
                form.cleaned_data[
                    "revenue"
                ]
            )

            dti_n = (
                form.cleaned_data[
                    "dti_n"
                ]
            )

            prediction_service = (
                LoanPredictionService()
            )

            result = (
                prediction_service
                .predict(
                    revenue,
                    dti_n
                )
            )

    else:

        form = (
            LoanApplicationForm()
        )

    context = {
        "form": form,
        "result": result
    }

    return render(
        request,
        "predictor/home.html",
        context
    )