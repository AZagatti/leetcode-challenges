# Last updated: 29/05/2025, 21:42:40
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            # Adiciona num a 'ones' se não estiver em 'twos'
            # Se num já está em 'ones', ele é removido (XOR)
            # Se num está em 'ones' E 'twos', 'ones' permanece (pois (ones & num) será num,
            # e num ^ num = 0, então 'ones' não muda por este passo se 'twos' não o limpar)
            ones = (ones ^ num) & ~twos

            # Adiciona num a 'twos' se não estiver mais em 'ones' (ou seja, apareceu 2x)
            # Se num já está em 'twos', ele é removido
            twos = (twos ^ num) & ~ones
        
        return ones
