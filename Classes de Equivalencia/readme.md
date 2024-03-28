| Classe de Equivalencia | ENTRADA | CLASSES VÁLIDAS | CLASSES INVÁLIDAS |
|------------------------|---------|-----------------|-------------------|
| Triangulo | X, Y, Z | (Z - Y) < X < (Z + Y) AND (Z - X) < Y < (Z + X) AND (X - Y) < Z < (X + Y) AND X > 0 AND Y > 0 AND Z > 0 | X >= Z + Y OR Z >= X + Y OR Y >= X + Z OR X == 0 OR Y == 0 OR Z == 0 OR X < 0 OR Y < 0 OR Z < 0 |
| Triangulo Equilátero | X, Y, Z |  TRIANGULO AND X == Y AND X == Z AND Y == Z | X != Z OR X != Y OR Z != Y OR Não ser triangulo |
| Triangulo Isosceles | X, Y, Z |  TRIANGULO AND (X == Y AND X != Z AND Z != Y) OR (X == Z AND X != Y AND Y != Z) OR (Z == Y AND X != Z AND X != Y) | X == Z AND X == Y OR Y == Z AND Y == X OR Z == Y AND Z == X OR Não ser triangulo |
| Triangulo Escaleno | X, Y, Z |  TRIANGULO AND X != Y AND X != Z AND Y != Z | X == Y OR X == Z OR Z == Y OR Não ser triangulo |
