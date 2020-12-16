*** Settings ***
Documentation  Basic Search Functionality
Resource  Information.robot
Resource  Start Ebay.robot

Test Setup  Start Ebay.Start Test Case
Test Teardown  Start Ebay.End Test Case


*** Test Cases ***
#gjpbnbdysq Случай
Verify basic search functionality for eBay
    [Documentation]  This test case verifiles the basic search
    [Tags]  Functional

    Verifi Serch result

#Неативный случай (не правильный password и Email)
Verify basic search functionality for eBay
   [Documentation]  This test case verifiles the basic search
   [Tags]  Functional

    Second Verifi Serch result









