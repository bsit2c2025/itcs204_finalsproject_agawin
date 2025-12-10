
@echo off
:askUser
SET /P userInput="Change GIT user and email [1], Change to Default [2]: "
IF "%userInput%" EQU "1"(
    echo You entered a valid number: %userInput%.
) IF "%userInput%" EQU "2"(
    git config --global user.name .
    git config --global user.email .
    ) ELSE (
    echo Invalid input. Please try again.
    GOTO askUser
)   
