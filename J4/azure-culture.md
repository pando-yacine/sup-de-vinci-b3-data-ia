# Azure pour le mastère — positionnement (culture, pas hands-on)

> Fiche courte pour la clôture J4 et pour ceux qui veulent aller plus loin.
> **On ne fait PAS de hands-on Azure dans ce cours.** Vous l'aurez en mastère.

---

## Pourquoi pas Azure aujourd'hui ?

On a fait le choix d'utiliser **Hugging Face Spaces** pour 4 raisons :

| Critère | HF Spaces | Azure App Service |
|---|---|---|
| **Carte bleue requise** | ❌ non | ✅ oui (free trial 200 $ puis CB) |
| **Time-to-deploy** | `git push hf main` → 5 min | Wizard portail + ARM template → ~30 min |
| **Spécialisation ML** | ✅ natif (registry de modèles, Spaces ML) | Possible mais c'est App Service générique |
| **Coût** | 0 € (CPU basic free) | ~13 €/mois (B1) au minimum |

→ Pour un cours de **4 jours**, HF est le bon outil. **En entreprise** ou **en mastère**, Azure (ou AWS / GCP) sera plus probable.

---

## Les 5 briques Azure que vous verrez en mastère

### 1. **Azure App Service**

L'équivalent de HF Spaces, mais sur l'écosystème Microsoft.
- **Use case** : héberger une API FastAPI ou une app Streamlit
- **Avantages vs HF** : SLA pro, scaling automatique, custom domain, certificats SSL gratuits
- **Coût** : à partir de ~13 €/mois (B1 = 1 vCPU, 1.75 Go RAM)

### 2. **Azure Blob Storage**

Stockage objet (équivalent S3 sur AWS).
- **Use case** : stocker des datasets > 1 Go, des modèles `.pkl`, des fichiers utilisateur
- **Pourquoi pas dans le repo Git** : Git est mauvais pour > 100 MB. Blob est conçu pour ça.
- **Coût** : ~0,02 €/Go/mois (très peu cher)

### 3. **Azure Machine Learning Studio**

Plateforme MLOps complète (équivalent SageMaker AWS / Vertex AI GCP).
- **Use case** : entraîner un modèle sur GPU à la demande, versionner 100+ modèles, déployer en endpoint
- **Concepts clés** : workspace, compute instance, registry de modèles, endpoints (REST API)
- **Quand passer dessus** : quand vous avez **> 5 modèles** à gérer et que `joblib.dump()` ne suffit plus

### 4. **Azure Functions** (serverless)

Code Python qui ne tourne **que quand on l'appelle**, et facturé à la milliseconde.
- **Use case** : API de prédiction légère, ETL planifié (cron), webhook
- **Avantages** : 0 € si pas utilisé, scaling automatique infini
- **Limitation** : cold start (~2 sec de latence au 1er appel)

### 5. **Application Insights**

Monitoring + logs centralisés (équivalent CloudWatch AWS / Stackdriver GCP).
- **Use case** : voir les erreurs, temps de réponse, nombre d'utilisateurs, etc. en temps réel
- **Indispensable** en prod, dispensable en démo

---

## Comparaison rapide cloud Azure / AWS / GCP

| Brique | Azure | AWS | GCP |
|---|---|---|---|
| App hébergée | App Service | Elastic Beanstalk / ECS | Cloud Run / App Engine |
| Stockage objet | Blob Storage | S3 | Cloud Storage |
| ML managé | ML Studio | SageMaker | Vertex AI |
| Serverless | Functions | Lambda | Cloud Functions |
| Database | SQL Database / Cosmos | RDS / DynamoDB | Cloud SQL / Firestore |
| Monitoring | Application Insights | CloudWatch | Cloud Monitoring |

→ Les concepts sont **transposables**. Apprenez bien Azure une fois (ou AWS, ou GCP), et vous comprendrez les 3.

---

## Quand passer de HF Spaces à Azure

Symptômes qui suggèrent qu'il est temps de migrer :

| Symptôme | Pourquoi HF ne suffit plus |
|---|---|
| Vous avez 5+ modèles à gérer | HF est pensé pour 1-3 modèles par Space. ML Studio gère 100+ avec versioning |
| Votre Space fait > 10 GB de données | HF a une limite ~50 GB mais c'est inconfortable. Blob Storage est conçu pour ça |
| Vous avez besoin de **SLA** (99,9 % uptime) | HF free n'a pas de SLA. App Service a un SLA contractuel |
| Plus de **100 utilisateurs simultanés** | HF CPU basic = 2 vCPU. App Service peut scaler horizontalement |
| **Custom domain + SSL** (`app.macompany.com`) | HF impose `*.hf.space`. App Service permet n'importe quel domain |
| **Conformité enterprise** (RGPD, ISO) | HF est moins outillé. Azure a la certification ISO 27001, GDPR-compliant, etc. |

---

## CI/CD pour Azure (équivalent HF)

Le même workflow GitHub Actions, mais avec Azure :

```yaml
name: Deploy to Azure App Service
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: azure/webapps-deploy@v3
        with:
          app-name: 'mon-app'
          publish-profile: ${{ secrets.AZURE_PUBLISH_PROFILE }}
```

Le `publish-profile` est un XML que vous téléchargez depuis le portail Azure → App Service → Get publish profile.

> **Les concepts CI/CD que vous avez vus aujourd'hui (workflow, jobs, steps, secrets, triggers) sont 100 % transposables.** Seul le step de déploiement change.

---

## Ressources pour aller plus loin (gratuites)

| Ressource | Format | Public |
|---|---|---|
| **Microsoft Learn — Azure Fundamentals (AZ-900)** | Modules en ligne, gratuit | Tous niveaux, **certification gratuite** pour étudiants |
| **Microsoft Learn — Deploy Python to App Service** | Tuto pas à pas | Niveau dév Python |
| **Microsoft Learn — Azure ML Studio** | Modules ML | Niveau data scientist |
| **Azure Free Tier** | 12 mois gratuit + 200 $ crédit | À créer **avec un email étudiant** pour éviter les charges |
| **Cloud Academy / A Cloud Guru** | Cours payants mais qualité pro | Pour la certification AZ-104 (admin) ou AI-102 (AI engineer) |

---

## Certification Azure pour étudiants

Microsoft offre **gratuitement** la certification **AZ-900** (Azure Fundamentals) aux étudiants via le programme **Imagine Cup** / **Student Ambassadors**. C'est une **vraie certification** qui s'affiche sur LinkedIn et qui rassure les recruteurs au stage / 1er job.

Démarche : créer un compte sur https://learn.microsoft.com avec votre email étudiant Sup de Vinci.

---

## En résumé

- **Aujourd'hui (B3)** : on a déployé sur HF Spaces parce que c'est gratuit, simple, et ML-friendly.
- **Mastère / 1er job** : vous croiserez Azure App Service, ML Studio, Blob Storage, App Insights.
- **Bonne nouvelle** : les concepts (Docker, CI/CD, secrets, healthcheck, monitoring) sont **les mêmes**. Vous n'avez qu'à apprendre les noms des services et 1-2 spécificités.

> Le but du J4 n'était pas de vous apprendre Azure. C'était de vous donner les **réflexes industrialisation** qui vous serviront sur **n'importe quel cloud**. Si vous comprenez pourquoi un endpoint `/api/health` est utile, ou pourquoi un secret ne doit jamais être committé, vous serez efficace sur Azure, AWS ou GCP en quelques jours.
