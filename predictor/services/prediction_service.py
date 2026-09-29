from pathlib import Path

import joblib

from django.conf import settings

from .data_processor import LoanDataProcessor


class LoanPredictionService:

    def __init__(self):

        self.processor = (
            LoanDataProcessor()
        )

        model_path = (
            Path(settings.BASE_DIR)
            / "models"
            / "random_forest_model.pkl"
        )

        if not model_path.exists():

            raise FileNotFoundError(
                f"Model not found at: "
                f"{model_path}"
            )

        self.model = joblib.load(
            model_path
        )

    def predict(
        self,
        revenue,
        dti_n
    ):

        applicant = (
            self.processor
            .prepare_application(
                revenue,
                dti_n
            )
        )

        prediction = (
            self.model
            .predict(applicant)[0]
        )

        probabilities = (
            self.model
            .predict_proba(
                applicant
            )[0]
        )

        classes = list(
            self.model.classes_
        )

        repayment_index = (
            classes.index(0)
        )

        default_index = (
            classes.index(1)
        )

        repayment_probability = (
            probabilities[
                repayment_index
            ] * 100
        )

        default_probability = (
            probabilities[
                default_index
            ] * 100
        )

        if prediction == 0:

            outcome = (
                "LIKELY TO REPAY"
            )

        else:

            outcome = (
                "LIKELY TO DEFAULT"
            )

        return {
            "prediction":
                int(prediction),

            "outcome":
                outcome,

            "repayment_probability":
                round(
                    float(
                        repayment_probability
                    ),
                    2
                ),

            "default_probability":
                round(
                    float(
                        default_probability
                    ),
                    2
                )
        }