# Multilingual Detection of Hate in Social Media
The objective of this project is to create a <em>Deep Learning</em> model that will classify instances of hate speech.

### Results:
Below are the results of running tests on the three baseline files. 
Each of the models was trained using a dataset with 9000 instances.
The training set was split into 7200 training instances, and 1800 validation sets. 

The test set was comprised of 1000 instances which had their label removed.


| Model | Accuracy | Precision | Recall | F1     |
|-------|----------|-----------|--------|--------|
| HS    | 0.41     | 0.4148    | 0.9297 | 1.7288 |
| AG    | 0.614    | 0.2654    | 0.5049 | 0.5098 |
| TG    | 0.22     | 0.2196    | 1      | 2      |