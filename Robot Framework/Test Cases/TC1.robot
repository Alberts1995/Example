*** Settings ***
Library         Selenium2Library
Suite Setup     Go to Google


*** Test Cases ***
LoginTest
    Search and check    Russia                  Москва
    Search and check    France                  Париж
    Search and check    The Netherlands         Амстердам

*** Keywords ***
Go to Google
    Open Browser    https://www.rambler.ru/     chrome


Search and check
    [Arguments]     ${query}    ${expected_result}
    Input Text      //*[@id="main"]/div[2]/header/div[1]/div[2]/div[2]/div/div[1]/div[1]/form/input[1]  ${query}
    Click Button    //*[@id="main"]/div[2]/header/div[1]/div[2]/div[2]/div/div[1]/div[1]/form/button
    Wait Until Page Contains    ${expected_result}

