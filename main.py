import matplotlib.pyplot as plt

from src.salary_prediction import DATA_DIRECTORY, SalaryPrediction

prediction = SalaryPrediction(
    train_path=DATA_DIRECTORY / "salary_train.csv",
    test_path=DATA_DIRECTORY / "salary_test.csv",
)
prediction.train()

y_pred = prediction.model.predict(prediction.x_test)

salary = prediction.predict(
    years_of_experience=2,
    education_years=5,
    num_projects=20,
)
print(salary)

plt.scatter(prediction.x_test["years_of_experience"], prediction.y_test)
plt.plot(prediction.x_test["years_of_experience"], y_pred, color="red")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary vs Years of Experience")
plt.show()
