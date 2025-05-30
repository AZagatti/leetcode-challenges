# Last updated: 29/05/2025, 21:42:56
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        all_subsets = []

        # Haver� 2^n subconjuntos poss�veis.
        # Cada n�mero de 0 a 2^n - 1 pode representar um subconjunto.
        # Ex: Se n=3, iteramos de 0 (000_bin) a 7 (111_bin).
        # 2**n � o mesmo que 1 << n (1 deslocado n bits para a esquerda)
        num_subsets = 1 << n # Ou 2**n

        for i in range(num_subsets):
            current_subset = []
            # Para cada n�mero 'i', verificamos seus bits.
            # Cada bit corresponde a um elemento em 'nums'.
            for j in range(n):
                # Se o j-�simo bit de 'i' est� LIGADO (1),
                # ent�o nums[j] pertence a este subconjunto.
                # (i >> j) & 1:
                #   (i >> j) desloca o j-�simo bit de 'i' para a posi��o 0 (mais � direita).
                #   & 1      faz um "E" bit a bit com 1. Se o bit na posi��o 0 for 1,
                #            o resultado � 1. Caso contr�rio, � 0.
                if (i >> j) & 1:
                    current_subset.append(nums[j])
            
            all_subsets.append(current_subset)
            
        return all_subsets
