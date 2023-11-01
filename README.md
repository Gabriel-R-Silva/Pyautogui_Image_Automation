# Pyautogui_Image_Automation
Pyautogui project for image automation.
This README has both an English and a Portuguese version.

# README EN-US
README PT-BR
This project aims to use PyAutoGUI for test automation. The following libraries are used:
* `pyautogui`
* `time`
* `subprocess`
* `sys`
* `os`
* `datetime`

# Why use PyAutoGUI in this way?
A common issue with using AutoGUI is the need for delays and the requirement to always pass coordinates. The approach presented in this project involves searching for a specific image and deciding whether to click on it within the same function. This not only results in a click but also embeds a complete validation process, making the test more robust and precise.

# How can I use it?
The main script containing the primary function is `automated.py`. Inside it, there is the `find_image` function, which should be used in the automation process. This function searches for the image, and you can specify whether you want to perform a single click, double click, or left click. Additionally, due to the time-based loop, it will keep trying to find the image for a few seconds, eliminating the need for explicit delays. The waiting time can vary depending on the project, as it depends on external factors. In the example, we use a 5-second wait. If the image is not found within this time, a print statement will indicate which image was not found, take a screenshot, and terminate the relevant exe process, allowing for a clean execution of the process. Therefore, it is essential to go to the `automated.py` script and specify which programs should be terminated in case of failure in the `program_name` array. The `execute_script.py` script contains a function to pass an array of strings with the names of the scripts that will be executed to indicate any errors and which script returned an error. In more complex projects, multiple scripts can be used to test the automation process. To maintain organization, the execution of scripts has been separated into `script_manager.py`.

# Example of usage:
In the provided project, an example using the Windows calculator is included. There are two scripts: calc_example and calc_example_error. In the first case, it performs the addition of `1 + 1` and waits for the result `2`. In the second case, it attempts to add `2 + 2` and expects the result `2`. The second script is intentionally incorrect to demonstrate the validation process. This same concept can be applied to any system, allowing automation of any software.

# Final considerations:
This process enables the execution of complete automated black-box testing and can be incorporated into other processes and projects. It's a great option for conducting tests without relying on paid software. I've tried to explain why to use this project's approach as clearly as possible. I hope this helps, and let's start programming.


# README PT-BR
Esse projeto tem o intuito de utilizar o Pyautogui para fazer automatização de teste.
são utilizadas as seguinte bibliotecas
* `pyautogui`
* `time`
* `subprocess`
* `sys`
* `os`
* `datetime`

# Por que utilizar o pyautogui dessa maneira? 
Um problema constante que se tem com o uso do autogui é o uso de delay e uma necessidade de sempre passar coordenadas
da forma apresentada pelo projeto é passado para que seja feito a procura de determinada imagem e na própria função 
decidir se quer que se clique ou não na mesma, dessa forma além de se ter sem o resultado de clicar se tenha todo um 
processo de validação embutido o que torna o teste muito mais robusto e preciso.

# Como posso utilizar?
O Script onde possui a função principal é o `automated.py` nele existira a função `find_image` essa função que devera ser usada
no processo de automatização ela procura a imagem, é possível indicar se você deseja dar um click, double click ou left click
além disso devido a while feito por tempo ele ficara alguns segundos tentando achar a imagem isso que evita o uso do delay 
o tempo para se ficar esperando pode variar com o projeto, pois depende de fatores externos no exemplo usamos 5 segundos, 
caso nesse tempo não seja encontrado será feito um print indicando qual imagem não foi encontrada, será tirado um print da tela 
e ira matar o processo do exe em questão para assim permitir uma nova execução de processo limpa.
Por isso é importante ir no script `automated.py` e no array `program_name` indicar quais programas devem ser encerrados caso ocorra a falha
no script `execute_script.py` possui uma função para se passar um array de strings com o nome dos scripts que serão executados,
de forma a indicar caso algum retorne erro e qual retornou erro, pois em projetos mais complexos pode se ter diversos scripts para testar 
a automação do processo, apenas por questão de organização foi separado para rodar os scripts pelo `script_manager.py` apenas por questão 
de organização e deixar o script da função separado do script de execução.

# Exemplo do uso:
No projeto apresentado foi colocado um exemplo utilizando a calculadora do windows como exemplo, que são o script 
calc_example e calc_example_error no primeiro caso é feito um processo de se somar `1 + 1` e esperar o resultado `2` 
e no segundo é feito a soma de `2 + 2` e esperar o resultado `2`, esse segundo script propositalmente está errado para 
demostrar o processo de validação, esse mesmo conceito pode ser aplicado a qualquer sistema permitindo a automação 
de qualquer software.

# Considerações finais:
Esse processo permite ser realizado black box testing automatizados completos, podendo ainda ser incorporado a outros processo
e projetos, se tornando uma ótima opção para se realizar testes sem depender de softwares pagos, tentei ao máximo explicar o porque 
utilizar a forma de utilizar desse projeto espero ter ajudado e vamos programar.

