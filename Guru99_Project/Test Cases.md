# AUT is NOT ready
## Scenarios from SRS document 
SRS - (Software Requirements Specification)

    Scope

    Non-functional testing like stress,performance is beyond scope of this project.
    Automation testing is beyond scope.
    Functional testing & external interfaces are in scope and need to be tested
    The banking site will be only compatible with Chrome version 27 and above

###### Test scenario: Check the New Account functionality

| Test Case ID | Test case description | Expected Result	|
|--------------|-----------------------|------------------- |
|1              |Customer ID is empty| System displays error
|2              |Special characters in ID| System displays error
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

###### Other testing areas:
| Role | Features/modules |
|--------------|-----------------------|
|Manager|New Customer|
|Manager|Edit Customer|
|Manager|Delete Customer|
|Manager|New Account|
|Manager|Edit Account|
|Manager|Delete Account|
|Manager|Deposit|
|Manager|Withdrawal|
|Manager|Fund Transfer|
|Manager|Change Password|
|Manager|Balance Enquiry|
|Manager|Mini Statement|
|Manager|Customized Statement|
|Manager|Login & Logout|
|--------------|-----------------------|
|Customer|Balance enquiry|
|Customer|Fund Transfer|
|Customer|Mini Statement|
|Customer|Customized Statement|
|Customer|Change Password|
|Customer|Login & Logout|
