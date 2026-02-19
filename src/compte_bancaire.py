class CompteBancaire:
    def __init__(self, titulaire: str, solde: int = 0) -> None:
        self.titulaire: str = titulaire
        self.solde: int = solde

    def deposer(self, montant: int) -> None:
        self.solde += montant

    def retirer(self, montant: int) -> None:
        if montant > self.solde:
            raise ValueError("Fonds insuffisants.")
        self.solde -= montant

    def __str__(self) -> str:
        return f"CompteBancaire(titulaire='{self.titulaire}', solde={self.solde})"
