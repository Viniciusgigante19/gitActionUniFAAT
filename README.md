# Atividade de CI com GitHub Actions

Este repositório contém uma aplicação de calculadora simples com testes e um workflow de Integração Contínua (CI) configurado com GitHub Actions.

## Funcionamento do CI

O workflow de CI está definido no arquivo `.github/workflows/ci.yml`. Ele é acionado a cada `push` para o repositório. As etapas do workflow são:

1.  **Checkout:** O código do repositório é baixado para o ambiente de execução.
2.  **Setup Python:** O ambiente Python na versão 3.9 é configurado.
3.  **Install Dependencies:** As dependências do projeto, listadas no arquivo `requirements.txt`, são instaladas.
4.  **Run Tests:** Os testes definidos na pasta `tests/` são executados com o `pytest`.

Se qualquer uma dessas etapas falhar, o workflow indicará um erro, notificando que as alterações recentes podem ter quebrado o projeto.

## Exercício

**Objetivo:** Adicionar uma nova funcionalidade à calculadora, com seu respectivo teste, e demonstrar o funcionamento do pipeline de CI.

**Passos:**

1.  **Crie uma nova feature:**
    *   Abra o arquivo `app/calc.py`.
    *   Adicione uma nova função à calculadora. Sugestão: uma função de potenciação (`potencia(base, expoente)`).

2.  **Adicione um novo teste:**
    *   Abra o arquivo `tests/test_calc.py`.
    *   Adicione um novo teste para a função que você criou. O teste deve verificar se a função retorna o resultado esperado para diferentes entradas.

3.  **Demonstre seu conhecimento em CI:**
    *   Faça o `commit` e o `push` das suas alterações para o seu repositório no GitHub.
    *   Acesse a aba "Actions" do seu repositório.
    *   Tire um print da tela mostrando o workflow de CI sendo executado com sucesso (com um ícone de "check" verde).
    *   Adicione este print ao seu relatório/entrega para comprovar que você completou o exercício e que suas alterações passaram nos testes automatizados.

## Como Entregar o Exercício

A entrega deve ser feita através de um **Pull Request (PR)** a partir de um `fork` deste repositório.

**Passo a Passo:**

1.  **Faça um Fork:**
    *   No canto superior direito da página deste repositório no GitHub, clique no botão **Fork**.
    *   Isso criará uma cópia completa do repositório na sua própria conta do GitHub.

2.  **Clone o Seu Fork:**
    *   Na página do **seu fork**, clique no botão verde **Code** e copie a URL (HTTPS ou SSH).
    *   No seu terminal, execute o comando:
        ```bash
        git clone <URL_DO_SEU_FORK>
        ```

3.  **Crie uma Nova Branch:**
    *   Navegue para o diretório do projeto clonado e crie uma branch para suas alterações:
        ```bash
        cd <NOME_DO_REPOSITORIO>
        git checkout -b minha-nova-feature
        ```

4.  **Realize as Alterações:**
    *   Implemente a nova função na calculadora e adicione o teste, conforme descrito na seção "Exercício".

5.  **Faça o Commit e o Push:**
    *   Adicione e confirme suas alterações:
        ```bash
        git add .
        git commit -m "feat: Adiciona função de potenciação e teste"
        ```
    *   Envie a sua branch para o **seu fork** no GitHub:
        ```bash
        git push origin minha-nova-feature
        ```

6.  **Crie o Pull Request (PR):**
    *   Abra a página do **seu fork** no GitHub.
    *   O GitHub geralmente mostrará um aviso para criar um Pull Request a partir da sua branch recém-enviada. Clique em **Compare & pull request**.
    *   Se o aviso não aparecer, vá para a aba **Pull Requests** e clique em **New pull request**.
    *   Certifique-se de que o `base repository` seja o repositório **original** e o `head repository` seja o **seu fork**.
    *   O `compare` deve ser a sua branch (`minha-nova-feature`) e o `base` deve ser a branch `main` do repositório original.
    *   Adicione um título e uma breve descrição para o seu PR.
    *   Clique em **Create pull request**.

7.  **Entregue:**
    *   O link do seu Pull Request é o que você deve entregar como comprovação da atividade. O PR mostrará suas alterações e o status do workflow de CI, que deve passar com sucesso.
