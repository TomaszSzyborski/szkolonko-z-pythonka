"""
Wczytaj plik DNA_losowe.txt
Majac lancuch nukleotydow z DNA stworz odpowiadajacy mu mRNA
i zapisz do pliku mRNA.txt

Wypisz do pliku - analiza_dna.txt
- wszystkie znalezione kodujace i niekodujace triplety,
- liczbe wystapien kazdego z nich
- oraz pierwsze 100 indeksow na ktorych sie znajduja

w formie:
Triplet: GCU, liczba wystapien: 11, indeksy: 1, 15, 76 ...

Baza wiedzy:
https://pl.wikipedia.org/wiki/MRNA
https://pl.wikipedia.org/wiki/Aminokwasy_bia%C5%82kowe
https://pl.wikipedia.org/wiki/Kodon
"""

"""
TABLEA KODUJĄCYCH TRIPLETÓW ZE ZRODEL
| Kodon   | Aminokwas         | Kodon   | Aminokwas   | Kodon   | Aminokwas    | Kodon   | Aminokwas   |
|---------+-------------------+---------+-------------+---------+--------------+---------+-------------|
| UUU     | fenyloalanina     | UCU     | seryna      | UAU     | tyrozyna     | UGU     | cysteina    |
| UUC     | fenyloalanina     | UCC     | seryna      | UAC     | tyrozyna     | UGC     | cysteina    |
| UUA     | leucyna           | UCA     | seryna      | UAA     | Ochre (Stop) | UGA1    | Opal (Stop) |
| UUG     | leucyna           | UCG     | seryna      | UAG     | Amber (Stop) | UGG     | tryptofan   |
| CUU     | leucyna           | CCU     | prolina     | CAU     | histydyna    | CGU     | arginina    |
| CUC     | leucyna           | CCC     | prolina     | CAC     | histydyna    | CGC     | arginina    |
| CUA     | leucyna           | CCA     | prolina     | CAA     | glutamina    | CGA     | arginina    |
| CUG     | leucyna           | CCG     | prolina     | CAG     | glutamina    | CGG     | arginina    |
| AUU     | izoleucyna        | ACU     | treonina    | AAU     | asparagina   | AGU     | seryna      |
| AUC     | izoleucyna        | ACC     | treonina    | AAC     | asparagina   | AGC     | seryna      |
| AUA     | izoleucyna        | ACA     | treonina    | AAA     | lizyna       | AGA     | arginina    |
| AUG2    | metionina (Start) | ACG     | treonina    | AAG     | lizyna       | AGG     | arginina    |
| GUU     | walina            | GCU     | alanina     | GAU     | asparaginian | GGU     | glicyna     |
| GUC     | walina            | GCC     | alanina     | GAC     | asparaginian | GGC     | glicyna     |
| GUA     | walina            | GCA     | alanina     | GAA     | glutaminian  | GGA     | glicyna     |
| GUG3    | walina            | GCG     | alanina     | GAG     | glutaminian  | GGG     | glicyna     |

"""



