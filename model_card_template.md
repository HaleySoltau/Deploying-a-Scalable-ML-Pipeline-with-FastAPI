\# Model Card



For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf



\## Model Details



This model is a Random Forest Classifier trained to predict whether an individual's income exceeds $50K per year based on Census data. The model was developed as part of a machine learning pipeline deployment project.



\- \*\*Model Type:\*\* Random Forest Classifier

\- \*\*Model Version:\*\* 1.0

\- \*\*Framework:\*\* scikit-learn

\- \*\*Hyperparameters:\*\* 

&nbsp; - n\_estimators: 100

&nbsp; - max\_depth: 10

&nbsp; - random\_state: 42



\## Intended Use



This model is intended for educational purposes to demonstrate the deployment of a machine learning pipeline with FastAPI. It can be used to predict income levels based on demographic and employment information from Census data.



\*\*Intended Users:\*\* Data scientists, ML engineers, and students learning about MLOps and model deployment.



\*\*Out-of-Scope Uses:\*\* This model should not be used for making real-world decisions about individuals' financial status, creditworthiness, or employment without careful consideration of ethical implications and potential biases.



\## Training Data



The model was trained on the Census Income dataset from the UCI Machine Learning Repository. 



\- \*\*Dataset:\*\* Census Income Data (https://archive.ics.uci.edu/ml/datasets/census+income)

\- \*\*Size:\*\* 32,561 samples with 15 features

\- \*\*Split:\*\* 80% training (26,048 samples), 20% testing (6,513 samples)

\- \*\*Features:\*\* Age, workclass, education, marital status, occupation, relationship, race, sex, capital gain/loss, hours per week, native country

\- \*\*Target Variable:\*\* Binary classification (<=50K or >50K annual income)



\## Evaluation Data



The model was evaluated on a held-out test set comprising 20% of the original dataset (6,513 samples). The test set maintains the same feature distributions as the training data.



\## Metrics



The model's performance was evaluated using precision, recall, and F1 score:



\*\*Overall Performance:\*\*

\- \*\*Precision:\*\* 0.7962 (79.62%)

\- \*\*Recall:\*\* 0.5372 (53.72%)

\- \*\*F1 Score:\*\* 0.6416 (64.16%)



\*\*Interpretation:\*\*

\- The model correctly identifies high earners (>50K) 79.6% of the time when it predicts them (precision)

\- The model identifies 53.7% of all actual high earners in the dataset (recall)

\- The balanced F1 score of 64.2% indicates moderate overall performance



\*\*Slice Performance:\*\*

Performance varies across different demographic slices. Notable observations from slice\_output.txt:

\- Education level significantly impacts performance (higher education correlates with better recall)

\- Performance is relatively consistent across different racial groups

\- Some occupations show higher precision (e.g., Exec-managerial: 84.3% precision)



\## Ethical Considerations



\*\*Potential Biases:\*\*

\- The model uses sensitive attributes like race, sex, and native country, which could lead to discriminatory predictions

\- Historical biases in Census data may be perpetuated by the model

\- Performance varies across demographic slices, potentially leading to unfair outcomes for certain groups



\*\*Fairness Concerns:\*\*

\- The model should not be used for automated decision-making in hiring, lending, or other high-stakes scenarios

\- Regular audits should be conducted to ensure the model does not discriminate against protected groups

\- Consider removing sensitive features or using fairness-aware machine learning techniques for production use



\## Caveats and Recommendations



\*\*Limitations:\*\*

\- The model was trained on data that may not reflect current economic conditions

\- Performance on data outside the training distribution may be poor

\- The model has moderate recall (53.7%), meaning it misses nearly half of actual high earners



\*\*Recommendations:\*\*

\- Use this model only for educational and demonstration purposes

\- Before production deployment, consider: retraining with recent data, implementing fairness constraints, and conducting thorough bias testing

\- Monitor model performance continuously, especially across different demographic groups

\- Consult with domain experts and ethicists before using predictions in real-world applications

\- Consider the trade-offs between precision and recall based on the specific use case

