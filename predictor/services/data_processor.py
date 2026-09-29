import pandas as pd


class LoanDataProcessor:

    def __init__(self):

        self.features = [
            "revenue",
            "dti_n"
        ]

    def prepare_application(
        self,
        revenue,
        dti_n
    ):

        applicant = pd.DataFrame(
            {
                "revenue": [
                    revenue
                ],

                "dti_n": [
                    dti_n
                ]
            },
            columns=self.features
        )

        return applicant