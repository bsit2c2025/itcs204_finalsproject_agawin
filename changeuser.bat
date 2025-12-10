@echo off
SET /P userInput="Set Git Username : "
echo Hello, %userInput%!   


git config --global user.name %userInput%

SET /P userInput="Set Git Email : "
echo Hello, %userInput%!   

git config --global user.email %userInput%

