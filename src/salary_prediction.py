from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression

DATA_DIRECTORY = Path("data")


class SalaryPrediction:
    def __init__(self, train_path: Path, test_path: Path) -> None:
        self.train_data = pd.read_csv(train_path)
        self.test_data = pd.read_csv(test_path)
        self.x_train, self.y_train = self._split_features_target(self.train_data)
        self.x_test, self.y_test = self._split_features_target(self.test_data)
        self.model = LinearRegression()

    @staticmethod
    def _split_features_target(
        data: pd.DataFrame, target: str = "salary"
    ) -> tuple[pd.DataFrame, pd.Series]:
        x = data.drop(target, axis=1)
        y = data[target]
        return x, y

    def train(self) -> None:
        self.model.fit(self.x_train, self.y_train)

    def predict(
        self,
        *,
        years_of_experience: float,
        education_years: int,
        num_projects: int,
    ) -> float:
        input_data = pd.DataFrame(
            [[years_of_experience, education_years, num_projects]],
            columns=self.x_train.columns,
        )
        return self.model.predict(input_data)[0]
