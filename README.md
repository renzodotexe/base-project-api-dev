# FastAPI Blog API (Basisproject)

## Beschrijving

Dit basisproject implementeert een RESTful API voor het beheren van blogposts met behulp van FastAPI.

## Gehoste API

Deze API is gehost op Okteto Cloud. Je kunt de API-documentatie en voorbeelden vinden op de volgende locatie:

[Okteto Cloud Container](https://blogpost-api-renzodotexe.cloud.okteto.net/docs/)

## Aantoonbare Werking

Hieronder vind je screenshots die de werking van elk API-endpoint demonstreren.

### Weergeven Alle Blogposts

- **Alle Blogposts**
  ![Alle Blogposts](screenshots/get-all-blogposts-1.png)

### Aanmaken Blogpost

- **Autorisatie**
  ![Autorisatie](screenshots/create-blogpost-1.png)
- **Request Body**
  ![Verzoekbody](screenshots/create-blogpost-2.png)
- **Fout bij duplicaat**
  ![Fout bij duplicaat](screenshots/create-blogpost-3.png)
- **Verkeerd datatype**
  ![Verkeerd datatype](screenshots/create-blogpost-4.png)

### Ophalen Specifieke Blogpost

- **Geldige ID**
  ![Geldige ID](screenshots/get-specific-blogpost-by-id-1.png)
- **Ongeldige ID**
  ![Ongeldige ID](screenshots/get-specific-blogpost-by-id-2.png)

### Updaten Blogpost

- **Gewijzigde Waarden**
  ![Gewijzigde Waarden](screenshots/update-specific-blogpost-by-id-1.png)
- **Bewijs dat ID niet kan worden gewijzigd**
  ![Bewijs dat ID niet kan worden gewijzigd](screenshots/update-specific-blogpost-by-id-2.png)

### Leegmaken Database

- **Succes**
  ![Succes](screenshots/clear-database-1.png)
- **Niet Geautoriseerd**
  ![Niet Geautoriseerd](screenshots/clear-database-2.png)
- **Bewijs**
  ![Bewijs](screenshots/clear-database-3.png)

## Volledige OpenAPI Documentatie

Screenshots van de volledige OpenAPI-docs pagina:

- **Overzicht**
  ![Overzicht](screenshots/openapi-docs-1.png)
- **GET - Alle Blogposts**
  ![GET - Alle Blogposts](screenshots/openapi-docs-2.png)
- **POST - Nieuwe Blogpost**
  ![POST - Nieuwe Blogpost](screenshots/openapi-docs-3.png)
- **GET - Zoeken Blogpost Op ID**
  ![GET - Zoeken Blogpost Op ID](screenshots/openapi-docs-4.png)
- **PUT - Bijwerken Blogpost Op ID**
  ![PUT - Bijwerken Blogpost Op ID](screenshots/openapi-docs-5.png)
- **DELETE - Verwijderen Blogpost Op ID**
  ![DELETE - Verwijderen Blogpost Op ID](screenshots/openapi-docs-6.png)
- **POST - Volledige Database Legen**
  ![POST - Volledige Database Legen](screenshots/openapi-docs-7.png)
