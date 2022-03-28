def right_justify(word):
    print(f"{' ' * (70 - len(word))}{word}")


if __name__ == '__main__':
    print(f'este texto sempre é impresso e o que vem entre '
          f'chaves é avaliado: {2 ** 3}')
    right_justify('meu')
    # A última letra tem que estar na mesma posição final da palavra inicial
    right_justify('primeiro')
    right_justify('poema')
    right_justify('concreto')
    print(' ')
    right_justify('em python')