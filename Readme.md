# Projeto Teste QA API

# Objetivo:

Esse projeto tem como objetivo garantir a qualidade da integração da aplicação com a Dog API https://dog.ceo/dog-api/documentation.

# Automação:

Foram Criados scripts baseados nos cenários para validar que as APIs esteja respondendo corretamente, que os dados retornados estejam no formato esperado e que a aplicação se comporte conforme o esperado.

. GET /breeds/list/all

. GET /breed/{breed}/images

. GET /breeds/image/random

# O script:

. Chama a API e valida seu retorno

. Gera um report ao final do teste

# Tecnologias Utilizadas:

. Python 3 - Linguagem principal

. PyTest - Framework de testes

. Requests - Requisições HTTP

. PyTest HTML - Relatórios HTML

. Allure Report - Relatórios avançados

. GitHub Actions - CI/CD


# Estrutura do projeto 

```text
dog-api-tests/
│
├── requirements.txt
├── README.md
├── pytest.ini
│
├── tests/
│   ├── test_breeds_list.py
│   ├── test_breed_images.py
│   ├── test_random_image.py
│   └── test_invalid_breed.py
│
├── utils/
│   └── config.py
│
├── reports/
│
└── .github/
    └── workflows/
        └── api-tests.yml

