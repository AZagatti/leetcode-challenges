# Last updated: 29/05/2025, 21:42:56
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        all_subsets = []

        # Haverá 2^n subconjuntos possíveis.
        # Cada número de 0 a 2^n - 1 pode representar um subconjunto.
        # Ex: Se n=3, iteramos de 0 (000_bin) a 7 (111_bin).
        # 2**n é o mesmo que 1 << n (1 deslocado n bits para a esquerda)
        num_subsets = 1 << n # Ou 2**n

        for i in range(num_subsets):
            current_subset = []
            # Para cada número 'i', verificamos seus bits.
            # Cada bit corresponde a um elemento em 'nums'.
            for j in range(n):
                # Se o j-ésimo bit de 'i' está LIGADO (1),
                # então nums[j] pertence a este subconjunto.
                # (i >> j) & 1:
                #   (i >> j) desloca o j-ésimo bit de 'i' para a posição 0 (mais à direita).
                #   & 1      faz um "E" bit a bit com 1. Se o bit na posição 0 for 1,
                #            o resultado é 1. Caso contrário, é 0.
                if (i >> j) & 1:
                    current_subset.append(nums[j])
            
            all_subsets.append(current_subset)
            
        return all_subsets
