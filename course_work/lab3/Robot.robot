*** Settings ***
Library    Process
Library    OperatingSystem
*** Variables ***
${cli}    /home/git/qa_kp01_Pidruchnyy/lab3/main.py

*** Test Cases ***
Dir root create
    ${result} =    Run Process    python3   ${cli}    get    directory    name\=root
    Should Contain    ${result.stdout}   Status code: 200

Dir inner create
    ${result} =    Run Process    python3   ${cli}    post    directory    parent\=root    name\=child    max_elems\=8
    Should Contain    ${result.stdout}   Status code: 201

Dir create not exists
    ${result} =    Run Process    python3   ${cli}    post    directory    parent\=root    name\=child    max_elems\=8
    Should Contain    ${result.stdout}   Status code: 400

Dir move
    ${result} =    Run Process    python3   ${cli}    patch    directory    name\=child    parent\=root
    Should Contain    ${result.stdout}   Status code: 200

Dir delete
    ${result} =    Run Process    python3   ${cli}    delete    directory    name\=child
    Should Contain    ${result.stdout}   Status code: 200

Dir delete not exists
    ${result} =    Run Process    python3   ${cli}    delete    directory    name\=child
    Should Contain    ${result.stdout}   Status code: 400