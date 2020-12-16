*** Settings ***
Library  SeleniumLibrary   #импортированная билиотека

*** Variables ***
${env}  todoist                        #так же можно предать ключь через командную строку (-v env:(название ключа)
&{url}  todoist=https://todoist.com/ru

*** Keywords ***
Start Test Case
    Open Browser  ${url.${env}}   chrome             # открывает браузер страницу
    Maximize Browser Window                                 # Во все окно

End Test Case
    Close Browser                                           # Закрытвает браузер
