## Model - View - Controller 2024

## Autor

- [Diogo Misael](https://github.com/misaeldiogo)


## MVC

####  VIEW >> é responsável pelo interface gráfica, é aquilo que o usuário vai ver.

>> HTML, XML

>> RECEBE DADOS DE >> CONTROLLER

#### MODEL >> é responsável pelo armazenamento e estruturas dos dados.

>> ENVIA >> DADOS PARA >> CONTROLLER

<< RECEBE >> DEMAND DE >> CONTROLLER

#### CONTROLLER >> é responsável pela lógica do problema.

>> RECEBE >> DADOS PARA >> CONTROLLER

<< ENVIA >> DEMAND DE >> CONTROLLER

<< ENVIA >> DADOS >> VIEW

############################

# MVC: Um Exemplo Detalhado com um Site de Validação de CPF

## Visão Geral do Padrão MVC

Você está correto em sua descrição básica do MVC (Model-View-Controller). Vamos aprofundar um pouco mais em cada componente e como eles interagem usando um exemplo prático de um site de validação de CPF.

## Os Componentes do MVC

#### Model (Modelo): Responsável pela representação dos dados e regras de negócio. No nosso exemplo, o modelo representa a estrutura de um CPF válido, incluindo regras de formatação e validação.

#### View (Visão): Responsável pela interface gráfica que o usuário vê e interage. No site de validação de CPF, a view seria o formulário HTML para inserir o CPF, juntamente com mensagens de erro ou sucesso.

#### Controller (Controlador): Atua como intermediário entre a view e o model, processando as requisições do usuário e manipulando os dados do model. No nosso exemplo, o controller recebe o CPF digitado pelo usuário, valida-o usando o model e atualiza a view com o resultado (válido ou inválido).

## Fluxo de Interação no Exemplo do CPF

Usuário digita o CPF no formulário HTML (View).

O formulário HTML envia o CPF para o controller.

O controller recebe o CPF e o passa para o model para validação.

O model verifica se o CPF é válido de acordo com as regras definidas.

O resultado da validação (válido ou inválido) é retornado ao controller.

O controller atualiza a view com a mensagem de validação (válido ou inválido).

## Benefícios do Padrão MVC

#### Separação de preocupações: 

Cada componente tem responsabilidades bem definidas, tornando o código mais organizado e fácil de manter.

#### Reuso de código: 

Componentes podem ser reutilizados em diferentes partes da aplicação.

#### Testabilidade: 

Cada componente pode ser testado de forma independente.

#### Manutenibilidade: 

O código é mais fácil de ser atualizado e modificado.

## Exemplo de Tecnologias Usadas com MVC

HTML, CSS e JavaScript: Tecnologias web comuns para criar a view.

Java, Python, PHP: Linguagens de programação para implementar o controller e model.

Bibliotecas e frameworks: Diversas ferramentas facilitam a implementação do MVC em diferentes linguagens e plataformas.

## Projetos Pequenos

#### Basta criar apenas: Arquivos Python ou outros formatyos.

## Projetos Grandes

#### Preciso criar:

PASTA: MODEL, VIEW, CONTROLLER.

>> Dentro de cada pasta crio os arquivos.

Exemplo:

>> Pasta Controller  >> Aquivo >> controller_restrito.py  >> Arquivo >> controller_acesso.py

## Próximos Passos

Você deu um ótimo começo! Para aprofundar sua compreensão do MVC, recomendo:

Explorar exemplos práticos em diferentes linguagens e frameworks.

Experimentar implementar um projeto simples usando o padrão MVC.

Consultar tutoriais e documentações online para aprender mais sobre o padrão e suas melhores práticas.

Estou aqui para ajudar se você tiver mais perguntas!

## Recursos Adicionais

Se você estiver interessado em aprender mais sobre MVC, aqui estão alguns recursos úteis:

Wikipedia: Model-View-Controller: https://tr.wikipedia.org/wiki/Vikipedi:%C4%B0%C5%9F_birli%C4%9Fi_projesi/2022/51._hafta/Mustafa_MVC

ASP.NET MVC: https://learn.microsoft.com/en-us/aspnet/mvc/

MVC Tutorial: https://www.tutorialspoint.com/asp.net_mvc/index.htm

Observação: Em seu exemplo, você mencionou XML como uma tecnologia para a View. Embora o XML possa ser usado para representar dados, é mais comum usar HTML para criar interfaces gráficas web.