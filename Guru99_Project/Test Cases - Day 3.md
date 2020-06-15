# AUT is NOT ready
## Mockups are available 

###### Testing areas:
| Role | Features/modules |
|--------------|-----------------------|
|Manager|New Customer|*
|Manager|New Account|*
|Manager|Edit Customer|
|Manager|Edit Account|
|Manager|Delete Customer|
|Manager|Delete Account|
|Manager|Mini Statement|
|Manager|Customized Statement|

###### Test scenario: Check the New Account functionality

| Test Case ID | Test case description | Expected Result	|
|--------------|-----------------------|------------------- |
|1                  |Customer ID is empty| System displays error
|2                  |Special characters in ID| System displays error
|3              	|Characters in ID| System displays error
|4              	|First character in ID is a space| System displays error
|5              	|Valid ID + Initial deposit less than 500| System displays error
|6              	|Valid ID + Customer ID does not associate with manager| System displays error
|19              	|Too long ID| System displays error
|20              	|Reset button click| Blank fields
|21              	|Submit button click with valid data| Pass
|2              	|Return key with valid data| Pass
|------------------|--------------------------------------------------------------------------| -----------------------------
|7              	|#1 + Initial deposit less than 500 | System displays error
|8              	|#2 + Initial deposit less than 500 | System displays error
|9              	|#3 + Initial deposit less than 500 | System displays error
|10              	|#4 + Initial deposit less than 500 | System displays error
|11              	|#1 + Customer ID does not associate with manager | System displays error
|12              	|#2 + Customer ID does not associate with manager | System displays error
|13              	|#3 + Customer ID does not associate with manager | System displays error
|14              	|#4 + Customer ID does not associate with manager | System displays error
|15              	|#11 + Initial deposit less than 500 | System displays error
|16              	|#12 + Initial deposit less than 500 | System displays error
|17              	|#13 + Initial deposit less than 500 | System displays error
|18              	|#14 + Initial deposit less than 500 | System displays error

###### Test scenario: Check the Manager New Customer functionality

| Test Case ID | Test case description | Expected Result	|
|--------------|-----------------------|------------------- |
|1              |Customer Name is empty| System displays error
|2              |Special characters in Customer Name| System displays error
|3              |Numbers in Customer Name| System displays error
|4              |First character in Customer Name is a space| System displays error
|5              |Address is empty| System displays error
|6              |First character in Address is a space| System displays error
|7              |Special characters in Address| System displays error
|8              |City is empty| System displays error
|9              |Special characters in City| System displays error
|10              |Numbers in City| System displays error
|11              |First character in City is a space| System displays error
|12              |State is empty| System displays error
|13              |Numbers in State| System displays error
|14              |Special characters in State| System displays error
|15              |First character in State is a space| System displays error
|16              |Enter e-mail existing in database| System displays error

. . . Similar tests for all visible fields, below only tests without validation.

###### Test scenario: Check the Manager Edit Customer functionality

| Test Case ID | Test case description | Expected Result	|
|--------------|-----------------------|------------------- |
|1             |Customer Name is empty| System displays error
|2             |Invalid Customer ID| System displays error
|3             |Customer Id does not associated with Manager| System displays error

###### Test scenario: Check the Manager Edit Account functionality

| Test Case ID | Test case description | Expected Result	|
|--------------|-----------------------|------------------- |
|1             |Invalid Account Number| System displays error
|2             |Account number does not associated with Manager| System displays error

###### Test scenario: Check the Manager Delete Account functionality

| Test Case ID | Test case description | Expected Result	|
|--------------|-----------------------|------------------- |
|1             |Invalid Account Number| System displays error
|2             |Account number does not associated with logged Manager| System displays error
