import pandas as pd

from src.salary_prediction import DATA_DIRECTORY, SalaryPrediction


def _create_prediction() -> SalaryPrediction:
    return SalaryPrediction(
        train_path=DATA_DIRECTORY / "salary_train.csv",
        test_path=DATA_DIRECTORY / "salary_test.csv",
    )


def test_load_data() -> None:
    # Arrange - Given
    prediction = _create_prediction()

    # Act - When
    train_data = prediction.train_data

    # Assert - Then
    assert isinstance(train_data, pd.DataFrame)
    assert "salary" in train_data.columns
    assert "years_of_experience" in train_data.columns
    assert "education_years" in train_data.columns
    assert "num_projects" in train_data.columns
    assert len(train_data) > 0


def test_split_features_target() -> None:
    # Arrange - Given
    prediction = _create_prediction()

    # Act - When
    x_train = prediction.x_train
    y_train = prediction.y_train

    # Assert - Then
    assert "salary" not in x_train.columns
    assert len(x_train.columns) == 3
    assert len(y_train) == len(prediction.train_data)


def test_train() -> None:
    # Arrange - Given
    prediction = _create_prediction()

    # Act - When
    prediction.train()

    # Assert - Then
    assert hasattr(prediction.model, "coef_")
    assert hasattr(prediction.model, "intercept_")


def test_predict() -> None:
    # Arrange - Given
    prediction = _create_prediction()
    prediction.train()

    # Act - When
    result = prediction.predict(
        years_of_experience=3,
        education_years=16,
        num_projects=15,
    )

    # Assert - Then
    assert result > 0
