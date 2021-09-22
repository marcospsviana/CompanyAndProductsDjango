## COMPANY AND PRODUCTS PROJECT

**Objetivo**
Desenvolva um sistema web de adição, atualização, filtro e remoção de produtos de determinada empresa.
Este serviço deve atender aos seguintes requisitos:
- Adicionar empresas
- Adicionar produtos das empresas cadastradas
- Remover um produto da empresa
- Consultar todos os produtos disponíveis que tal empresa possui
- Consultar a lista de empresas cadastradas e trazer os produtos cadastrados

### **criação da estrutura inicial do projeto**

- criar o ambiente virtual

```
python3 -m venv .venv

```
- ativar o ambiente

```
source .venv/bin/activate
```
- instalar gerenciador de dependencias
```
pip install pip-tools
```
- criar o arquivos para compilação das dependencias
```
touch requirements.in requirements-dev.in
echo 'django' > requirements.in
echo '-r requirements.in' > requirements-dev.in
```
- incluir dependencias de desenvolvimento em requirements-dev.in
```
pytest
flake8
black
```
- compilar as dependencias
```
pip-compile requirements.in --generate-hashes
pip-compile requirements-dev.in --generate-hashes
```
- instalar dependencias
```
pip install -r requirements-dev.txt
```
- criar o projeto django
```
django-admin startproject comanymanager .
```
