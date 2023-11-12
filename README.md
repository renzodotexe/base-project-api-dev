# FastAPI Blog API (Basisproject)

## Beschrijving

Dit basisproject implementeert een RESTful API voor **het beheren van blogposts** met behulp van FastAPI.

## Hosted API

Deze API is gehost op Okteto Cloud. Je kunt de API-documentatie en voorbeelden vinden op de volgende locatie:

[Okteto Cloud Container](https://base-project-api-dev-renzodotexe.cloud.okteto.net/docs)

## Aantoonbare Werking

Hieronder kan je screenshots vinden die elk endpoint van de API demonstreren.

### Weergeven Alle Blogposts

- ![All Blogposts](screenshots/get-all-blogposts-1.png)

### Aanmaken Blogpost

- ![Authorization](screenshots/create-blogpost-1.png)
- ![Request Body](screenshots/create-blogpost-2.png)
- ![Error On Duplicate](screenshots/create-blogpost-3.png)

### Ophalen Specifieke Blogpost

- ![Valid ID](screenshots/get-specific-blogpost-by-id-1.png)
- ![Non-valid ID](screenshots/get-specific-blogpost-by-id-2.png)

### Updaten Blogpost

- ![Changed Values](screenshots/update-specific-blogpost-by-id-1.png)
- ![Proof That ID Cannot Be Changed](screenshots/update-specific-blogpost-by-id-2.png)

### Leegmaken Database

- ![Success](screenshots/clear-database-1.png)
- ![Not Authorized](screenshots/clear-database-2.png)
- ![Proof](screenshots/clear-database-3.png)

## Volledige OpenAPI Docs

Screenshots van de volledige OpenAPI-docs pagina:

![Overzicht](screenshots/openapi-docs-1.png)
![GET - All Blogposts](screenshots/openapi-docs-2.png)
![POST - New Blogpost](screenshots/openapi-docs-3.png)
![GET - Search Blogpost By ID](screenshots/openapi-docs-4.png)
![PUT - Update Blogpost By ID](screenshots/openapi-docs-5.png)
![DELETE - Remove Blogpost By ID](screenshots/openapi-docs-6.png)
![POST - Clear Whole Database](screenshots/openapi-docs-7.png)
