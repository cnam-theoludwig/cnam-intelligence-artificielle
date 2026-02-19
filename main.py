from PIL import Image

from src.compte_bancaire import CompteBancaire


def main() -> None:
    compte = CompteBancaire(titulaire="Théo", solde=100)
    print(compte)

    compte.deposer(montant=50)
    print(f"Après dépôt de 50: Solde = {compte.solde}")

    compte.retirer(montant=30)
    print(f"Après retrait de 30: Solde = {compte.solde}")

    try:
        compte.retirer(montant=200)
    except ValueError as error:
        print(f"Erreur: {error}")

    print(f"Après tentative de retrait de 200: Solde = {compte.solde}")

    image_path = "test_image.png"
    image = Image.new("RGB", (100, 100), color="red")
    image.save(image_path)

    image = Image.open(image_path)
    print(image.format, image.size, image.mode)
    image.show()


if __name__ == "__main__":
    main()
