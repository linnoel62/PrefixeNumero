def prefix_number_in_vcf(file_path):
    """Lit un fichier VCF, ajoute le préfixe '01' aux numéros et modifie le fichier."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        updated_lines = []

        for line in lines:
            line = line.strip()
            if line.startswith("TEL;"):
                # Mettre à jour le numéro de téléphone
                key, number = line.split(':', 1)
                updated_number = add_prefix_to_number(number)
                updated_lines.append(f"{key}:{updated_number}\n")
            else:
                updated_lines.append(f"{line}\n")

        # Réécrire dans le même fichier
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(updated_lines)

        print(f"Les numéros de téléphone ont été mis à jour dans le fichier : {file_path}")

    except Exception as e:
        print(f"Erreur lors de la mise à jour du fichier : {e}")

def add_prefix_to_number(number):
    """Ajoute le préfixe '01' aux numéros de téléphone selon les règles."""
    if number.startswith('+229'):
        # Numéro international : insérer '01' après l'indicatif
        parts = number.split("+229")
        print (number.split("+229"))   
        return f"+229{parts[0]}01{parts[1]}"
    else:
        # Numéro local : ajouter '01' au début
        return f"01{number}"

# Remplacez par le chemin de votre fichier .vcf
file_path = "./contacts.vcf"
prefix_number_in_vcf(file_path)
