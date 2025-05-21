# Last updated: 21/05/2025, 20:34:46
'''
-----
Bit Manipulation with two variables.
-----
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            # Adiciona num a 'ones' se n�o estiver em 'twos'
            # Se num j� est� em 'ones', ele � removido (XOR)
            # Se num est� em 'ones' E 'twos', 'ones' permanece (pois (ones & num) ser� num,
            # e num ^ num = 0, ent�o 'ones' n�o muda por este passo se 'twos' n�o o limpar)
            ones = (ones ^ num) & ~twos

            # Adiciona num a 'twos' se n�o estiver mais em 'ones' (ou seja, apareceu 2x)
            # Se num j� est� em 'twos', ele � removido
            twos = (twos ^ num) & ~ones
        
        return ones
