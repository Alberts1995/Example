*** Settings ***
Library  SeleniumLibrary           #импортированная билиотека


*** Variables ***

&{search_text}  emal=ttrvuf0@lywenw.com  passw=Aj#%R*g54%u$x=Y  new_pr=New Project  new_chall=new challenge

*** Keywords ***

Verifi Serch result
    Press Keys  //*[@id="__next"]/div/div/header/nav/div/ul[2]/li[1]/a     [Return]
    Input Text  //*[@id="email"]      ${search_text.emal}
    Input Text  //*[@id="password"]      ${search_text.passw}
    Press Keys  //*[@id="login_form"]/button    [Return]
    Sleep   2s
    Mouse Down  //*[@id="projects_list_manager"]/div[1]/a
    Click Element   //*[@id="projects_list_manager"]/div[1]/a
    Input Text  //*[@id="edit_project_modal_field_name"]      ${search_text.new_pr}
    Press Keys  //*[@id="reactist-modal-box-3"]/form/footer/button[2]    [Return]
    Press Keys  //*[@id="editor"]/div/div[2]/div/ul/li/div/div/div/button   ${search_text.new_chall}
    Press Keys  //*[@id="editor"]/div/div[2]/div/ul/li/div/div/ul/li/form/div[2]/button[1]  new challenge2
    Sleep   2s
    Mouse Down  //*[@id="editor"]/div/div[2]/div/ul/li/div/div/ul/li[2]/form/div[1]/div[2]/button
    Click Element   //*[@id="editor"]/div/div[2]/div/ul/li/div/div/ul/li[2]/form/div[1]/div[2]/button
    Press Keys  class=scheduler-suggestions-item    [Return]
    Press Keys  //*[@id="editor"]/div/div[2]/div/ul/li/div/div/ul/li[2]/form/div[2]/button[1]  [Return]
    Press Keys  //*[@id="editor"]/div/div[2]/div/ul/li/div/div/ul/li[1]/div/div[2]/div[1]  [Return]
    Sleep   2s
    Mouse Down  class=plus_add_button
    Click Element   class=plus_add_button
    Press Keys  class=DraftEditor-root   calle
    Press Keys    class=item_editor_submit.ist_button.st_button_red    [Return]

Second Verifi Serch result

    Press Keys  //*[@id="__next"]/div/div/header/nav/div/ul[2]/li[1]/a     [Return]              #Нажатие на кнопку
    Input Text  //*[@id="email"]      name      #Вводит текст в поисковик
    Input Text  //*[@id="password"]     password             #Вводит текст в поисковик
    Press Keys  //*[@id="login_form"]/button    [Return]



