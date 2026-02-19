import pytest

from src.compte_bancaire import CompteBancaire


def test_init_default_solde() -> None:
    # Arrange - Given
    titulaire = "Alice"

    # Act - When
    compte = CompteBancaire(titulaire=titulaire)

    # Assert - Then
    assert compte.titulaire == "Alice"
    assert compte.solde == 0


def test_init_with_solde() -> None:
    # Arrange - Given
    titulaire = "Bob"
    solde = 500

    # Act - When
    compte = CompteBancaire(titulaire=titulaire, solde=solde)

    # Assert - Then
    assert compte.titulaire == "Bob"
    assert compte.solde == 500


def test_deposer() -> None:
    # Arrange - Given
    compte = CompteBancaire(titulaire="Alice", solde=100)

    # Act - When
    compte.deposer(montant=50)

    # Assert - Then
    assert compte.solde == 150


def test_retirer_fonds_suffisants() -> None:
    # Arrange - Given
    compte = CompteBancaire(titulaire="Alice", solde=100)

    # Act - When
    compte.retirer(montant=30)

    # Assert - Then
    assert compte.solde == 70


def test_retirer_fonds_insuffisants() -> None:
    # Arrange - Given
    compte = CompteBancaire(titulaire="Alice", solde=50)

    # Act & Assert - When & Then
    with pytest.raises(ValueError, match="Fonds insuffisants"):
        compte.retirer(montant=100)
    assert compte.solde == 50


def test_str() -> None:
    # Arrange - Given
    compte = CompteBancaire(titulaire="Alice", solde=100)

    # Act - When
    result = str(compte)

    # Assert - Then
    assert result == "CompteBancaire(titulaire='Alice', solde=100)"


def test_retirer_montant_exact() -> None:
    # Arrange - Given
    compte = CompteBancaire(titulaire="Alice", solde=100)

    # Act - When
    compte.retirer(montant=100)

    # Assert - Then
    assert compte.solde == 0
