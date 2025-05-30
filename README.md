# Cassino PyVegas - Projeto Livre OO

**Disciplina**: Orientação a Objetos   
**Faculdade**: UnB Gama  
**Professor**: Henrique Moura  

## Descrição do Projeto
Implementação de um sistema de cassino em Python utilizando o paradigma de Orientação a Objetos. O sistema permite que um jogador compre fichas, aposte em diferentes máquinas de jogo e teste sua sorte em jogos como caça-níquel e roleta.

## Casos de Uso

### 1. Cadastrar Jogador
- **Ator**: Jogador  
- **Descrição**: O jogador informa seu nome para iniciar no cassino  
- **Pré-condição**: O cassino deve estar iniciado  
- **Pós-condição**: O jogador é criado com saldo inicial de R$100,00 e 0 fichas  

### 2. Comprar Fichas
- **Ator**: Jogador  
- **Descrição**: O jogador interage com o vendedor para comprar fichas, convertendo seu dinheiro em fichas (cada ficha custa R$5,00)  
- **Pré-condição**: O jogador deve estar cadastrado e ter dinheiro suficiente  
- **Pós-condição**: O saldo de fichas do jogador aumenta e seu dinheiro diminui proporcionalmente  

### 3. Jogar no Caça-Níquel
- **Ator**: Jogador  
- **Descrição**: O jogador escolhe a máquina caça-níquel, paga 20 fichas para jogar e tenta obter combinações de símbolos iguais para ganhar prêmios  
- **Pré-condição**: O jogador deve ter fichas suficientes  
- **Pós-condição**: O saldo de fichas do jogador é atualizado conforme o resultado do jogo  

### 4. Jogar na Roleta
- **Ator**: Jogador  
- **Descrição**: O jogador escolhe a roleta, paga 20 fichas e aposta em uma cor (vermelho ou preto). Se a cor sorteada for a escolhida, ganha 5 fichas  
- **Pré-condição**: O jogador deve ter fichas suficientes  
- **Pós-condição**: O saldo de fichas do jogador é atualizado conforme o resultado da aposta  

## Conceitos de OO Aplicados
1. **Herança**: 
   - `CacaNiquel` e `Roleta` herdam de `Maquina`
   - Classe base define métodos abstratos implementados pelas subclasses

2. **Polimorfismo**:
   - Método `jogar()` implementado de forma diferente em cada máquina
   - Comportamento específico para cada tipo de jogo

3. **Encapsulamento**:
   - Atributos privados (`__dinheiro` em `Jogador`)
   - Métodos públicos para acesso controlado (`getMoney()`, `setMoney()`)

4. **Classes Abstratas**:
   - `Maquina` como classe abstrata com método abstrato `jogar()`
   - Define interface comum para todas as máquinas

5. **Composição**:
   - `Vendedor` compõe `Jogador` para realizar transações
   - `Cassino` contém múltiplas máquinas de jogo

## Estrutura do Repositório