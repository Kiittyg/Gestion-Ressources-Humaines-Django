from django.db import models
from accounts.models import User
from departments.models import Department
# Create your models here.

class Employee(models.Model):

    # lien avec utilisateur
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricule = models.CharField("Matricule", max_length=20, unique=True, blank=True)
    # identite
    
    nom = models.CharField("Nom", max_length=100)
    prenom = models.CharField("Prénom", max_length=100)

    email = models.EmailField("Email professionnel", unique=True)
    telephone = models.CharField("Téléphone", max_length=20)
    adresse = models.TextField("Adresse")

    date_naissance = models.DateField("Date de naissance")

    photo = models.ImageField("Photo de profil", upload_to='employees/photos/', null=True, blank=True)


    ETAT_CIVIL_CHOICES = (
    ('celibataire', 'Célibataire'),
    ('marie', 'Marié(e)'),
    ('divorce', 'Divorcé(e)'),
    ('veuf', 'Veuf/Veuve'),
)

    etat_civil = models.CharField(
    "État civil",
    max_length=20,
    choices=ETAT_CIVIL_CHOICES,
    default='celibataire'
)
    # RH infos
    POSTE_CHOICES = (

    # ======================
    # IT
    # ======================
    ("developpeur_fullstack", "Développeur Full Stack"),
    ("developpeur_backend", "Développeur Backend"),
    ("developpeur_frontend", "Développeur Frontend"),
    ("administrateur_systeme", "Administrateur Systèmes"),
    ("technicien_informatique", "Technicien Informatique"),
    ("chef_projet_it", "Chef de Projet IT"),
    ("responsable_it", "Responsable IT"),

    # ======================
    # Ressources Humaines
    # ======================
    ("responsable_rh", "Responsable RH"),
    ("assistant_rh", "Assistant RH"),
    ("charge_recrutement", "Chargé de Recrutement"),
    ("gestionnaire_paie", "Gestionnaire de Paie"),

    # ======================
    # Finance
    # ======================
    ("comptable", "Comptable"),
    ("chef_comptable", "Chef Comptable"),
    ("controleur_gestion", "Contrôleur de Gestion"),
    ("directeur_financier", "Directeur Financier"),

    # ======================
    # Marketing
    # ======================
    ("charge_marketing", "Chargé Marketing"),
    ("community_manager", "Community Manager"),
    ("responsable_marketing", "Responsable Marketing"),
    ("chef_produit", "Chef de Produit"),

    # ======================
    # Commercial
    # ======================
    ("commercial", "Commercial"),
    ("charge_clientele", "Chargé de Clientèle"),
    ("chef_commercial", "Chef Commercial"),
    ("responsable_ventes", "Responsable des Ventes"),

    # ======================
    # Logistique
    # ======================
    ("responsable_logistique", "Responsable Logistique"),
    ("gestionnaire_stock", "Gestionnaire de Stock"),
    ("magasinier", "Magasinier"),
    ("chauffeur", "Chauffeur"),

    # ======================
    # Administration
    # ======================
    ("assistant_administratif", "Assistant Administratif"),
    ("secretaire", "Secrétaire"),
    ("agent_entretien", "Agent d'Entretien"),
    ("agent_securite", "Agent de Sécurité"),

)

    poste = models.CharField("Niveau hiérarchique", max_length=100, choices=POSTE_CHOICES)
    
    
    NIVEAU_CHOICES = (
    ("stagiaire", "Stagiaire"),
    ("junior", "Junior"),
    ("senior", "Senior"),
    ("manager", "Manager"),
    ("directeur", "Directeur"),
)
    niveau = models.CharField(
    max_length=20,
    choices=NIVEAU_CHOICES,
    default="junior"
)
    department = models.ForeignKey(
    Department,
    on_delete=models.CASCADE,
    verbose_name="Département"
)

    TYPE_CONTRAT_CHOICES = (
    ('CDI', 'CDI'),
    ('CDD', 'CDD'),
    ('Stage', 'Stage'),
    ('Freelance', 'Freelance'),
)

    type_contrat = models.CharField(
    "Type de contrat",
    max_length=20,
    choices=TYPE_CONTRAT_CHOICES
)

    date_embauche = models.DateField("Date d'embauche")

    salaire = models.DecimalField("Salaire de base", max_digits=10, decimal_places=2)

    statut = models.CharField("Statut", max_length=20, default="actif")

    # documents
    cv = models.FileField("CV", upload_to='cv/', null=True, blank=True)
    diplome = models.FileField("Diplôme", upload_to='diplomes/', null=True, blank=True)
    contact_urgence = models.CharField(
    "Contact d'urgence",
    max_length=100,
     help_text="Ex: Nom - Numéro de téléphone - Lien de parenté"
)

    # system
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
     if not self.matricule:
        last = Employee.objects.order_by('id').last()

        if last and last.matricule:
            try:
                num = int(last.matricule.split('-')[-1]) + 1
            except:
                num = 1
        else:
            num = 1

        self.matricule = f"EMP-2026-{num:04d}"

     super().save(*args, **kwargs)

   
    def __str__(self):
        return f"{self.prenom} {self.nom}"